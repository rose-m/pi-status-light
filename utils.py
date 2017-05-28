_senseHat = None;


def import_sense_hat():
    global _senseHat;
    if _senseHat is not None:
        return _senseHat

    try:
        from sense_hat import SenseHat
        _senseHat = SenseHat;
        print('-> Using sense_hat')
    except ImportError:
        try:
            from sense_emu import SenseHat
            _senseHat = SenseHat;
            print('-> Using sense_emu')
        except ImportError:
            raise ImportError('Missing both sense_hat and sense_emu!')

    return _senseHat
