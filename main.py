import argparse
from time import sleep

from cplace_auth import CplaceAuthenticator
from data_collector import DataCollector
from hat_handler import HatHandler
from rating_light import RatingLightInfo
from utils import import_sense_hat

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Show rating light information from remote server')
    parser.add_argument('--emulate', action='store_true', help='Use sense_emu instead of the real thing')
    parser.add_argument('--cycle', type=int, default=5, help='Pause in seconds between cycles')
    args = parser.parse_args()

    import_sense_hat(force_emu=args.emulate)

    hat = HatHandler()
    hat.do_check()

    light = RatingLightInfo(name='Test', value=RatingLightInfo.RATING_LIGHT_RED)

    auth = CplaceAuthenticator('g9denm1u0ur193kfad0kfwzyg')
    collector = DataCollector('http://localhost:8083/intern/tricia/cf/cplace/fun/piStatus/handler/ratingLightStatus',
                              authenticator=auth)

    collector.start()
    sleep(2)

    while True:
        for rating in collector.get_data():
            hat.show_rating_light(rating)

        sleep(args.cycle)
        print('.', end='', flush=True)
