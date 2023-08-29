from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Macro Keys', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00261a, 'F20', [Keycode.F20]),
        (0x00261a, 'F21', [Keycode.F21]),
        (0x00261a, 'F22', [Keycode.F22]),
        # 2nd row ----------
        (0x002622, 'F17', [Keycode.F17]),
        (0x002622, 'F18', [Keycode.F18]),
        (0x002622, 'F19', [Keycode.F19]),
        # 3rd row ----------
        (0x002625, 'F14', [Keycode.F14]),
        (0x002625, 'F15', [Keycode.F15]),
        (0x002625, 'F16', [Keycode.F16]),
        # 4th row ----------
        (0x002026, 'F11', [Keycode.F11]),
        (0x002026, 'F12', [Keycode.F12]),
        (0x002026, 'F13', [Keycode.F13]),
        # Encoder button ---
        (0x000000, '', [Keycode.F23])
    ]
}
