class RatingLightInfo:
    RATING_LIGHT_UNKNOWN = None
    RATING_LIGHT_RED = 'RED'
    RATING_LIGHT_YELLOW = 'YELLOW'
    RATING_LIGHT_GREEN = 'GREEN'

    def __init__(self, name, value):
        self.name = name
        if (value == RatingLightInfo.RATING_LIGHT_GREEN
            or value == RatingLightInfo.RATING_LIGHT_YELLOW
            or value == RatingLightInfo.RATING_LIGHT_RED):
            self.value = value
        else:
            self.value = RatingLightInfo.RATING_LIGHT_UNKNOWN
