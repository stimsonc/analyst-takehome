from flask import Flask, render_template, request
from functions import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/seeall")
def seeall():
    pets = get_all()
    return render_template('seeall.html', pets=pets)

@app.route("/newestpet")
def newestpet():
    pet = get_newestpet()
    return render_template('newestpet.html', pet=pet)

@app.route("/<string:pet>")
def petwithname(pet):
    pet = get_pet(pet)
    return render_template('petwithname.html', pet=pet)

@app.route('/addpet', methods=('GET', 'POST'))
def addpet():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']

        conn = get_db_connection()
        conn.execute('INSERT INTO pets (Name, Breed) VALUES (?, ?)',
                        (name, breed))
        conn.commit()
        conn.close()
        pet = get_pet(name)
        return render_template('petwithname.html', pet=pet)

    return render_template('addpet.html')

@app.route('/petinquiry', methods=('GET', 'POST'))
def petinquiry():
    if request.method == 'POST':
        name = request.form['name']
        pet = get_pet(name)
        return render_template('petwithname.html', pet=pet)

    return render_template('petinquiry.html')
