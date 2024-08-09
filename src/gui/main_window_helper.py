# src/gui/main_window_helper.py
import os
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from .gui_main_window import Ui_MainWindow
from ..utils.file_handler import FileHandler
from ..utils.error_handler import ErrorHandler
from ..utils.config_manager import ConfigManager


class MainWindowHelper(QMainWindow):
    def __init__(self, config_manager: ConfigManager, file_handler: FileHandler, error_handler: ErrorHandler):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.config_manager = config_manager
        self.file_handler = file_handler
        self.error_handler = error_handler

        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        self.setWindowTitle(self.config_manager.get_window_title())
        self.setFixedSize(465, 285)
        self.center_on_screen()

        # Load icon using absolute path
        icon_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', self.config_manager.get_icon_path()))
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            self.error_handler.log_error(f"Icon file not found: {icon_path}")

    def center_on_screen(self):
        screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
        center_point = QDesktopWidget().screenGeometry(screen).center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def connect_signals(self):
        self.ui.btnSelectSourceFile.clicked.connect(self.select_ui_file)
        self.ui.btnSelectDestination.clicked.connect(self.select_py_file)
        self.ui.btnExecute.clicked.connect(self.convert_ui_to_py)

    def select_ui_file(self):
        try:
            ui_file, _ = QFileDialog.getOpenFileName(self, "Select UI File", "", "UI Files (*.ui)")
            if ui_file:
                self.ui.txtDownloadLink.setPlainText(ui_file)
        except Exception as e:
            self.error_handler.log_error("Error selecting UI file", str(e))
            QMessageBox.critical(self, "Error", f"Failed to select UI file: {str(e)}")

    def select_py_file(self):
        try:
            py_file, _ = QFileDialog.getSaveFileName(self, "Save Python File", "", "Python Files (*.py)")
            if py_file:
                self.ui.txtFilePath.setPlainText(py_file)
        except Exception as e:
            self.error_handler.log_error("Error selecting Python file", str(e))
            QMessageBox.critical(self, "Error", f"Failed to select Python file: {str(e)}")

    def convert_ui_to_py(self):
        ui_file = self.ui.txtDownloadLink.toPlainText()
        py_file = self.ui.txtFilePath.toPlainText()

        if not ui_file or not py_file:
            QMessageBox.warning(self, "Error", "Both UI and Python file paths must be selected.")
            return

        try:
            self.file_handler.convert_ui_to_py(ui_file, py_file)
            QMessageBox.information(self, "Success", "Conversion completed successfully!")
            self.file_handler.open_output_directory(py_file)
        except Exception as e:
            self.error_handler.log_error("Conversion failed", str(e))
            QMessageBox.critical(self, "Error", f"An error occurred during conversion: {str(e)}")