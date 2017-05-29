_senseHat = None;


def import_sense_hat(force_emu=False):
    global _senseHat;
    if _senseHat is not None:
        return _senseHat

    def import_emu():
        global _senseHat
        try:
            from sense_emu import SenseHat
            _senseHat = SenseHat;
            print('-> Using sense_emu')
        except ImportError as e:
            if force_emu:
                raise e
            raise ImportError('Missing both sense_hat and sense_emu!')

    if not force_emu:
        try:
            from sense_hat import SenseHat
            _senseHat = SenseHat;
            print('-> Using sense_hat')
        except ImportError:
            import_emu()
    else:
        import_emu()

    return _senseHat
