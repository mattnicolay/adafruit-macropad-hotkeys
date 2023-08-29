from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Macro Keys', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x260021, 'F20', [Keycode.F20]),
        (0x260021, 'F21', [Keycode.F21]),
        (0x260021, 'F22', [Keycode.F22]),
        # 2nd row ----------
        (0x260017, 'F17', [Keycode.F17]),
        (0x260017, 'F18', [Keycode.F18]),
        (0x260017, 'F19', [Keycode.F19]),
        # 3rd row ----------
        (0x26000d, 'F14', [Keycode.F14]),
        (0x26000d, 'F15', [Keycode.F15]),
        (0x26000d, 'F16', [Keycode.F16]),
        # 4th row ----------
        (0x260008, 'F11', [Keycode.F11]),
        (0x260008, 'F12', [Keycode.F12]),
        (0x260008, 'F13', [Keycode.F13]),
        # Encoder button ---
        (0x000000, '', [Keycode.F23])
    ]
}
