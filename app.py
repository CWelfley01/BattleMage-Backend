from pydoc import describe
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)



# SPELL TABLE
class Spells(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spellname = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    attackmod = db.Column(db.Integer, nullable=False)
    defencemod = db.Column(db.Integer, nullable=False)
    specialeffect = db.Column(db.String, nullable=False)
    

    def __init__(self, spellname, description, attackmod, defencemod, specialeffect ):
        self.spellname = spellname
        self.description = description
        self.attackmod = attackmod
        self.defencemod = defencemod
        self.specialeffect = specialeffect
        

class SpellSchema(ma.Schema):
    class Meta:
        fields = ("id", "spellname", "description", "attackmod", "defencemod", "specialeffect")

spell_schema = SpellSchema()
spells_schema = SpellSchema(many=True)

# Element Table
class Element(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Main = db.Column(db.String, nullable=False)
    Fire = db.Column(db.String, nullable=False)
    Water = db.Column(db.String, nullable=False)
    Air = db.Column(db.String, nullable=False)
    Earth = db.Column(db.String, nullable=False)
    
    def __init__(self, Main, Fire, Water, Air, Earth):
        self.Main = Main
        self.Fire = Fire
        self.Water = Water
        self.Air = Air
        self.Earth = Earth
        
class ElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "Main","Fire", "Water", "Air", "Earth")

element_schema = ElementSchema()
elements_schema = ElementSchema(many=True)
        



# Form table
class FormElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    element = db.Column(db.String, nullable=False)
    shot = db.Column(db.String, nullable=False)
    beam = db.Column(db.String, nullable=False)
    wall = db.Column(db.String, nullable=False)

    def __init__(self, element, shot, beam, wall):
        self.element = element
        self.shot = shot
        self.beam = beam
        self.wall = wall
        

class FormElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "element", "shot", "beam", "wall")

formElement_schema = FormElementSchema()
formElements_schema = FormElementSchema(many=True)


# ROUTES
@app.route("/add-spell", methods=["POST"])
def add_spell():
    spellname = request.json.get("spellname")
    description = request.json.get("description")
    attackmod = request.json.get("attackmod")
    defencemod = request.json.get("defencemod")
    specialeffect = request.json.get("specialeffect")
    

    record = Spells(spellname, description, attackmod, defencemod, specialeffect)
    
    db.session.add(record)
    db.session.commit()

    return jsonify(spell_schema.dump(record))

@app.route("/add-element", methods=["POST"])
def add_element():
    Main = request.json.get("Main")
    Fire = request.json.get("Fire")
    Water = request.json.get("Water")
    Air = request.json.get("Air")
    Earth = request.json.get("Earth")
    
    

    record = Element(Main, Fire, Water, Air, Earth)
    
    db.session.add(record)
    db.session.commit()

    return jsonify(element_schema.dump(record))




@app.route("/add-FormElement", methods=["POST"])
def add_FormElement():
    element = request.json.get("element")
    shot = request.json.get("shot")
    beam = request.json.get("beam")
    wall = request.json.get("wall")
    
    

    record = FormElement(element, shot, beam, wall)
    
    db.session.add(record)
    db.session.commit()

    return jsonify(FormElement_schema.dump(record))


@app.route("/Element")
def get_all_elements():
    all_elements = Element.query.order_by(Element).all()
    return jsonify(elements_schema.dump(all_elements))

@app.route("/Element/")
def get_element1(element1):
    element1 = request.args.get('http://127.0.0.1:3000/hud.js/{this.state.element1}')
    return jsonify(elements_schema.dump(element1))

# @app.route("/Element/{get_element1}/<element2>")
# def get_element2(element2):
#     element2 = request.args.get('http://127.0.0.1:3000/hud.js/{this.state.element2}')
#     return jsonify(element_schema.dump(element2))

# @app.route("/Element/<Main>/<secondary>")
# def Element(combined_element):
#     combined_element = request.args.get('http://127.0.0.1:5000/Element/{get_element1}/${get_element2}') 
#     return jsonify(element_schema(combined_element))


    
    
@app.route("/spells", methods=["GET"])
def get_all_spells():
    all_spells = Spells.query.all()
    return jsonify(spells_schema.dump(all_spells))



@app.route("/FormElement", methods=["GET"])
def get_all_FormElement():
    all_FormElement = FormElement.query.all()
    return jsonify(formelement_schema.dump(all_FormElement))



@app.route("/spell/<id>", methods=["DELETE","GET","PUT"])
def spell_id(id):
    spell = Spells.query.get(id)
    if request.method == "DELETE":
        db.session.delete(spell)
        db.session.commit()
    
        return spell_schema.jsonify(spell)
    elif request.method == "PUT":
        spellname = request.json['spellname']
        attackmod = request.json['attackmod']
        defencemod = request.json['defencemod']
        description = request.json['description']
        specialeffect = request.json['specialeffect']
       

        spell.spellname = spellname
        spell.attackmod = attackmod
        spell.defencemod = defencemod
        spell.description = description
        spell.specialeffect = specialeffect

        db.session.commit()
        return spell_schema.jsonify(spell)
    elif request.method == "GET":
        return spell_schema.jsonify(spell)
    
@app.route("/Element/<id>", methods=["DELETE","GET","PUT"])
def element_id(id):
    element = Element.query.get(id)
    if request.method == "DELETE":
        db.session.delete(element)
        db.session.commit()
    
        return element_schema.jsonify(element)
    elif request.method == "PUT":
        Main = request.json['Main']
        Fire = request.json['Fire']
        Water = request.json['Water']
        Air = request.json['Air']
        Earth = request.json['Earth']
       

        element.Main = Main
        element.Fire = Fire
        element.Water = Water
        element.Air = Air
        element.Earth = Earth

        db.session.commit()
        return element_schema.jsonify(element)
    elif request.method == "GET":
        return element_schema.jsonify(element)
    




if __name__ == "__main__":
    app.run(debug=True)