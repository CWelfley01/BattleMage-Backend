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
    Combo = db.Column(db.String, nullable=False)
    Result = db.Column(db.String, nullable=False)
    
    
    def __init__(self, Combo, Result):
        self.Combo = Combo
        self.Result = Result
        
        
class ElementSchema(ma.Schema):
    class Meta:
        fields = ("id", "Combo","Result")

element_schema = ElementSchema()
elements_schema = ElementSchema(many=True)
        



# Form table
class Form(db.Model):
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
        

class FormSchema(ma.Schema):
    class Meta:
        fields = ("id", "element", "shot", "beam", "wall")

form_schema = FormSchema()
forms_schema = FormSchema(many=True)


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
    Combo = request.json.get("Combo")
    Result = request.json.get("Result")
    
    
    

    record = Element(Combo, Result)
    
    db.session.add(record)
    db.session.commit()

    return jsonify(element_schema.dump(record))




@app.route("/add-Form", methods=["POST"])
def add_FormElement():
    element = request.json.get("element")
    shot = request.json.get("shot")
    beam = request.json.get("beam")
    wall = request.json.get("wall")
    
    

    record = Form(element, shot, beam, wall)
    
    db.session.add(record)
    db.session.commit()

    return jsonify(Form_schema.dump(record))


@app.route("/Element")
def get_all_elements():
    all_elements = Element.query.all()
    return jsonify(elements_schema.dump(all_elements))

@app.route("/spells", methods=["GET"])
def get_all_spells():
    all_spells = Spells.query.all()
    return jsonify(spells_schema.dump(all_spells))



@app.route("/Form", methods=["GET"])
def get_all_form():
    all_form = Form.query.all()
    return jsonify(forms_schema.dump(all_form))



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
        Combo = request.json['Combo']
        Result = request.json['Result']
        
       

        element.Combo = Combo
        element.Result = Result
        

        db.session.commit()
        return element_schema.jsonify(element)
    elif request.method == "GET":
        return element_schema.jsonify(element)
    
    
@app.route("/Form/<id>", methods=["DELETE","GET","PUT"])
def form_id(id):
    form = Form.query.get(id)
    if request.method == "DELETE":
        db.session.delete(form)
        db.session.commit()
    
        return form_schema.jsonify(form)
    elif request.method == "PUT":
        element = request.json.get("element")
        shot = request.json.get("shot")
        beam = request.json.get("beam")
        wall = request.json.get("wall")
        
       

        form.element = element
        form.shot = shot
        form.beam = beam
        form.wall = wall
        

        db.session.commit()
        return form_schema.jsonify(form)
    elif request.method == "GET":
        return form_schema.jsonify(form)
    

    




if __name__ == "__main__":
    app.run(debug=True)