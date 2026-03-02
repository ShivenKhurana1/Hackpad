import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, SSD1306
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()


keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D7, board.D8, board.D9, False),)


display = Display(
    display_driver=SSD1306(i2c=board.I2C(), device_address=0x3C),
    width=128,
    height=32,
)
keyboard.extensions.append(display)


rgb = RGB(pixel_pin=board.D10, num_pixels=6)
keyboard.extensions.append(rgb)


keyboard.keymap = [
    [
        KC.COPY,  KC.PASTE, KC.MUTE,
        KC.F13,   KC.F14,   KC.F15,
    ]
]


encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MEDIA_PLAY_PAUSE),)
]

if __name__ == '__main__':
    keyboard.go()