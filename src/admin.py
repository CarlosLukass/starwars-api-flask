import os
from flask_admin import Admin
from models import db, Users, Characters, Species, Planets, Vehicles, Starships, Favorites_characters, Favorites_planets, Favorites_species, Favorites_vehicles, Favorites_starships
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Species, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(Vehicles, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(ModelView(Favorites_characters, db.session))
    admin.add_view(ModelView(Favorites_planets, db.session))
    admin.add_view(ModelView(Favorites_species, db.session))
    admin.add_view(ModelView(Favorites_vehicles, db.session))
    admin.add_view(ModelView(Favorites_starships, db.session))
