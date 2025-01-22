import os
from to_task import to_task
import config_positions
from utils import game_one_tap, game_go_back_then_double_tap, game_enter_simulation

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_one_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'ark': {'func': game_one_tap, 'params': config_positions.ark[os.path.basename(__file__)]},
    'simulation_entry': {'func': game_enter_simulation, 'params': config_positions.simulation_entry},
}

class_order = ["menu", "ark", "simulation_entry"]
finish_class = ["simulation_entry"]

print("*="*20)
print(
    f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
