import badge, appglue, ugfx, easydraw, time
import wifi
import urequests as requests
from random import randint, choice


def disco_mode(pressed):
    if pressed:
        delay_for = randint(0, 600)
        for i in range(delay_for):
            data = []
            for i in range(6):
                G = randint(0, 255)
                R = randint(0, 255)
                B = randint(0, 255)
                W = 0
                data += [G,R,B,W]
            badge.leds_send_data(bytes(data))
            time.sleep(0.1)
        data = [0] * 6 * 4
        badge.leds_send_data(bytes(data))

def clear():
    ugfx.set_lut(ugfx.LUT_FULL)
    ugfx.clear(ugfx.BLACK)
    ugfx.flush()
    ugfx.clear(ugfx.WHITE)
    ugfx.flush()

def loop():
    print("ey holmes")


def app_main():
    ugfx.init()

    clear()
    ugfx.set_lut(ugfx.LUT_FASTEST)
    idle = [5,6,7,8]

    badge.vibrator_init()


    ugfx.input_attach(ugfx.JOY_DOWN, lambda pressed: disco_mode(pressed))
    ugfx.input_attach(ugfx.BTN_A, lambda pressed: badge.vibrator_activate(0xd))
    ugfx.input_attach(ugfx.BTN_START, lambda pressed: appglue.home())

    while True:
        badge.eink_busy_wait()

        ugfx.display_image(0,0, '/lib/dancin_disco_dave/trimmed_image_{}.png'.format(choice(idle)))
        ugfx.flush()


app_main()
