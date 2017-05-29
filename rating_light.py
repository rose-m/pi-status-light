class RatingLightInfo:
    RATING_LIGHT_UNKNOWN = None
    RATING_LIGHT_RED = 'red'
    RATING_LIGHT_YELLOW = 'yellow'
    RATING_LIGHT_GREEN = 'green'

    def __init__(self, name, value):
        self.name = name
        if (value == RatingLightInfo.RATING_LIGHT_GREEN
            or value == RatingLightInfo.RATING_LIGHT_YELLOW
            or value == RatingLightInfo.RATING_LIGHT_RED):
            self.value = value
        else:
            self.value = RatingLightInfo.RATING_LIGHT_UNKNOWN
