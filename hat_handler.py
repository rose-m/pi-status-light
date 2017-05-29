import atexit
from time import sleep

from rating_light import RatingLightInfo
from utils import import_sense_hat

green_inactive = (0, 150, 0)
green_active = (0, 255, 0)
yellow_inactive = (150, 150, 0)
yellow_active = (255, 255, 0)
red_inactive = (150, 0, 0)
red_active = (255, 0, 0)


class HatHandler:
    def __init__(self):
        SenseHat = import_sense_hat()
        self._sense = SenseHat()
        atexit.register(self.clear)

    def do_check(self):
        self._sense.clear((0, 255, 0))
        sleep(1)
        self.clear()

    def clear(self):
        self._sense.clear()

    def show_rating_light(self, rating, pause_time=2.0):
        """
        Shows the given rating light by first displaying its name and then the lights.

        :param rating: Rating to show
        :type rating: RatingLightInfo
        :param pause_time: Time to show lights
        :type pause_time: int
        :return:
        """
        r = red_inactive
        y = yellow_inactive
        g = green_inactive
        if rating.value == RatingLightInfo.RATING_LIGHT_GREEN:
            g = green_active
        elif rating.value == RatingLightInfo.RATING_LIGHT_YELLOW:
            y = yellow_active
        elif rating.value == RatingLightInfo.RATING_LIGHT_RED:
            r = red_active

        self._sense.show_message(
            rating.name,
            scroll_speed=0.1
        )

        o = (0, 0, 0)
        self._sense.set_pixels([
            o, o, o, r, r, o, o, o,
            o, o, o, r, r, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, y, y, o, o, o,
            o, o, o, y, y, o, o, o,
            o, o, o, o, o, o, o, o,
            o, o, o, g, g, o, o, o,
            o, o, o, g, g, o, o, o
        ])

        sleep(pause_time)
        self.clear()
