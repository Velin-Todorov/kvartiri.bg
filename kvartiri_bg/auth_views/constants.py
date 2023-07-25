NO_CHOICES = None, 'Other'

STUDIO: tuple = 'STUDIO', 'Studio'
APPARTMENT: tuple = 'APPARTMENT', 'Appartment'
ROOM: tuple = 'SINGLE_ROOM', 'Single Room'

CHOICES = [
    NO_CHOICES,
    STUDIO,
    APPARTMENT,
    ROOM
]
LOW: tuple = '0 Lv. - 500 Lv.', '0 Lv. - 500 Lv.'
MID: tuple = '500 Lv. - 1000 Lv.', '500 Lv. - 1000 Lv.'
HIGH: tuple = '1000+ Lv.', '1000+ Lv.'


PRICE_RANGE = [
    NO_CHOICES,
    LOW,
    MID, 
    HIGH
]