from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USER's Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# CHARACTERS model
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    specie = db.Column(db.String(20), unique=False, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(20), unique=False, nullable=False)
    skin_color = db.Column(db.String(20), unique=False, nullable=False)
    eye_color = db.Column(db.String(20), unique=False, nullable=False)
    birthyear = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'specie': self.specie,
            'gender': self.gender,
            'height': self.height,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'eye_color': self.eye_color,
            'birthyear': self.birthyear,
        }


# SPECIES model
class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    average_height = db.Column(db.Integer, unique=False, nullable=False)
    average_lifespan = db.Column(db.Integer, unique=False, nullable=False)
    hair_colors = db.Column(db.String(20), unique=False, nullable=False)
    eye_colors = db.Column(db.String(20), unique=False, nullable=False)
    homewold = db.Column(db.String(20), unique=False, nullable=False)
    language = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<Species %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'average_height': self.average_height,
            'average_lifespan': self.average_lifespan,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'homeworld': self.homeworld,
            'language': self.language,
        }


# PLANETS model
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    gravity = db.Column(db.String(20), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    climate = db.Column(db.String(20), unique=False, nullable=False)
    terrain = db.Column(db.String(20), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
        }


# VEHICLES model
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String(20), unique=False, nullable=False)
    vehicle_class = db.Column(db.String(20), unique=False, nullable=False)
    manufacturer = db.Column(db.String(20), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
        }


# STARSHIPS model
class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String(20), unique=False, nullable=False)
    starship_class = db.Column(db.String(20), unique=False, nullable=False)
    manufacturer = db.Column(db.String(20), unique=False, nullable=False)
    cost_in_credits = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
        }

# FAVORITES model
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id') , unique=False, nullable=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id') , unique=False, nullable=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id') , unique=False, nullable=True)
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id') , unique=False, nullable=True)
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id') , unique=False, nullable=True)

    # Relationships
    user = db.relationship('Users', primaryjoin=user_id == Users.id)
    characters = db.relationship('Characters', primaryjoin=characters_id == Characters.id)
    species = db.relationship('Species', primaryjoin=species_id == Species.id)
    planets = db.relationship('Planets', primaryjoin=planets_id == Planets.id)
    vehicles = db.relationship('Vehicles', primaryjoin=vehicles_id == Vehicles.id)
    starships = db.relationship('Starships', primaryjoin=starships_id == Starships.id)

    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'character_id': self.characters_id,
            'species_id': self.species_id,
            'planets_id': self.planets_id,
            'vehicles_id': self.vehicles_id,
            'starships_id': self.starships_id,
        }
