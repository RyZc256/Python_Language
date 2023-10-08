from datetime import datetime
import time


def main(hour=0,minute=0):
    now = datetime.now().strftime('%H-%M').split('-')
    hour = "%02d" % hour
    minute = "%02d" % minute
    if now[0] == hour and now[1] == minute:
        print(f"{datetime.now()} 要打卡了 ")
    time.sleep(60)


if __name__ == '__main__':
    while True:
        main(9,15)