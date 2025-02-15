from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def principal():
    title = "Mi Portfolio"
    return render_template('index.html', title=title)


@app.route('/skills')
def skills():
    return render_template('lenguajes.html')

@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@app.route('/proyectos')
def proyectos():
    projects = [
        {
            'title': 'Sistema de Control de Horas',
            'description': 'Aplicación para el control y gestión de horas trabajadas.',
            'image': 'fondo.jpg',
            'link': 'https://github.com/usuario/proyecto'
        },
        {
            'title': 'Aplicación Móvil',
            'description': 'En desarrollo',
            'image': 'fondo.jpg',
            'link': 'https://github.com/usuario/proyecto'
        }
    ]
    return render_template('proyectos.html', projects=projects)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ =='_main_':
    app.run(debug=True)