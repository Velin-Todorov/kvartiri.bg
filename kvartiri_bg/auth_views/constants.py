NO_CHOICES = None, ''

STUDIO: tuple = 'STUDIO', 'Studio'
APPARTMENT: tuple = 'APPARTMENT', 'Appartment'
ROOM: tuple = 'SINGLE_ROOM', 'Single Room'

LOW: tuple = '0 Lv. - 500 Lv.', '0 Lv. - 500 Lv.'
MID: tuple = '500 Lv. - 1000 Lv.', '500 Lv. - 1000 Lv.'
HIGH: tuple = '1000+ Lv.', '1000+ Lv.'

PRIVATE_OWNER: tuple = 'PRIVATE_OWNER', 'Private Owner'
COMPANY: tuple = 'COMPANY', 'Company'

TENANT: tuple = 'TENANT', 'Tenant'
LANDLORD:tuple = 'LANDLORD', 'Landlord'

CHOICES = [
    NO_CHOICES,
    STUDIO,
    APPARTMENT,
    ROOM
]


PRICE_RANGE = [
    NO_CHOICES,
    LOW,
    MID, 
    HIGH
]

TYPE = [
    PRIVATE_OWNER,
    COMPANY
]

PROFILE_TYPE = [
    TENANT,
    LANDLORD
]