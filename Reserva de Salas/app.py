from flask import Flask
from database import db
from reserva_route import reservas_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(reservas_blueprint)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=5001, debug=True)