import os
from to_task import to_task
import config_positions
from utils import game_one_tap, game_go_back_then_double_tap, game_enter_simulation, game_buff_then_simulation, game_tap_sleep_X2_ShortInv

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_one_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'menu_quit': {'func': game_go_back_then_double_tap, 'params': config_positions.menu_quit[os.path.basename(__file__)]},
    'ark': {'func': game_one_tap, 'params': config_positions.ark[os.path.basename(__file__)]},
    'simulation_entry': {'func': game_enter_simulation, 'params': config_positions.simulation_entry},
    'simulation_buff': {'func': game_buff_then_simulation, 'params': config_positions.simulation_buff},
    'simulation_end': {'func': game_tap_sleep_X2_ShortInv, 'params': config_positions.simulation_end},
}

class_order = ["menu", "ark", "simulation_entry", "simulation_buff", "simulation_end"]
finish_class = ["simulation_entry", "simulation_buff", "simulation_end"]

print("*="*20)
print(
    f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
