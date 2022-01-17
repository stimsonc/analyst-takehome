from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Pets database definitions
db = SQLAlchemy(app)
class Pet(db.Model):

    __tablename__ = 'pets'

    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return '<Pet %r>' % self.name

    def to_json(self):
        json_str = "{ 'name': %s, 'breed': %s }" % (self.name, self.breed)
        return json_str
db.create_all()


# Landing page
@app.route("/")
def index():
    return render_template('index.html')

# Add pet
@app.route('/addpet', methods=('GET', 'POST'))
def addpet():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        if breed not in ['cat', 'dog']:
            return 'Invalid breed. Please enter either "cat" or "dog".'
        pet = Pet(name, breed)
        db.session.add(pet)
        db.session.commit()
    return render_template('addpet.html')

@app.route('/petinquiry', methods=('GET', 'POST'))
def petinquiry():
    if request.method == 'POST':
        name = request.form['name']
        query = Pet.query.filter_by(name=name).all()
        if query:
            return render_template('petwithname.html', query=query)
        else:
            return render_template('petinquiry.html')
    return render_template('petinquiry.html')

@app.route("/seeall")
def seeall():
    return render_template('seeall.html', pets=Pet.query.all())

@app.route("/newestpet")
def newestpet():
    pet = Pet.query.order_by(Pet.ID.desc()).first()
    return render_template('newestpet.html', pet=pet)

@app.route("/<string:name>")
def petwithname(name):
    query = Pet.query.filter_by(name=name).all()
    return render_template('petwithname.html', query=query)
