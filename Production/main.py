import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()


keyboard.row_pins = (board.GP0,)
keyboard.col_pins = (board.GP1, board.GP2, board.GP3)

keyboard.keymap = [
    [KC.A, KC.B, KC.C], 
]

if __name__ == "__main__":
    keyboard.go()