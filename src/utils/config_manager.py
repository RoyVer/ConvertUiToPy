# src/utils/config_manager.py
import json
import os


class ConfigManager:
    def __init__(self, config_file: str, error_handler):
        self.config_file = config_file
        self.error_handler = error_handler
        self.config = self.load_config()

    def load_config(self) -> dict:
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)

            # Update log directory if specified in config
            if 'log_directory' in config:
                self.error_handler.update_log_directory(config['log_directory'])

            return config
        except FileNotFoundError:
            self.error_handler.log_error(f"Config file not found: {self.config_file}")
            return {}
        except json.JSONDecodeError:
            self.error_handler.log_error(f"Error decoding JSON from config file: {self.config_file}")
            return {}
        except Exception as e:
            self.error_handler.log_error(f"Unexpected error loading config: {str(e)}")
            return {}

    def get(self, key: str, default: str = None) -> str:
        return self.config.get(key, default)

    def get_log_directory(self) -> str:
        return self.get('log_directory', 'logs')

    def get_icon_path(self) -> str:
        return self.get('icon_path', 'resources/images/Icon.ico')

    def get_window_title(self) -> str:
        return self.get('window_title', 'ConvertUiToPy')