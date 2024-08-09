# src/main.py
import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from PyQt5.QtWidgets import QApplication
from src.gui.main_window_helper import MainWindowHelper
from src.utils.config_manager import ConfigManager
from src.utils.file_handler import FileHandler
from src.utils.error_handler import ErrorHandler

def main():
    app = QApplication(sys.argv)

    # Create ErrorHandler first with default log directory
    error_handler = ErrorHandler()

    # Create ConfigManager and pass the ErrorHandler
    config_manager = ConfigManager(os.path.join(project_root, 'config.json'), error_handler)

    # Create FileHandler
    file_handler = FileHandler(error_handler)

    # Create MainWindowHelper
    window = MainWindowHelper(config_manager, file_handler, error_handler)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()