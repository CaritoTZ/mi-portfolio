from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def principal():
    title = "Mi Portfolio"
    return render_template('index.html', title=title)


@app.route('/skills')
def skills():
    mislenguajes=("Pyhton", "Java", "C#", "JavaScripts")
    return render_template('lenguajes.html', lenguajes=mislenguajes)

@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ =='_main_':
    app.run(debug=True)