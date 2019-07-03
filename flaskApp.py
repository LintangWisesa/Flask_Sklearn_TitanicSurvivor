from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return '<h1>Welcome!</h1>'

# POST to titanic model
@app.route('/postTitanic', methods = ['GET', 'POST'])
def postTitanic():
    if request.method == 'POST':
        body = request.json
        
        # [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
        # fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
        female = body['female']
        male = body['male']
        child = body['child']
        man = body['man']
        woman = body['woman']
        pclass = body['pclass']
        age = body['age']
        sibsp = body['sibsp']
        parch = body['parch']
        fare = body['fare']
        adultman = body['adultman']
        alone = body['alone']
        prediksi = model.predict([[
            female, male, child, man, woman, pclass, age, 
            sibsp, parch, fare, adultman, alone
        ]])[0]

        print(prediksi)
        return jsonify({
            '0response' : 'POST successful!', 
            'female' : body['female'],
            'male' : body['male'],
            'child' : body['child'],
            'man' : body['man'],
            'woman' : body['woman'],
            'pclass' : body['pclass'],
            'age' : body['age'],
            'sibsp' : body['sibsp'],
            'parch' : body['parch'],
            'fare' : body['fare'],
            'adultman' : body['adultman'],
            'alone' : body['alone'],
            'zPREDIKSI': int(prediksi)
        })

if __name__ == '__main__':
    model = joblib.load('modelTitanic')
    app.run(debug = True, port = 1234)