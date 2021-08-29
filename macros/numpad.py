# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x122600, '7', ['7']),
        (0x122600, '8', ['8']),
        (0x122600, '9', ['9']),
        # 2nd row ----------
        (0x122600, '4', ['4']),
        (0x122600, '5', ['5']),
        (0x122600, '6', ['6']),
        # 3rd row ----------
        (0x122600, '1', ['1']),
        (0x122600, '2', ['2']),
        (0x122600, '3', ['3']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x122600, '0', ['0']),
        (0x101010, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
