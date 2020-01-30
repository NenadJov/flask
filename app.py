from flask import Flask, request, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://nenad:Saraivan1$@localhost:3306/python-base"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    model = db.Column(db.String(20))
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(data['name'], data['model'], data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]
        return {"count": len(results), "cars": results}

        
@app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_car(car_id):
    car = CarsModel.query.get_or_404(car_id)
    if request.method == 'GET':
        response = {
            "name": car.name,
            "model": car.model,
            "doors": car.doors
        }
        return {"message": "success", "car": response}
    elif request.method == 'PUT':
        data = request.get_json()
        car.name = data['name']
        car.model = data['model']
        car.doors = data['doors']
        db.session.add(car)
        db.session.commit()
        return {"message": f"car {car.name} successfully updated"}
    elif request.method == 'DELETE':
        db.session.delete(car)
        db.session.commit()
        return {"message": f"Car {car.name} successfully deleted."}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/student/<name>')
def student_name(name):
    #print(name)
    #return 'Hello, Student!'
    return f'Hello, {name}!'

@app.route('/student/<int:age>')
def student_age(age):
    return f'Age: {age}!'

@app.route('/get', methods = ['GET', 'POST'])
def get():
    if request.method == 'GET':
        return 'Get request'
    else:
        return 'Post request'

@app.route('/ciklus')
def ciklus():
    my_list = ['nikola', 'nenad', 'zare', 'biljana']
    object = {#this is dict
        'name':'Nikola',
        'surname':'Stojkovski',
        'age':24,
        'is_active':True
    }
    return render_template('ciklus.html', lista = my_list, my_dict = object)

@app.route('/index/<property>')
def index(property):
    return render_template('index.html', ime = property)

@app.route('/json', methods=['POST'])
def my_json():
    print(request.get_json())
    return 'test post'

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)

