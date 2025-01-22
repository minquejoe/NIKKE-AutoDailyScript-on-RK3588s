from adbutils import AdbDevice, AdbClient

import time
import smtplib
from email.mime.text import MIMEText
import subprocess
import config

from config import GAME_ACCOUNT, GAME_PASSWORD

adb = AdbClient(host=config.adb_host, port=config.adb_port)
adb.connect(config.device_serial)
d = AdbDevice(adb, config.device_serial)

# ==========================
#         游戏交互
# ==========================


def game_one_tap(x, y):
    d.shell(f'input tap {x} {y}')


def game_go_back():
    d.shell('input keyevent BACK')


def game_double_tap(x, y):
    game_one_tap(x, y)
    time.sleep(config.double_tap_interval)
    game_one_tap(x, y)


def game_go_back_then_double_tap(x, y):
    game_go_back()
    time.sleep(config.go_back_sleep_time)
    game_double_tap(x, y)


def game_tap_sleep_X2_ShortInv(x1, y1, x2, y2):
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)


def game_sleep_tap_X2_LongInv(x1, y1, x2, y2):
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x2, y2)


def game_one_tap_LongSleep(x, y):
    game_one_tap(x, y)
    time.sleep(config.long_sleep)


def game_enter_talk_and_go(x1, y1, x2, y2, x3, y3, x, y):
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x3, y3)
    time.sleep(config.sleep_tap_short_interval)
    game_tap_sleep_X10_ShortInv(x, y)


def game_tap_sleep_X10_ShortInv(x, y):
    for _ in range(10):
        game_one_tap(x, y)
        time.sleep(config.sleep_tap_short_interval)


def game_arena(x1, y1, x2, y2, x3, y3, x4, y4):
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x3, y3)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x4, y4)
    time.sleep(config.sleep_tap_long_interval*3)
    game_one_tap(x4, y4+30)
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x3, y3)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x4, y4)
    time.sleep(config.sleep_tap_long_interval*3)


def game_login_manual(x1, y1, x2, y2, x3, y3, comfirm_x, comfirm_y):
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    d.shell(f'input text {GAME_ACCOUNT}')
    game_one_tap(comfirm_x, comfirm_y)
    time.sleep(config.sleep_tap_short_interval)

    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)
    d.shell(f'input text {GAME_PASSWORD}')
    game_one_tap(comfirm_x, comfirm_y)
    time.sleep(config.sleep_tap_short_interval)

    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x3, y3)


def game_error(x, y):
    game_one_tap(x, y)
    time.sleep(config.sleep_tap_short_interval)
    game_start()


def game_enter_simulation(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)
    game_double_tap(x3, y3)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x4, y4)
    time.sleep(90)  # 直接等1分钟
    game_go_back()
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x5, y5)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x6, y6)
    time.sleep(config.sleep_tap_short_interval)

# ==========================
#       游戏启动、关闭
# ==========================


def game_start():
    d.shell(f'am start -n {config.package_name}/{config.start_activity_name}')


def game_close():
    d.shell(f'am force-stop {config.package_name}')

# ==========================
#            截图
# ==========================


def take_screenshot():
    pilimg = d.screenshot()
    pilimg.save(config.IMG_PATH)


# ==========================
#          发送邮件
# ==========================
SOURCE_MAIL_ADDR = config.SOURCE_MAIL_ADDR
SOURCE_MAIL_PASS = config.SOURCE_MAIL_PASS
TARGET_MAIL_ADDR = config.TARGET_MAIL_ADDR


def send_email(timeout_commands: list):
    # 使用QQ邮箱
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(SOURCE_MAIL_ADDR, SOURCE_MAIL_PASS)

    msg = MIMEText(
        f"The following commands exceeded the {config.task_timeout} seconds runtime limit:\n{timeout_commands}")
    msg['Subject'] = "NIKKE Timeout Alert"
    msg['From'] = SOURCE_MAIL_ADDR
    msg['To'] = TARGET_MAIL_ADDR

    server.sendmail(SOURCE_MAIL_ADDR, TARGET_MAIL_ADDR, msg.as_string())
    server.quit()


# ==========================
#     python3 文件序列执行
# ==========================
task_seq = config.task_seq
task_timeout = config.task_timeout
task_timeout_threshold = config.task_timeout_threshold


def exec_seq():
    # Execute python3 files sequentially
    timeout_task = []
    for task in task_seq:
        try:
            # Run python3 command with a timeout
            subprocess.run(task.split(), timeout=task_timeout)

        except subprocess.TimeoutExpired:
            # If timeout, add command to timeout_task list
            timeout_task.append(task)
            print(f"Timeout: {task} took longer than {task_timeout} seconds.")
            continue

        print(
            f'RUNNING NEXT FILE ... SLEEP {config.next_file_interval} SECONDS ...')
        time.sleep(config.next_file_interval)

    # If too many tasks timed out, send an email
    if timeout_task:
        send_email('\n'.join(timeout_task))

    # If all python3 commands timed out, return True
    if len(timeout_task) >= task_timeout_threshold:
        return True
    else:
        return False
