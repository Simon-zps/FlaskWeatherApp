from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.secret_key = 'fsdjhbsefgy4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cities.sqlite3'

db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name


def get_weather(name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid=5cbe52b855cbe0a353eb7d0dcd3e4d8e&lang=pl'
    return requests.get(url.format(name)).json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['yourcity']
        rows = db.session.query(City).count()

        if not City.query.filter_by(name=name).first() and rows < 5:
            weather = get_weather(name)
            if weather['cod'] == 200:
                city = City(name)
                db.session.add(city)
                db.session.commit()
                flash(f'{name} added to the database')
            else:
                flash(f"{name} doesn't exist")
        elif rows >= 5:
            flash('Too many cities on the list, delete at least one to enter new')
        else:
            flash(f'{name} already in the database')

    cities = City.query.all()
    weather_data = []

    for city in cities:
        r = get_weather(city.name)

        weather = {
             'city': city.name,
             'temperature': round(r['main']['temp'] - 273, 2),
             'description': r['weather'][0]['description'].capitalize(),
        }

        weather_data.append(weather)
    return render_template('index.html', weather_data=weather_data)


@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()
    flash(f'{name} deleted from the database')
    return redirect(url_for('index'))


@app.route('/cleardata')
def clear_data():
    for ct in City.query.all():
        db.session.delete(ct)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
