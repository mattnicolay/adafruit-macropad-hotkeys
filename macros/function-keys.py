from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Fn Keys', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x260021, 'F10', [Keycode.F10]),
        (0x260021, 'F11', [Keycode.F11]),
        (0x260021, 'F12', [Keycode.F12]),
        # 2nd row ----------
        (0x260017, 'F7', [Keycode.F7]),
        (0x260017, 'F8', [Keycode.F8]),
        (0x260017, 'F9', [Keycode.F9]),
        # 3rd row ----------
        (0x26000d, 'F4', [Keycode.F4]),
        (0x26000d, 'F5', [Keycode.F5]),
        (0x26000d, 'F6', [Keycode.F6]),
        # 4th row ----------
        (0x260008, 'F1', [Keycode.F1]),
        (0x260008, 'F2', [Keycode.F2]),
        (0x260008, 'F3', [Keycode.F3]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
