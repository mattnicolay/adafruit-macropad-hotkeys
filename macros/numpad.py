# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0d2600, '7', [Keycode.KEYPAD_SEVEN]),
        (0x0d2600, '8', [Keycode.KEYPAD_EIGHT]),
        (0x0d2600, '9', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x0d2600, '4', [Keycode.KEYPAD_FOUR]),
        (0x0d2600, '5', [Keycode.KEYPAD_FIVE]),
        (0x0d2600, '6', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x0d2600, '1', [Keycode.KEYPAD_ONE]),
        (0x0d2600, '2', [Keycode.KEYPAD_TWO]),
        (0x0d2600, '3', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x101010, '-', [Keycode.KEYPAD_MINUS]),
        (0x0d2600, '0', [Keycode.KEYPAD_ZERO]),
        (0x101010, '+', [Keycode.KEYPAD_PLUS]),
        # Encoder button ---
        (0x000000, '', [Keycode.KEYPAD_ENTER])
    ]
}
