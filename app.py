from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/student/<name>')
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


if __name__ == '__main__':
    app.run(debug=True, port=3000)

