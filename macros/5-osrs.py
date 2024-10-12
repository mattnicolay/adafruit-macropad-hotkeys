# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'OSRS', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x260017, '1', [Keycode.ONE]),
        (0x260008, '2', [Keycode.TWO]),
        (0x260008, '3', [Keycode.THREE]),
        # 2nd row ----------
        (0x26000d, 'Atk', [Keycode.F1]),
        (0x260017, 'Equp', [Keycode.F4]),
        (0x260008, 'Magic', [Keycode.F6]),
        # 3rd row ----------
        (0x260021, 'Inv', [Keycode.ESCAPE]),
        (0x26000d, 'UP', [Keycode.UP_ARROW]),
        (0x260017, 'Pray', [Keycode.F5]),
        # 4th row ----------
        (0x260021, 'LEFT', [Keycode.LEFT_ARROW]),
        (0x260021, 'DOWN', [Keycode.DOWN_ARROW]),
        (0x26000d, 'RIGHT', [Keycode.RIGHT_ARROW]),
        # Encoder button ---
        (0x000000, '', [Keycode.SPACEBAR])
    ]
}
