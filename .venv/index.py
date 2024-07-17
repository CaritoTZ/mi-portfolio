from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarlenguajes():
    mislenguajes=("Pyhton", "Java", "C#", "JavaScripts")
    return render_template('lenguajes.html', lenguajes=mislenguajes)

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ =='_main_':
    app.run(debug=True)