import os
from to_task import to_task
import config_positions
from utils import game_one_tap, game_go_back_then_double_tap, game_enter_talk_and_go, game_tap_sleep_X10_ShortInv

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_one_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'character': {'func': game_one_tap, 'params': config_positions.character},
    'character_talk_select': {'func': game_one_tap, 'params': config_positions.character_talk_select},
    'character_talk_entry': {'func': game_enter_talk_and_go, 'params': config_positions.character_talk_entry},
    'character_talk_ongoing': {'func': game_tap_sleep_X10_ShortInv, 'params': config_positions.character_talk_ongoing},
    'character_talk_reaction': {'func': game_one_tap, 'params': config_positions.character_talk_reaction},
}

class_order = ["menu", "character", "character_talk_select",
               "character_talk_entry", "character_talk_ongoing", "character_talk_reaction"]
finish_class = []

print("*="*20)
print(
    f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
