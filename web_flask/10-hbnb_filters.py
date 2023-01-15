#!/usr/bin/python3
"""
Script that starts web flask application
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_int(n):
    """display html page only if int given
       place given int into html template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_odd_or_even(n):
    """display html page only if int given
       place given int into html template
       substitute text to display if int is odd or even
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def tear_down(self):
    """removing current SQLAlchemy session"""
    storage.close()


@app.route('/states_list/', strict_slashes=False)
def states_list():
    """states_list route"""
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html', state_objs=state_objs)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states route"""
    state_objs = [s for s in storage.all("State").calues()]
    return render_template('8-cities_by_states.html', state_objs=state_objs)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """fetch sorted cities for state ID"""
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state
    return render_template('9-states.html', state_obj=state_obj)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """html page  with city & state filters & amenities"""
    state_objs = [s for s in storage.all("State").values()]
    amenity_objs = [a for a in storage.all("Amnenity").values()]
    return rendered_template('10-hbnb_filters.html', state_objs=state_objs,
                             amenity_objs=amenity_objs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
