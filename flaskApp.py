from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('welcome.html')

# prediction page
@app.route('/prediksi')
def prediksi():
    return render_template('prediksi.html')

# result page
@app.route('/hasil', methods = ['GET', 'POST'])
def hasil():
    if request.method == 'POST':
        sex = int(request.form['sex'])
        age = int(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        pclass = int(request.form['pclass'])
        fare = int(request.form['fare'])

        if int(sex) == 0:
            if int(age) < 15:
                female = 1; male = 0; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 1; male = 0; child = 0 
                man = 0; woman = 1; adultman = 0
        else:
            if int(age) < 15:
                female = 0; male = 1; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 0; male = 1; child = 0 
                man = 1; woman = 0; adultman = 1
        
        if int(sibsp) == 0 and int(parch) == 0:
            alone = 1
        else:
            alone = 0

        # [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
        # fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
        prediksi = model.predict([[
            female, male, child, man, woman, pclass, age, 
            sibsp, parch, fare, adultman, alone
        ]])[0]

        dataHasil = {
            'female': female, 'male': male, 'child': child, 
            'man': man, 'woman': woman, 'pclass': pclass, 
            'age': age, 'sibsp': sibsp, 'parch': parch, 
            'fare': fare, 'adultman': adultman, 'alone': alone,
            'PREDIKSI': int(prediksi)
        }

        return render_template('hasil.html', hasil=dataHasil)

# POST 12 vars to titanic model
@app.route('/postTitanic12', methods = ['GET', 'POST'])
def postTitanic12():
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
            'female' : female,
            'male' : male,
            'child' : child,
            'man' : man,
            'woman' : woman,
            'pclass' : pclass,
            'age' : age,
            'sibsp' : sibsp,
            'parch' : parch,
            'fare' : fare,
            'adultman' : adultman,
            'alone' : alone,
            'zPREDIKSI': int(prediksi)
        })

# POST 6 vars to titanic model
@app.route('/postTitanic6', methods = ['GET', 'POST'])
def postTitanic6():
    if request.method == 'POST':
        body = request.json
        
        sex = body['sex']   # female = 0, male = 1
        age = body['age']
        sibsp = body['sibsp']
        parch = body['parch']
        pclass = body['pclass']
        fare = body['fare']

        if int(sex) == 0:
            if int(age) < 15:
                female = 1; male = 0; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 1; male = 0; child = 0 
                man = 0; woman = 1; adultman = 0
        else:
            if int(age) < 15:
                female = 0; male = 1; child = 1 
                man = 0; woman = 0; adultman = 0
            else:
                female = 0; male = 1; child = 0 
                man = 1; woman = 0; adultman = 1
        
        if int(sibsp) == 0 and int(parch) == 0:
            alone = 1
        else:
            alone = 0

        # [ 0.    1.    0.    1.    0.    3.     22.    1.    0.    7.25     1.    0.  ]
        # fm   male  child  man  woman  pclass  age  sibsp  par   fare   adultM   alone
        prediksi = model.predict([[
            female, male, child, man, woman, pclass, age, 
            sibsp, parch, fare, adultman, alone
        ]])[0]

        print(prediksi)
        return jsonify({
            '0response' : 'POST successful!', 
            'female' : female,
            'male' : male,
            'child' : child,
            'man' : man,
            'woman' : woman,
            'pclass' : pclass,
            'age' : age,
            'sibsp' : sibsp,
            'parch' : parch,
            'fare' : fare,
            'adultman' : adultman,
            'alone' : alone,
            'zPREDIKSI': int(prediksi)
        })

if __name__ == '__main__':
    model = joblib.load('modelTitanic')
    app.run(debug = True, port = 1234)