import badge, appglue, ugfx, easydraw, time
import wifi
import urequests as requests
from random import randint, choice


leds = [0] * 24
idle = [5,6,7,8]

def send_random_colors():
    for i in range(6):
        leds[i*4 ] = randint(0, 10) #G
        leds[i*4 + 1] = randint(0, 10) #R
        leds[i*4 + 2] = randint(0, 10) #B
        leds[i*4 + 3] = 0 #W

    badge.leds_send_data(bytes(leds), len(leds))

def clear():
    ugfx.set_lut(ugfx.LUT_FULL)
    ugfx.clear(ugfx.BLACK)
    ugfx.flush()
    ugfx.clear(ugfx.WHITE)
    ugfx.flush()

def loop():

    while True:
        if badge.eink_busy():
            send_random_colors()
        else:
            ugfx.display_image(0,0, '/lib/dancin_disco_dave/trimmed_image_{}.png'.format(choice(idle)))
            ugfx.flush()

        #slows everything down and also allows processing input
        time.sleep(0.1)

def app_main():
    ugfx.init()

    clear()
    ugfx.set_lut(ugfx.LUT_FASTEST)

    badge.vibrator_init()

    ugfx.input_attach(ugfx.BTN_A, lambda pressed: badge.vibrator_activate(0xd))
    ugfx.input_attach(ugfx.BTN_START, lambda pressed: appglue.home())

    loop()


app_main()
