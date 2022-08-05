self.shot = shot
self.beam = beam
self.wall = wall
#  fire table
class FireElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    null = db.Column(db.String, nullable=False)
    water = db.Column(db.String, nullable=False)
    air = db.Column(db.String, nullable=False)
    earth = db.Column(db.String, nullable=False)

def __init__(self, null, water, air, earth):
    self.water = water
    self.air = air
    self.earth = earth
        

class WaterElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "fire", "air", "earth")

WaterElement_schema = WaterElementSchema()
WaterElements_schema = WaterElementSchema(many=True)

class WaterElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    null = db.Column(db.String, nullable=False)
    fire = db.Column(db.String, nullable=False)
    air = db.Column(db.String, nullable=False)
    earth = db.Column(db.String, nullable=False)

def __init__(self, null, fire, air, earth):
    self.fire = fire
    self.air = air
    self.earth = earth
        

class WaterElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "fire", "air", "earth")

WaterElement_schema = WaterElementSchema()
WaterElements_schema = WaterElementSchema(many=True)

class WaterElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "fire", "air", "earth")

WaterElement_schema = WaterElementSchema()
WaterElements_schema = WaterElementSchema(many=True)

class AirElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    null = db.Column(db.String, nullable=False)
    fire = db.Column(db.String, nullable=False)
    water = db.Column(db.String, nullable=False)
    earth = db.Column(db.String, nullable=False)

def __init__(self, null, fire, water, earth):
    self.fire = fire
    self.water = water
    self.earth = earth
        

class AirElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "fire", "water", "earth")

AirElement_schema = AirElementSchema()
AirElements_schema = AirElementSchema(many=True)

class EarthElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    null = db.Column(db.String, nullable=False)
    fire = db.Column(db.String, nullable=False)
    water = db.Column(db.String, nullable=False)
    air = db.Column(db.String, nullable=False)

def __init__(self, null, fire, water, air):
    self.fire = fire
    self.water = water
    self.air = air
        

class EarthElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "fire", "water", "air")

EarthElement_schema = EarthElementSchema()
EarthElements_schema = EarthElementSchema(many=True)

class FormElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shot = db.Column(db.String, nullable=False)
    beam = db.Column(db.String, nullable=False)
    wall = db.Column(db.String, nullable=False)

def __init__(self, null, shot, beam, wall):
    self.shot = shot
    self.beam = beam
    self.wall = wall
        

class EarthElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "null", "shot", "beam", "wall")

FormElement_schema = FormElementSchema()
FormElements_schema = FormElementSchema(many=True)