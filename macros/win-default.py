# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Win Default', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x018FC2, 'Scrnsht', [Keycode.PRINT_SCREEN]),
        (0x018FC2, 'Left', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0x018FC2, 'Right', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0x0829C2, 'Emoji', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        (0x0829C2, 'Brt Dn', [ConsumerControlCode.BRIGHTNESS_DECREMENT]),
        (0x0829C2, 'Brt Up', [ConsumerControlCode.BRIGHTNESS_INCREMENT]),
        # 3rd row ----------
        (0xAB029A, 'Mute', [ConsumerControlCode.MUTE]),
        (0xAB029A, 'Vol Down', [ConsumerControlCode.VOLUME_DECREMENT]),
        (0xAB029A, 'Vol Up', [ConsumerControlCode.VOLUME_INCREMENT]),
        # 4th row ----------
        (0x4D00AB, 'Prev', [ConsumerControlCode.SCAN_PREVIOUS_TRACK ]),
        (0x4D00AB, 'Pause', [ConsumerControlCode.PLAY_PAUSE]),
        (0x4D00AB, 'Next', [ConsumerControlCode.SCAN_NEXT_TRACK]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.UP_ARROW]) # Close window/tab
    ]
}
