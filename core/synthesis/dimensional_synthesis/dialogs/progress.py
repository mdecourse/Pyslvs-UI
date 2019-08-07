# -*- coding: utf-8 -*-

"""The progress dialog of dimensional synthesis algorithm."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import List, Dict, Any
from core.QtModules import (
    QDialog,
    Qt,
    QTimer,
    Signal,
    Slot,
)
from core.info import logger
from .Ui_progress import Ui_Dialog
from .thread import WorkerThread
from .options import AlgorithmType


class ProgressDialog(QDialog, Ui_Dialog):

    """Progress dialog.

    + Batch execute function.
    + Interrupt function.
    """

    stop_signal = Signal()

    def __init__(
        self,
        type_num: AlgorithmType,
        mech_params: Dict[str, Any],
        setting: Dict[str, Any],
        parent
    ):
        super(ProgressDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.rejected.connect(self.__close_work)

        self.mechanisms: List[Dict[str, Any]] = []

        # Batch label.
        if 'max_gen' in setting:
            self.limit = setting['max_gen']
            if self.limit > 0:
                self.batch_label.setText(f"{self.limit} generation(s)")
            else:
                self.batch_label.setText('∞')
            self.limit_mode = 'max_gen'
        elif 'min_fit' in setting:
            self.limit = setting['min_fit']
            self.batch_label.setText(f"fitness less then {self.limit}")
            self.limit_mode = 'min_fit'
        elif 'max_time' in setting:
            self.limit = setting['max_time']
            self.batch_label.setText(
                f"{self.limit // 3600:02d}:"
                f"{self.limit % 3600 // 60:02d}:"
                f"{self.limit % 3600 % 60:02d}"
            )
            self.limit_mode = 'max_time'
        else:
            self.limit = 0
            self.batch_label.setText('∞')
            self.limit_mode = 'max_gen'
        self.loopTime.setEnabled(self.limit > 0)

        # Timer.
        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.__set_time)
        self.time_spend = 0.

        # Worker thread.
        self.work = WorkerThread(type_num, mech_params, setting, self)
        self.stop_signal.connect(self.work.stop)
        if self.work.is_two_kernel():
            self.fast_kernel_label.hide()
        else:
            self.full_kernel_label.hide()
        self.work.progress_update.connect(self.__set_progress)
        self.work.result.connect(self.__get_result)
        self.work.finished.connect(self.__finish)

    @Slot(int, str)
    def __set_progress(self, progress: int, fitness: str):
        """Progress bar will always full."""
        value = progress + self.limit * self.work.current_loop
        if self.limit_mode in {'min_fit', 'max_time'} or self.limit == 0:
            self.progress_bar.setMaximum(value)
        self.progress_bar.setValue(value)
        self.fitness_label.setText(fitness)

    @Slot()
    def __set_time(self):
        """Set time label."""
        self.time += 1
        t_min = self.time % 3600
        self.time_label.setText(
            f"{self.time // 3600:02d}:"
            f"{t_min // 60:02d}:"
            f"{t_min % 60:02d}"
        )

    @Slot(name='on_start_button_clicked')
    def __start(self):
        """Start the process."""
        loop = self.loopTime.value()
        self.progress_bar.setMaximum(self.limit * loop)
        if self.limit_mode in {'min_fit', 'max_time'} or self.limit == 0:
            # Progress bar will show generations instead of percent.
            self.progress_bar.setFormat("%v generations")
        self.work.set_loop(loop)
        self.timer.start()
        self.work.start()
        self.start_button.setEnabled(False)
        self.loopTime.setEnabled(False)
        self.interrupt_button.setEnabled(True)

    @Slot(dict)
    def __get_result(self, mechanism: Dict[str, Any]):
        """Get the result."""
        self.mechanisms.append(mechanism)
        self.time_spend += mechanism['time']

    @Slot()
    def __finish(self):
        """Finish the process."""
        self.timer.stop()
        self.accept()

    @Slot(name='on_interrupt_button_clicked')
    def __interrupt(self):
        """Interrupt the process."""
        if self.work.isRunning():
            self.stop_signal.emit()
            logger.info("The thread has been interrupted.")

    @Slot()
    def __close_work(self):
        """Close the thread."""
        if self.work.isRunning():
            self.stop_signal.emit()
            logger.info("The thread has been canceled.")
