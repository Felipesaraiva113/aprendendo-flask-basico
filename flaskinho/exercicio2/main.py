from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def home():
    pares = []
    impares = []
    numero = None
    if request.method == 'POST':
        numero = str(request.form['numbers'])
        for i in numero:
            if int(i) % 2 == 0:
                pares.append(int(i))
            else:
                impares.append(int(i))
    return render_template('index.html',pares=pares,numero=numero,impares=impares)
if __name__ == '__main__':
    app.run(debug=True) 





