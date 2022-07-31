"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, Response, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
# Flask_bscrypt
from flask_bcrypt import Bcrypt

# Flask_jwt_extended
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Models
from models import db, Users, Characters, Species, Planets, Vehicles, Starships, Favorites_characters, Favorites_planets, Favorites_species, Favorites_vehicles, Favorites_starships

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
MIGRATE = Migrate(app, db)

# Configurations
jwt = JWTManager(app)
db.init_app(app)
setup_admin(app)
CORS(app)
bcrypt = Bcrypt(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Login  ====================================================================
@app.route("/login", methods=["POST"])
def login():
    user_email = request.json.get("email", None)
    user_password = request.json.get("password", None)
    user = Users.query.filter_by( email = user_email ).first()

    # verify request body
    if user_email is None or user_password is None or user is None:
        return jsonify({"msg": "wrong username or password, try again"}), 401
    
    # verify password
    if bcrypt.check_password_hash(user.password, user_password):
        access_token = create_access_token(identity=user_email)
        return jsonify({
            "status": Response().status_code,
            "access_token": access_token
            })
    else:
        return jsonify({"msg": "wrong username or password, try again"}), 401

    
# Register  ====================================================================
@app.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    
    # Comprobations
    if email is None or password is None:
        return jsonify({"msg": "Bad email or password"}), 401

    encrypted_password = bcrypt.generate_password_hash(password)
    new_user = Users(email = email, password = encrypted_password, is_active = True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "user create successfully"}), 200

# Characters  ====================================================================
@app.route('/characters', methods=['GET'])
def handle_characters():
    
    # GET
    if request.method == 'GET':
        characters = Characters.query.all()
        total_characters = len(characters)
        results = list(map(lambda character:character.serialize(), characters))
        response_body = {
            'status': int(Response().status_code),
            'total_characters': total_characters,
            'results': results
        }
        return jsonify(response_body), 200

# Character by ID
@app.route('/characters/<int:id>', methods=['GET'])
def handle_characters_by_id(id):
    
    # GET
    if request.method == 'GET':
        character = Characters.query.get(id)
        result = character.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Species ======================================================================
@app.route('/species', methods=['GET'])
def handle_species():
    
    # GET
    if request.method == 'GET':
        species = Species.query.all()
        total_species = len(species)
        results = list(map(lambda specie: specie.serialize(), species))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_species': total_species
        }
        return jsonify(response_body), 200

# Specie by ID
@app.route('/species/<int:id>', methods=['GET'])
def handle_species_by_id(id):
    
    # GET
    if request.method == 'GET':
        specie = Species.query.get(id)
        result = specie.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Planets ======================================================================
@app.route('/planets', methods=['GET'])
def handle_planets():
    
    # GET
    if request.method == 'GET':
        planets = Planets.query.all()
        total_planets = len(planets)
        results = list(map(lambda planet:planet.serialize(), planets))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_planets': total_planets
        }
        return jsonify(response_body), 200

# Planet by ID
@app.route('/planets/<int:id>', methods=['GET'])
def handle_planets_by_id(id):
    
    # GET
    if request.method == 'GET':
        planet = Planets.query.get(id)
        result = planet.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Vehicles ======================================================================
@app.route('/vehicles', methods=['GET'])
def handle_vehicles():

    # GET
    if request.method == 'GET':
        vehicles = Vehicles.query.all()
        total_vehicles = len(vehicles)
        results = list(map(lambda vehicle:vehicle.serialize(), vehicles))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_vehicles': total_vehicles
        }
        return jsonify(response_body), 200

# Vehicle by ID
@app.route('/vehicles/<int:id>', methods=['GET'])
def handle_vehicles_by_id(id):

    # GET
    if request.method == 'GET':
        vehicle = Vehicles.query.get(id)
        result = vehicle.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Starships ======================================================================
@app.route('/starships', methods=['GET'])
def handle_starships():

    # GET
    if request.method == 'GET':
        starships = Starships.query.all()
        total_starships = len(starships)
        results = list(map(lambda starship:starship.serialize(), starships))
        response_body = {
            'status': int(Response().status_code),
            'results': results,
            'total_vehicles': total_starships
        }
        return jsonify(response_body), 200

# Starship by ID
@app.route('/starships/<int:id>', methods=['GET'])
def handle_starships_by_id(id):

    # GET
    if request.method == 'GET':
        starship = Starships.query.get(id)
        result = starship.serialize()
        response_body = {
            'status': int(Response().status_code),
            'result': result
        }
        return jsonify(response_body), 200

# Favorites ======================================================================
@app.route('/favorites', methods=['GET', 'POST', 'DELETE'])
@jwt_required()
def handle_favorites():

    # GET
    if request.method == 'GET':
        current_user = get_jwt_identity()

        if current_user is None:
            return jsonify({"msg": "please login to see your favorites"}), 401

        user_data = Users.query.filter_by( email = current_user).first()

        fav_characters = Favorites_characters.query.filter_by( user_id = user_data.id ).all()
        fav_planets = Favorites_planets.query.filter_by( user_id = user_data.id ).all()
        fav_species = Favorites_species.query.filter_by( user_id = user_data.id ).all()
        fav_vehicles = Favorites_vehicles.query.filter_by( user_id = user_data.id ).all()
        fav_starships = Favorites_starships.query.filter_by( user_id = user_data.id ).all()

        response_body = {
            'status': int(Response().status_code),
            'results': {
            "characters": list(map(lambda item: Species.query.get(item.character_id).serialize(), fav_characters )),
            "planets": list(map(lambda item: Species.query.get(item.planet_id).serialize(), fav_planets )),
            "species":  list(map(lambda item: Species.query.get(item.specie_id).serialize(), fav_species )),
            "vehicles": list(map(lambda item: Species.query.get(item.vehicle_id).serialize(), fav_vehicles )),
            "starships": list(map(lambda item: Species.query.get(item.starship_id).serialize(), fav_starships )),
            }
        }
        return jsonify(response_body), 200


    # POST
    if request.method == 'POST':
        current_user = get_jwt_identity()
        user = Users.query.filter_by( email = current_user).first()
        category = request.json.get("category", None)
        item_id = request.json.get("id", None)

        if user is not None and category is not None and item_id is not None:
            # Characters
            if category == 'characters':
                exist_item = Favorites_characters.query.filter_by(user_id = user.id, character_id = item_id).first()
                if exist_item is None:
                    new_favorite = Favorites_characters( user_id = user.id ,character_id = item_id )
                    db.session.add(new_favorite)
                    db.session.commit()
                    return jsonify({"msg": "favorite added successfully"}), 200
                else:
                    return jsonify({"msg": "that favorite already exist"}), 200
            
            # Planets
            if category == 'planets':
                exist_item = Favorites_planets.query.filter_by(user_id = user.id, planet_id = item_id).first()
                if exist_item is None:
                    new_favorite = Favorites_planets( user_id = user.id ,planet_id = item_id )
                    db.session.add(new_favorite)
                    db.session.commit()
                    return jsonify({"msg": "favorite added successfully"}), 200
                else:
                    return jsonify({"msg": "that favorite already exist"}), 200

            # Species
            if category == 'species':
                exist_item = Favorites_species.query.filter_by(user_id = user.id, specie_id = item_id).first()
                if exist_item is None:
                    new_favorite = Favorites_species( user_id = user.id ,specie_id = item_id )
                    db.session.add(new_favorite)
                    db.session.commit()
                    return jsonify({"msg": "favorite added successfully"}), 200
                else:
                    return jsonify({"msg": "that favorite already exist"}), 200
            
            # Vehicles
            if category == 'vehicles':
                exist_item = Favorites_vehicles.query.filter_by(user_id = user.id, vehicle_id = item_id).first()
                if exist_item is None:
                    new_favorite = Favorites_vehicles( user_id = user.id ,vehicle_id = item_id )
                    db.session.add(new_favorite)
                    db.session.commit()
                    return jsonify({"msg": "favorite added successfully"}), 200
                else:
                    return jsonify({"msg": "that favorite already exist"}), 200

            # Starships 
            if category == 'starships':
                exist_item = Favorites_starships.query.filter_by(user_id = user.id, starship_id = item_id).first()
                if exist_item is None:
                    new_favorite = Favorites_starships( user_id = user.id ,starship_id = item_id )
                    db.session.add(new_favorite)
                    db.session.commit()
                    return jsonify({"msg": "favorite added successfully"}), 200
                else:
                    return jsonify({"msg": "that favorite already exist"}), 200

            return jsonify({"msg": "The category not exist"}), 400         

        else:
            return jsonify({"msg": "You need to send a category and id"}), 400


    # DELETE
    if request.method == 'DELETE':
        
        current_user = get_jwt_identity()
        user = Users.query.filter_by(email = current_user).first()

        category = request.json.get("category", None)
        item_id = request.json.get("id", None)

        if user is not None and category is not None and item_id is not None:
            if category == 'characters':
                row = Favorites_characters.query.filter_by( user_id = user.id, character_id = item_id ).first()
                db.session.delete(row)
                db.session.commit()
                return jsonify({"result": "favorite removed successfully"}), 200
                
            if category == 'planets':
                row = Favorites_planets.query.filter_by( user_id = user.id, planet_id = item_id ).first()
                db.session.delete(row)
                db.session.commit()
                return jsonify({"msg": "favorite removed successfully"}), 200
                
            if category == 'species':
                row = Favorites_species.query.filter_by( user_id = user.id, specie_id = item_id ).first()
                db.session.delete(row)
                db.session.commit()
                return jsonify({"msg": "favorite removed successfully"}), 200
                
            if category == 'vehicles':
                row = Favorites_vehicles.query.filter_by( user_id = user.id, vehicle_id = item_id ).first()
                db.session.delete(row)
                db.session.commit()
                return jsonify({"msg": "favorite removed successfully"}), 200
                
            if category == 'starships':
                row = Favorites_starships.query.filter_by( user_id = user.id, starship_id = item_id ).first()
                db.session.delete(row)
                db.session.commit()
                return jsonify({"msg": "favorite removed successfully"}), 200

            return jsonify({"msg": "The category not exist"}), 400

        else:
            return jsonify({"msg": "You need to send a category and id"}), 400




######################################################
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
