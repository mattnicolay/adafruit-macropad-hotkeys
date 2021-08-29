# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0d2600, '7', ['7']),
        (0x0d2600, '8', ['8']),
        (0x0d2600, '9', ['9']),
        # 2nd row ----------
        (0x0d2600, '4', ['4']),
        (0x0d2600, '5', ['5']),
        (0x0d2600, '6', ['6']),
        # 3rd row ----------
        (0x0d2600, '1', ['1']),
        (0x0d2600, '2', ['2']),
        (0x0d2600, '3', ['3']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x0d2600, '0', ['0']),
        (0x101010, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
