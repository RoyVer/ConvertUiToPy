# ConvertUiToPy

ConvertUiToPy is a simple GUI application designed to convert `.ui` files created in Qt Designer to Python `.py` files using `pyuic5`. The application is built using PyQt5 and follows the SOLID principles for maintainable and scalable code.

## Features

- Select a `.ui` file via a file dialog.
- Specify the output `.py` file via a save file dialog.
- Convert `.ui` to `.py` with a single click.
- Dark theme for a modern look.
- Error handling with logging and notifications.

## Project Structure

```plaintext
project_root/
│
├── main.py
├── gui_handler.py
├── file_handler.py
├── error_handler.py
├── config.json
└── ui/
    └── main.ui
```

### Installation
Unpack the zip file.

Install the required dependencies using pip:
```pip install -r requirements.txt```

### Run the main.py file
```Python main.py```

Use the GUI to select a .ui file and specify the output .py file.

Click "Execute" to perform the conversion.

A notification will confirm if the conversion was successful.

#### Error Handling
Errors are logged to the Logs directory and displayed in the console.

#### License
This project is licensed under the MIT License. See the [LICENSE](LICENCE "LICENSE") file for details.
