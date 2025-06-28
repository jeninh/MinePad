import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros, Press, Release

keyboard = KMKKeyboard()

#3x3
keyboard.matrix = MatrixScanner(
    cols=[board.A0, board.A1, board.A2],   # col0, col1, col2
    rows=[board.A3, board.GP6, board.GP7], # row0, row1, row2
    diode_orientation=MatrixScanner.DIODE_COL2ROW
)

# encoder enablele
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# macros!
macros = Macros()
keyboard.modules.append(macros)

# rotary encoder pins
encoder.pins = ((board.GP3, board.GP4, board.GP2),)

# rotary scroll
encoder.map = [
    ((KC.MS_WH_DOWN, KC.MS_WH_UP),)  # clockwise = down, counterclockwise = up
]

keyboard.keymap = [
    [
        KC.TAB,    KC.W,      KC.E,
        KC.A,      KC.S,      KC.D,
        KC.F,      KC.SPACE,  KC.Q,
        KC.MACRO(Press(KC.LCTRL), Release(KC.LCTRL)),  # Encoder button press (4th "key")
    ]
]
