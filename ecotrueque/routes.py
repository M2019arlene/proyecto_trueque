# Importaciones correctas de Flask y otros módulos necesarios
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, Registro, Publicaciones  # Asegúrate de las importaciones correctas de los modelos
from sqlalchemy import Column, Integer, String, Text, LargeBinary




#UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'upload')


bp = Blueprint('routes', __name__)
# Definición del Blueprint

@bp.route('/')
def index():
    publicaciones = Publicaciones.query.all()  # Obtener todas las publicaciones de la base de datos
    return render_template('index.html', publicaciones=publicaciones)



@bp.route('/register', methods=['GET', 'POST'])
def register():     
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['correo']
        password = request.form['password']
        genero = request.form['genero']
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        new_user = Registro(usuario=nombre, email=email, contraseña=hashed_password, nombre=nombre, apellido=apellido, genero=genero)
        db.session.add(new_user)
        db.session.commit()
        
        flash('User registered successfully', 'success')
        return redirect(url_for('routes.index'))
    
    return render_template('Registro.html')



@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['correo']
        password = request.form['password']

        user = Registro.query.filter_by(email=email).first()

        if user:
            print(f"User found: {user.nombre}")  # Debugging
            print(f"Stored hashed password: {user.contraseña}")
            print(f"Password to check: {password}")

            if check_password_hash(user.contraseña, password):
                flash('Logged in successfully', 'success')
                return redirect(url_for('routes.index'))
            else:
                print("Password check failed")  # Debugging
                flash('Login failed. Check your email and/or password', 'danger')
                return redirect(url_for('routes.login'))
        else:
            print("User not found")  # Debugging
            flash('Login failed. Check your email and/or password', 'danger')
            return redirect(url_for('routes.login'))

    return render_template('IniciarSesion.html')

# Ruta para cargar un producto con imagen
@bp.route('/cargar_producto', methods=['GET', 'POST'])
def cargar_producto():
    if request.method == 'POST':
        titulo = request.form.get('nombre_articulo')
        descripcion = request.form.get('descripcion')
        imagenes = request.form.get('imagenes')  # Obtén el url de imagen desde el formulario

        if not titulo or not descripcion or not imagenes:
            flash('Por favor, completa todos los campos', 'danger')
            return redirect(url_for('routes.cargar_producto'))

        # Guarda el archivo en el directorio especificado
        #filename = secure_filename(imagenes.filename)  # Seguro para evitar nombres maliciosos
       # imagenes.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        # Crea una nueva instancia de Publicaciones y guarda la referencia a la imagen
        nueva_publicacion = Publicaciones(titulo=titulo, descripcion=descripcion, imagenes=imagenes)
        db.session.add(nueva_publicacion)
        db.session.commit()

        flash('Publicación agregada correctamente', 'success')
        return redirect(url_for('routes.cargar_producto'))
        
    #return render_template('cargar_producto.html')
    # Asegúrate de pasar un contexto con las variables necesarias para renderizar la plantilla
    return render_template('cargar_producto.html', result_id=17)  # Aquí result_id es un ejemplo, asegúrate de pasar el valor correcto

@bp.route('/mostrar_publicaciones') 
def mostrar_publicaciones():
    publicaciones = Publicaciones.query.all()  # Obtener todas las publicaciones de la base de datos
    return render_template('mostrar_publicaciones.html', publicaciones=publicaciones)

@bp.route('/buscar_publicacion', methods=['GET'])
def buscar_publicacion():
    pub_id = request.args.get('id')
    if not pub_id:
        flash('ID de publicación no proporcionado', 'danger')
        return redirect(url_for('routes.index'))
    
    try:
        pub_id = int(pub_id)
        publicacion = Publicaciones.query.get(pub_id)
        if publicacion:
            return render_template('mostrar_publicaciones.html', publicacion=publicacion)
        else:
            flash('Publicación no encontrada', 'danger')
            return redirect(url_for('routes.index'))
    except ValueError:
        flash('ID de publicación inválido', 'danger')
        return redirect(url_for('routes.index'))


@bp.route('/editar_publicacion/<int:pub_id>', methods=['GET', 'POST'])
def editar_publicacion(pub_id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        imagenes = request.form.get('imagenes')

        if not titulo or not descripcion or not imagenes:
            flash('Por favor, completa todos los campos', 'danger')
            return redirect(url_for('routes.editar_publicacion', pub_id=pub_id))

        publicacion = Publicaciones.query.get(pub_id)
        if publicacion:
            publicacion.titulo = titulo
            publicacion.descripcion = descripcion
            publicacion.imagenes = imagenes
            db.session.commit()
            flash('Publicación actualizada correctamente', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Publicación no encontrada', 'danger')
            return redirect(url_for('routes.index'))

    # Si la solicitud es GET, muestra el formulario de edición
    publicacion = Publicaciones.query.get(pub_id)
    if publicacion:
        return render_template('editar_publicacion.html', publicacion=publicacion)
    else:
        flash('Publicación no encontrada', 'danger')
        return redirect(url_for('routes.index'))



@bp.route('/eliminar_publicacion/<int:pub_id>', methods=['POST'])
def eliminar_publicacion(pub_id):
    publicacion = Publicaciones.query.get(pub_id)
    if publicacion:
        db.session.delete(publicacion)
        db.session.commit()
        flash('Publicación eliminada correctamente', 'success')
    else:
        flash('Publicación no encontrada', 'danger')
    return redirect(url_for('routes.index'))