# src/utils/file_handler.py
import os
import subprocess
from PyQt5.QtWidgets import QFileDialog
from src.utils.error_handler import ErrorHandler

class FileHandler:
    def __init__(self, error_handler: ErrorHandler):
        self.error_handler = error_handler

class FileHandler:
    def __init__(self, error_handler: ErrorHandler):
        self.error_handler = error_handler

    def select_input_file(self, parent, caption: str, file_filter: str) -> str:
        file, _ = QFileDialog.getOpenFileName(parent, caption, "", file_filter)
        return file

    def select_output_file(self, parent, caption: str, file_filter: str) -> str:
        file, _ = QFileDialog.getSaveFileName(parent, caption, "", file_filter)
        return file

    def convert_ui_to_py(self, ui_file: str, py_file: str) -> None:
        result = subprocess.run(['pyuic5', '-o', py_file, ui_file], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(result.stderr)

    def open_output_directory(self, file_path: str) -> None:
        output_dir = os.path.dirname(file_path)
        os.startfile(output_dir)