from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def homepage():
    imc = None
    if request.method == 'POST':
        peso = float(request.form['pesoForm'])
        altura = float(request.form['alturaForm'])
        imc = peso/altura**2
    return render_template('index.html',imc=imc)
if __name__ == '__main__':
    app.run(debug=True)
 