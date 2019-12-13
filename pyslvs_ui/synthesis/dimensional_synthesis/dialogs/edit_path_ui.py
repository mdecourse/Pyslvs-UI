# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyslvs_ui/synthesis/dimensional_synthesis/dialogs/edit_path.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.move_tab = QtWidgets.QWidget()
        self.move_tab.setObjectName("move_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.move_tab)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.move_x_label = QtWidgets.QLabel(self.move_tab)
        self.move_x_label.setObjectName("move_x_label")
        self.gridLayout.addWidget(self.move_x_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.move_y_label = QtWidgets.QLabel(self.move_tab)
        self.move_y_label.setObjectName("move_y_label")
        self.gridLayout.addWidget(self.move_y_label, 1, 0, 1, 1)
        self.move_y = QtWidgets.QDoubleSpinBox(self.move_tab)
        self.move_y.setMinimum(-1000000.0)
        self.move_y.setMaximum(1000000.0)
        self.move_y.setObjectName("move_y")
        self.gridLayout.addWidget(self.move_y, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.move_x = QtWidgets.QDoubleSpinBox(self.move_tab)
        self.move_x.setMinimum(-1000000.0)
        self.move_x.setMaximum(1000000.0)
        self.move_x.setObjectName("move_x")
        self.gridLayout.addWidget(self.move_x, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 99, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.move_button = QtWidgets.QPushButton(self.move_tab)
        self.move_button.setDefault(True)
        self.move_button.setObjectName("move_button")
        self.horizontalLayout_3.addWidget(self.move_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.move_tab, "")
        self.scale_tab = QtWidgets.QWidget()
        self.scale_tab.setObjectName("scale_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scale_tab)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scale_h_label = QtWidgets.QLabel(self.scale_tab)
        self.scale_h_label.setObjectName("scale_h_label")
        self.gridLayout_2.addWidget(self.scale_h_label, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 3, 1, 1)
        self.scale_v_label = QtWidgets.QLabel(self.scale_tab)
        self.scale_v_label.setObjectName("scale_v_label")
        self.gridLayout_2.addWidget(self.scale_v_label, 1, 0, 1, 1)
        self.scale_h = QtWidgets.QDoubleSpinBox(self.scale_tab)
        self.scale_h.setMinimum(1.0)
        self.scale_h.setMaximum(10000.0)
        self.scale_h.setObjectName("scale_h")
        self.gridLayout_2.addWidget(self.scale_h, 0, 1, 1, 1)
        self.scale_v = QtWidgets.QDoubleSpinBox(self.scale_tab)
        self.scale_v.setMinimum(1.0)
        self.scale_v.setMaximum(10000.0)
        self.scale_v.setObjectName("scale_v")
        self.gridLayout_2.addWidget(self.scale_v, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 3, 1, 1)
        self.scale_r_label = QtWidgets.QLabel(self.scale_tab)
        self.scale_r_label.setObjectName("scale_r_label")
        self.gridLayout_2.addWidget(self.scale_r_label, 2, 0, 1, 1)
        self.scale_rx = QtWidgets.QDoubleSpinBox(self.scale_tab)
        self.scale_rx.setMinimum(-1000000.0)
        self.scale_rx.setMaximum(1000000.0)
        self.scale_rx.setObjectName("scale_rx")
        self.gridLayout_2.addWidget(self.scale_rx, 2, 1, 1, 1)
        self.scale_ry = QtWidgets.QDoubleSpinBox(self.scale_tab)
        self.scale_ry.setMinimum(-1000000.0)
        self.scale_ry.setMaximum(1000000.0)
        self.scale_ry.setObjectName("scale_ry")
        self.gridLayout_2.addWidget(self.scale_ry, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 3, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 52, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.scale_button = QtWidgets.QPushButton(self.scale_tab)
        self.scale_button.setDefault(True)
        self.scale_button.setObjectName("scale_button")
        self.horizontalLayout_4.addWidget(self.scale_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.scale_tab, "")
        self.reduce_tab = QtWidgets.QWidget()
        self.reduce_tab.setObjectName("reduce_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.reduce_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reduce_n = QtWidgets.QSpinBox(self.reduce_tab)
        self.reduce_n.setMinimum(1)
        self.reduce_n.setObjectName("reduce_n")
        self.gridLayout_3.addWidget(self.reduce_n, 0, 1, 1, 1)
        self.reduce_n_label = QtWidgets.QLabel(self.reduce_tab)
        self.reduce_n_label.setObjectName("reduce_n_label")
        self.gridLayout_3.addWidget(self.reduce_n_label, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 193, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.reduce_button = QtWidgets.QPushButton(self.reduce_tab)
        self.reduce_button.setObjectName("reduce_button")
        self.horizontalLayout_5.addWidget(self.reduce_button)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.reduce_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout.addWidget(self.button_box)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.button_box.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Path process"))
        self.move_x_label.setText(_translate("Dialog", "X coordinate: "))
        self.move_y_label.setText(_translate("Dialog", "Y coordinate: "))
        self.move_button.setText(_translate("Dialog", "Move"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.move_tab), _translate("Dialog", "Move"))
        self.scale_h_label.setText(_translate("Dialog", "Horizontal: "))
        self.scale_v_label.setText(_translate("Dialog", "Vertical: "))
        self.scale_r_label.setText(_translate("Dialog", "Reference point: "))
        self.scale_button.setText(_translate("Dialog", "Scale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scale_tab), _translate("Dialog", "Scale"))
        self.reduce_n_label.setText(_translate("Dialog", "Reduce the points for each:"))
        self.reduce_button.setText(_translate("Dialog", "Reduce"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reduce_tab), _translate("Dialog", "Reduce"))
from pyslvs_ui import icons_rc
