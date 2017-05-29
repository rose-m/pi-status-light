import argparse
from time import sleep

from data_collector import DataCollector
from hat_handler import HatHandler
from rating_light import RatingLightInfo
from utils import import_sense_hat

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show rating light information from remote server')
    parser.add_argument('--emulate', action='store_true', help='Use sense_emu instead of the real thing')
    args = parser.parse_args()

    import_sense_hat(force_emu=args.emulate)

    hat = HatHandler()
    hat.do_check()

    light = RatingLightInfo(name='Test', value=RatingLightInfo.RATING_LIGHT_RED)
    collector = DataCollector('http://www.google.de/aklsdkl')

    collector.start()

    while True:
        hat.show_rating_light(light)
        sleep(10)
        print('.', end='', flush=True)
        break
