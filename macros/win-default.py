# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Win Default', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 2nd row ----------
        (0x120026, 'Scrnsht', [Keycode.PRINT_SCREEN]),
        (0x120026, 'Close', [Keycode.ALT, Keycode.F4]),
        (0x120026, 'Desktop', [Keycode.WINDOWS, 'D']),
        # 3rd row ----------
        (0x004000, 'Mute', [ConsumerControlCode.MUTE]),
        (0x004000, 'Vol Down', [ConsumerControlCode.VOLUME_DECREMENT]),
        (0x004000, 'Vol Up', [ConsumerControlCode.VOLUME_INCREMENT]),
        # 4th row ----------
        (0x120026, 'Prev', [ConsumerControlCode.SCAN_PREVIOUS_TRACK ]),
        (0x120026, 'Pause', [ConsumerControlCode.PLAY_PAUSE]),
        (0x120026, 'Next', [ConsumerControlCode.SCAN_NEXT_TRACK]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, Keycode.TAB])
    ]
}
