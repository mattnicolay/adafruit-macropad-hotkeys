# MACROPAD Hotkeys: Evernote web application for Mac
# Contributed by Redditor s010sdc

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Mac Default', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x260021, 'Scrnsht', [Keycode.COMMAND, Keycode.SHIFT, '3']),
        (0x260021, 'Left', [Keycode.CONTROL, Keycode.LEFT_ARROW]),
        (0x260021, 'Right', [Keycode.CONTROL, Keycode.RIGHT_ARROW]),
        # 2nd row ----------
        (0x260017, 'Emoji', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        (0x260017, 'Brt Dn', [ConsumerControlCode.BRIGHTNESS_DECREMENT]),
        (0x260017, 'Brt Up', [ConsumerControlCode.BRIGHTNESS_INCREMENT]),
        # 3rd row ----------
        (0x26000d, 'Mute', [ConsumerControlCode.MUTE]),
        (0x26000d, 'Vol Down', [ConsumerControlCode.VOLUME_DECREMENT]),
        (0x26000d, 'Vol Up', [ConsumerControlCode.VOLUME_INCREMENT]),
        # 4th row ----------
        (0x260008, 'Prev', [ConsumerControlCode.SCAN_PREVIOUS_TRACK ]),
        (0x260008, 'Pause', [ConsumerControlCode.PLAY_PAUSE]),
        (0x260008, 'Next', [ConsumerControlCode.SCAN_NEXT_TRACK]),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, Keycode.UP_ARROW]) # Close window/tab
    ]
}
