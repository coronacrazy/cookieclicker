import pyautogui as pt
import time

# not actually sure how this works
pt.FAILSAFE = True

    # time to prepare web tab for cookie clicker
time.sleep(5)

    # coordinates
cookie = 250, 500
cursor = 1700, 300
grandma = 1700, 350
farm = 1700, 400
mine = 1700, 500
factory = 1700, 550
bank = 1700, 650
temple  = 1700, 700
wizard = 1700, 750
rocketship = 1700, 850
alchemy = 1700, 900
portal = 1700, 1000

# clicking the cookie and actually moving the the buildings to buy
while True:
        for x in range(250):
                pt.moveTo(cookie)
                pt.click(cookie)

        pt.moveTo(cursor)
        pt.click(cursor)
        time.sleep(0.5)
        pt.moveTo(grandma)
        pt.click(grandma)
        time.sleep(0.5)
        pt.moveTo(farm)
        pt.click(farm)
        time.sleep(0.5)
        pt.moveTo(mine)
        pt.click(mine)
        time.sleep(0.5)
        pt.moveTo(factory)
        pt.click(factory)
        time.sleep(0.5)
        pt.moveTo(bank)
        pt.click(bank)
        time.sleep(0.5)
        pt.moveTo(temple)
        pt.click(temple)
        time.sleep(0.5)
        pt.moveTo(wizard)
        pt.click(wizard)
