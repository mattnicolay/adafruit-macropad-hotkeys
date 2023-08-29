# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Ableton Live', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x94061b, 'esc', [Keycode.ESCAPE]),
        (0x94061b, 'search', [Keycode.COMMAND, 'f']),
        (0x94061b, 'enter', [Keycode.ENTER]),
        # 2nd row ----------
        (0x52b8f2, 'track view', [Keycode.SHIFT, Keycode.TAB]),
        (0x000000, '', []),
        (0x52b8f2, 'mix view', [Keycode.TAB]),
        # 3rd row ----------
        (0x3c047d, 'auto', ['a']),
        (0x3c047d, 'draw', ['b']),
        (0x3c047d, 'hide', [Keycode.OPTION, Keycode.COMMAND, 'p']),
        # 4th row ----------
        (0x004000, 'play', [Keycode.SPACE]),
        (0x0080ff, 'stop', ['w']),
        (0x660000, 'rec', ['r']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
