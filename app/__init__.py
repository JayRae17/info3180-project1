from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Som3$ec5etK*y'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://namoqsjyijrgzf:c5118a88511a95899a55134b2ab2794ae0e62178a4b7620b71b51526a724fdd1@ec2-3-91-112-166.compute-1.amazonaws.com:5432/dd07a9q5ufeik7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
db = SQLAlchemy(app)

# Config Values
# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'
# needed for session security, the flash() method in this case stores the message
# in a session
SECRET_KEY = 'Sup3r$3cretkey'


app.config.from_object(__name__)
from app import views



