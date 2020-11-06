# loading enviroment variables
from dotenv import load_dotenv
load_dotenv()

#creates flask application
from flask import Flask
app = Flask(__name__)

#connects to database
from database import init_db
db = init_db(app)

#setup serialization and deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

#registers controllers
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
