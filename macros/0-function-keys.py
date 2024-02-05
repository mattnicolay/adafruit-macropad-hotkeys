from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Fn Keys', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x41007d, 'F10', [Keycode.F10]),
        (0x41007d, 'F11', [Keycode.F11]),
        (0x41007d, 'F12', [Keycode.F12]),
        # 2nd row ----------
        (0x5300a1, 'F7', [Keycode.F7]),
        (0x5300a1, 'F8', [Keycode.F8]),
        (0x5300a1, 'F9', [Keycode.F9]),
        # 3rd row ----------
        (0x6800c9, 'F4', [Keycode.F4]),
        (0x6800c9, 'F5', [Keycode.F5]),
        (0x6800c9, 'F6', [Keycode.F6]),
        # 4th row ----------
        (0x7b00ed, 'F1', [Keycode.F1]),
        (0x7b00ed, 'F2', [Keycode.F2]),
        (0x7b00ed, 'F3', [Keycode.F3]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
