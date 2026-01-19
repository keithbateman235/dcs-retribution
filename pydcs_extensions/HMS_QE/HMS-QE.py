from dcs.unittype import ShipType

from game.modsupport import shipmod

@shipmod
class HMS_QE(unittype.ShipType):
    id = "HMS_QE"
    name = "HMS Queen Elizabeth (TPaP)"
    plane_num = 24
    helicopter_num = 16
    parking = 4
    detection_range = 300000
    threat_range = 150000
    air_weapon_dist = 150000
