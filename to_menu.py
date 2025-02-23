import os
from to_task import to_task
import config_positions
from utils import game_double_tap, game_go_back_then_double_tap, game_tap_sleep_X2_ShortInv, game_login_manual, game_error

# Define the mapping from class name to adb command
class_to_adb = {
    'login_annoncement': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.login_annoncement},
    'login_region': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.login_region},
    'login': {'func': game_double_tap, 'params': config_positions.login_wait},
    'login_manual': {'func': game_login_manual, 'params': config_positions.login_manual},
    'login_error': {'func': game_error, 'params': config_positions.login_error},

    'item_get': {'func': game_double_tap, 'params': config_positions.item_get},
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},

    'simulation_end': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.simulation_end},
}

class_order = ["login", "menu_annoncement", "menu"]
finish_class = ["menu", "menu_quit"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
