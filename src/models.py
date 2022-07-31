from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USER's Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.email

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
    homeworld = db.Column(db.String(20), unique=False, nullable=False)
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

# FAVORITES Characters model
class Favorites_characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), unique=False, nullable=False)

    # Relationships
    users = db.relationship('Users', primaryjoin=user_id == Users.id)
    characters = db.relationship('Characters', primaryjoin=character_id == Characters.id)

    def __repr__(self):
        return '<Favorites_characters %r>' % self.name

    def serialize(self):
        return {
            'user_id': self.user_id,
            'character_id': self.character_id
        }
        
# FAVORITES Planets model
class Favorites_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    planet_id = db.Column(db.Integer,db.ForeignKey('planets.id'), unique=False, nullable=False)

    # Relationships
    users = db.relationship('Users', primaryjoin=user_id == Users.id)
    planets = db.relationship('Planets', primaryjoin=planet_id == Planets.id)

    def __repr__(self):
        return '<Favorites_planets %r>' % self.name

    def serialize(self):
        return {
            'user_id': self.user_id,
            'planet_id': self.planet_id
        }

# FAVORITES Species model
class Favorites_species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    specie_id = db.Column(db.Integer,db.ForeignKey('species.id'), unique=False, nullable=False)

    # Relationships
    users = db.relationship('Users', primaryjoin=user_id == Users.id)
    species = db.relationship('Species', primaryjoin=specie_id == Species.id)

    def __repr__(self):
        return '<Favorites_species %r>' % self.specie_id

    def serialize(self):
        return {
            'user_id': self.user_id,
            'specie_id': self.specie_id
        }

# FAVORITES Vehicles model
class Favorites_vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    vehicle_id = db.Column(db.Integer,db.ForeignKey('vehicles.id'), unique=False, nullable=False)

    # Relationships
    users = db.relationship('Users', primaryjoin=user_id == Users.id)
    vehicles = db.relationship('Vehicles', primaryjoin=vehicle_id == Vehicles.id)

    def __repr__(self):
        return '<Favorites_vehicles %r>' % self.name

    def serialize(self):
        return {
            'user_id': self.user_id,
            'vehicle_id': self.vehicle_id
        }

# FAVORITES Starships model
class Favorites_starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=False, nullable=False)
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'), unique=False, nullable=False)

    # Relationships
    users = db.relationship('Users', primaryjoin=user_id == Users.id)
    starships = db.relationship('Starships', primaryjoin=starship_id == Starships.id)

    def __repr__(self):
        return '<Favorites_starships %r>' % self.name

    def serialize(self):
        return {
            'user_id': self.user_id,
            'starship_id': self.starship_id
        }

