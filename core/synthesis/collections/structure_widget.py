# -*- coding: utf-8 -*-

"""The widget of 'Structure' tab."""

from __future__ import annotations

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    TYPE_CHECKING,
    List,
    Tuple,
    Sequence,
    Dict,
    Optional,
)
from core.QtModules import (
    Signal,
    Slot,
    qt_image_format,
    Qt,
    QMessageBox,
    QProgressDialog,
    QCoreApplication,
    QListWidgetItem,
    QInputDialog,
    QImage,
    QSize,
    QWidget,
    QPainter,
    QPointF,
    QPixmap,
    QApplication,
)
from core.graphics import (
    to_graph,
    engine_picker,
    engines,
)
from core.libs import (
    Graph,
    link_assortments as l_a,
    contracted_link_assortments as c_l_a,
    labeled_enumerate,
    is_planar,
)
from .Ui_structure_widget import Ui_Form

if TYPE_CHECKING:
    from core.widgets import MainWindowBase


class StructureWidget(QWidget, Ui_Form):

    """Structure widget.

    Preview the structures that was been added in collection list by user.
    """

    layout_sender = Signal(Graph, dict)

    def __init__(self, parent: MainWindowBase):
        """Get IO dialog functions from parent."""
        super(StructureWidget, self).__init__(parent)
        self.setupUi(self)
        self.output_to = parent.output_to
        self.save_reply_box = parent.save_reply_box
        self.input_from = parent.input_from
        self.addPointsByGraph = parent.add_points_by_graph
        self.unsaveFunc = parent.workbook_no_save
        self.is_monochrome = parent.monochrome_option.isChecked

        # Data structures.
        self.collections: List[Graph] = []
        self.collections_layouts: List[Dict[int, Tuple[float, float]]] = []
        self.collections_grounded: List[Graph] = []

        # Engine list.
        self.graph_engine.addItems(engines)

    def clear(self):
        """Clear all sub-widgets."""
        self.grounded_merge.setEnabled(False)
        self.configure_button.setEnabled(False)
        self.collections.clear()
        self.collection_list.clear()
        self.__clear_selection()

    @Slot(name='on_clear_button_clicked')
    def __user_clear(self):
        """Ask user before clear."""
        if not self.collections:
            return
        if QMessageBox.question(
            self,
            "Delete",
            "Sure to remove all your collections?"
        ) != QMessageBox.Yes:
            return

        self.clear()
        self.unsaveFunc()

    @Slot(name='on_graph_link_as_node_clicked')
    @Slot(name='on_graph_show_label_clicked')
    @Slot(name='on_reload_atlas_clicked')
    @Slot(int, name='on_graph_engine_currentIndexChanged')
    def __reload_atlas(self):
        """Reload atlas with the engine."""
        current_pos = self.collection_list.currentRow()
        self.collections_layouts.clear()
        self.collection_list.clear()
        self.__clear_selection()

        if not self.collections:
            return

        progress_dlg = QProgressDialog(
            "Drawing atlas...",
            "Cancel",
            0,
            len(self.collections),
            self
        )
        progress_dlg.setAttribute(Qt.WA_DeleteOnClose, True)
        progress_dlg.setWindowTitle("Type synthesis")
        progress_dlg.resize(400, progress_dlg.height())
        progress_dlg.setModal(True)
        progress_dlg.show()
        engine_str = self.graph_engine.currentText()
        for i, g in enumerate(self.collections):
            QCoreApplication.processEvents()
            if progress_dlg.wasCanceled():
                progress_dlg.deleteLater()
                return

            item = QListWidgetItem(f"No. {i + 1}")
            engine = engine_picker(g, engine_str, self.graph_link_as_node.isChecked())
            item.setIcon(to_graph(
                g,
                self.collection_list.iconSize().width(),
                engine,
                self.graph_link_as_node.isChecked(),
                self.graph_show_label.isChecked(),
                self.is_monochrome()
            ))
            self.collections_layouts.append(engine)
            item.setToolTip(f"{g.edges}")
            self.collection_list.addItem(item)
            progress_dlg.setValue(i + 1)

        progress_dlg.deleteLater()
        self.collection_list.setCurrentRow(current_pos)

    def __test_graph(self, graph: Graph) -> bool:
        """Test graph and return True if it is valid."""
        error = ""
        if not graph.edges:
            error = "is an empty graph"
        else:
            if not graph.is_connected():
                error = "is not a close chain"
            if not is_planar(graph):
                error = "is not a planar chain"
            for graph_ in self.collections:
                if graph.is_isomorphic(graph_):
                    error = f"is isomorphic with: {graph_.edges}"
        if error:
            QMessageBox.warning(self, "Add Collection Error", f"Error: {error}")
            return False
        return True

    def add_collection(self, edges: Sequence[Tuple[int, int]]):
        """Add collection by in put edges."""
        graph = Graph(edges)
        if not self.__test_graph(graph):
            return
        self.collections.append(graph)
        self.unsaveFunc()
        self.__reload_atlas()

    def add_collections(self, collections: Sequence[Sequence[Tuple[int, int]]]):
        """Add collections."""
        for c in collections:
            self.add_collection(c)

    @Slot(name='on_add_by_edges_button_clicked')
    def __add_from_edges(self):
        """Add collection by input string."""
        edges_str = ""
        while not edges_str:
            edges_str, ok = QInputDialog.getText(
                self,
                "Add by edges",
                "Please enter a connection expression:\n"
                "Example: [(0, 1), (1, 2), (2, 3), (3, 0)]"
            )
            if not ok:
                return
        try:
            edges = eval(edges_str)
            if any(len(edge) != 2 for edge in edges):
                raise ValueError("wrong format")
        except (SyntaxError, ValueError) as error:
            QMessageBox.warning(self, str(error), f"Error: {error}")
            return
        else:
            self.add_collection(edges)

    @Slot(name='on_add_by_files_button_clicked')
    def __add_from_files(self):
        """Append atlas by text files."""
        file_names = self.input_from(
            "Edges data",
            ["Text File (*.txt)"],
            multiple=True
        )
        if not file_names:
            return

        read_data = []
        for file_name in file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    read_data.append(line)

        collections = []
        for edges in read_data:
            try:
                collections.append(Graph(eval(edges)))
            except (SyntaxError, TypeError):
                QMessageBox.warning(
                    self,
                    "Wrong format",
                    "Please check the edges text format."
                )
                return
        if not collections:
            return
        self.collections += collections
        self.__reload_atlas()

    @Slot(name='on_capture_graph_clicked')
    def __save_graph(self):
        """Save the current graph."""
        if self.selection_window.count() != 1:
            return

        file_name = self.output_to("Atlas image", qt_image_format)
        if not file_name:
            return

        pixmap: QPixmap = self.selection_window.item(0).icon().pixmap(self.selection_window.iconSize())
        pixmap.save(file_name)
        self.save_reply_box("Graph", file_name)

    @Slot(name='on_save_atlas_clicked')
    def __save_atlas(self):
        """Save function as same as type synthesis widget."""
        count = self.collection_list.count()
        if not count:
            return

        lateral, ok = QInputDialog.getInt(
            self,
            "Atlas",
            "The number of lateral:",
            5,
            1
        )
        if not ok:
            return

        file_name = self.output_to("Atlas image", qt_image_format)
        if not file_name:
            return

        icon_size = self.collection_list.iconSize()
        width = icon_size.width()
        image_main = QImage(QSize(
            lateral * width if count > lateral else count * width,
            ((count // lateral) + bool(count % lateral)) * width
        ), self.collection_list.item(0).icon().pixmap(icon_size).toImage().format())
        image_main.fill(Qt.transparent)
        painter = QPainter(image_main)
        for row in range(count):
            image = self.collection_list.item(row).icon().pixmap(icon_size).toImage()
            painter.drawImage(QPointF(
                row % lateral * width,
                row // lateral * width
            ), image)
        painter.end()
        pixmap = QPixmap()
        pixmap.convertFromImage(image_main)
        pixmap.save(file_name)
        self.save_reply_box("Atlas", file_name)

    @Slot(name='on_save_edges_clicked')
    def __save_edges(self):
        """Save function as same as type synthesis widget."""
        count = self.collection_list.count()
        if not count:
            return
        file_name = self.output_to("Atlas edges expression", ["Text file (*.txt)"])
        if not file_name:
            return
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(str(G.edges) for G in self.collections))
        self.save_reply_box("edges expression", file_name)

    @Slot(int, name='on_collection_list_currentRowChanged')
    def __set_selection(self, row: int):
        """Show the data of collection.

        Save the layout position to keep the graphs
        will be in same appearance.
        """
        item: Optional[QListWidgetItem] = self.collection_list.item(row)
        has_item = item is not None
        self.delete_button.setEnabled(has_item)
        self.configure_button.setEnabled(has_item)
        self.selection_window.clear()
        if item is None:
            return

        # Preview item.
        link_is_node = self.graph_link_as_node.isChecked()
        item_preview = QListWidgetItem(item.text())
        row = self.collection_list.row(item)
        g = self.collections[row]
        self.ground_engine = self.collections_layouts[row]
        item_preview.setIcon(to_graph(
            g,
            self.selection_window.iconSize().width(),
            self.ground_engine,
            link_is_node,
            self.graph_show_label.isChecked(),
            self.is_monochrome()
        ))
        self.selection_window.addItem(item_preview)

        # Set attributes.
        self.edges_text.setText(str(list(g.edges)))
        self.nl_label.setText(str(len(g.nodes)))
        self.nj_label.setText(str(len(g.edges)))
        self.dof_label.setText(str(g.dof()))
        self.is_degenerate_label.setText(str(g.is_degenerate()))
        self.link_assortments_label.setText(str(l_a(g)))
        self.contracted_link_assortments_label.setText(str(c_l_a(g)))

        # "Link as node" layout cannot do these action.
        self.configure_button.setEnabled(not link_is_node)
        self.grounded_merge.setEnabled(not link_is_node)

        # Automatic ground.
        self.__grounded()

    def __clear_selection(self):
        """Clear the selection preview data."""
        self.grounded_list.clear()
        self.selection_window.clear()
        self.edges_text.clear()
        self.nl_label.setText('0')
        self.nj_label.setText('0')
        self.dof_label.setText('0')
        self.is_degenerate_label.setText("N/A")
        self.link_assortments_label.setText("N/A")
        self.contracted_link_assortments_label.setText("N/A")

    @Slot(name='on_expr_copy_clicked')
    def __copy_expr(self):
        """Copy the expression."""
        string = self.edges_text.text()
        if string:
            QApplication.clipboard().setText(string)
            self.edges_text.selectAll()

    @Slot(name='on_delete_button_clicked')
    def __delete_collection(self):
        """Delete the selected collection."""
        row = self.collection_list.currentRow()
        if not row > -1:
            return

        if QMessageBox.question(
            self,
            "Delete",
            f"Sure to remove #{row} from your collections?"
        ) != QMessageBox.Yes:
            return

        self.collection_list.takeItem(row)
        del self.collections[row]
        self.__clear_selection()
        self.unsaveFunc()

    @Slot(name='on_configure_button_clicked')
    def __configuration(self):
        """Triangular iteration."""
        self.layout_sender.emit(
            self.collections[self.collection_list.currentRow()],
            self.ground_engine.copy()
        )

    def __grounded(self):
        """Grounded combinations."""
        current_item = self.collection_list.currentItem()
        self.collections_grounded.clear()
        self.grounded_list.clear()
        g = self.collections[self.collection_list.row(current_item)]
        item = QListWidgetItem("Released")
        icon = to_graph(
            g,
            self.grounded_list.iconSize().width(),
            self.ground_engine,
            self.graph_link_as_node.isChecked(),
            self.graph_show_label.isChecked(),
            self.is_monochrome()
        )
        item.setIcon(icon)
        self.collections_grounded.append(g)
        self.grounded_list.addItem(item)

        for node, graph_ in labeled_enumerate(g):
            item = QListWidgetItem(f"link_{node}")
            icon = to_graph(
                g,
                self.grounded_list.iconSize().width(),
                self.ground_engine,
                self.graph_link_as_node.isChecked(),
                self.graph_show_label.isChecked(),
                self.is_monochrome(),
                except_node=node
            )
            item.setIcon(icon)
            self.collections_grounded.append(graph_)
            self.grounded_list.addItem(item)

    @Slot(name='on_grounded_merge_clicked')
    def __grounded_merge(self):
        """Merge the grounded result."""
        item = self.grounded_list.currentItem()
        if not item:
            return

        graph = self.collections_grounded[0]
        text = item.text()
        if text == "Released":
            ground_link = None
        else:
            ground_link = int(text.split("_")[1])
        if QMessageBox.question(
            self,
            "Message",
            f"Merge \"{text}\" chain to your canvas?"
        ) == QMessageBox.Yes:
            self.addPointsByGraph(
                graph,
                self.ground_engine,
                ground_link
            )
