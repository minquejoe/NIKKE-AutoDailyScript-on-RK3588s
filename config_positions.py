# 包含<识别出的场景>对应的<需要点击的位置>
# 相同的<识别出的场景>在不同的文件里对应不同<需要点击的位置>

login_annoncement = {'x1': 88, 'y1': 957, 'x2': 640, 'y2': 280}
login_region = {'x1': 350, 'y1': 560, 'x2': 360, 'y2': 930}
login_wait = {'x': 640, 'y': 280}
item_get = {'x': 640, 'y': 280}
menu = {
    'to_menu.py': {'x': 300, 'y': 635},       # 菜单处与角色互动
    'to_talk.py': {'x': 105, 'y': 1180},
    'to_arena_rookie.py': {'x': 570, 'y': 870},
    'to_arena_special.py': {'x': 570, 'y': 870},
}
menu_quit = menu

character = {'x': 400, 'y': 150}
character_talk_select = {'x': 350, 'y': 440}
character_talk_entry = {'x1': 690, 'y1': 560, 'x2': 505,
                        'y2': 1055, 'x3': 500, 'y3': 800, 'x': 500, 'y': 920}
character_talk_ongoing = {'x': 500, 'y': 920}
character_talk_reaction = {'x': 570, 'y': 960}

ark = {
    'to_arena_rookie.py': {'x1': 530, 'y1': 820, 'x2': 180, 'y2': 680, 'x3': 600, 'y3': 1120, 'x4': 490, 'y4': 1060, },
    'to_arena_special.py': {'x1': 530, 'y1': 820, 'x2': 520, 'y2': 680, 'x3': 600, 'y3': 1120, 'x4': 490, 'y4': 1060, }
}

login_manual = {'x1': 360, 'y1': 540, 'x2': 360, 'y2': 630, 'x3': 360, 'y3': 750, 'comfirm_x': 613, 'comfirm_y': 678, }

login_error = {'x': 360, 'y': 830,}

# login_error = {'x':1200, 'y':700}
# login_quit = {'x':1175, 'y':680}
# waiting = {'x':1200, 'y':700}

# wilders_fullview = {'x':1040, 'y':295}
# wilders_harvest = {'x1':1740, 'y1':330, 'x2':1740, 'y2':630}

# battle_story = {'x':870, 'y':970}
# battle_resource_01 = {
#         'to_mind.py':{'x':550, 'y':525},
#         'to_gold.py':{'x':1320, 'y':525},       # 识别不出 battle_resource_02 ，此处用 01 代替
#         'to_dust.py':{'x':490, 'y':525},       # 识别不出 battle_resource_02 ，此处用 01 代替
#         }
# battle_resource_mind = {'x1':640, 'y1':900, 'x2':1600, 'y2':920}        # 识别不出意识、灰尘进入界面
# battle_entry = battle_resource_mind     # 会把选择界面识别为进入界面
# battle_confirm = {'x':1600, 'y':990}
# battle_win = {'x':210, 'y':70}
# levelup = {'x':210, 'y':70}

# battle_resource_02 = battle_resource_01
# battle_resource_gold = battle_resource_mind

# battle_resource_dust = battle_resource_mind

# mailbox = {'x':300, 'y':930}

# task_daily = {'x1':1760, 'y1':240, 'x2':1660, 'y2':100}
# task_weekly = task_daily

# juke_box_calim = {'x1':1800, 'y1':1000, 'x2':1400, 'y2':60}
# juke_box_point = juke_box_calim.copy()
# juke_box_point.update({'x3':1400, 'y3':130})
# juke_box_calim_finish = {'x':210, 'y':70}
