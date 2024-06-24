from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] =''  # Cambia esto a tu contraseña
app.config['MYSQL_DB'] = 'ecotrueque_db'

# Inicializar MySQL
mysql = MySQL(app)

# Clave secreta para la gestión de sesiones
app.secret_key = '1234'

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM publicaciones')
    items = cursor.fetchall()
    cursor.close()
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])

def add():
    if request.method == 'POST':
        # Obtener los datos del formulario
        articulo = request.form['articulo']
        
        categoria = request.form['categoria']
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
       

        # Conectar y ejecutar la inserción en la base de datos
        cursor = mysql.connection.cursor()
        try:
            cursor.execute('INSERT INTO publicaciones (articulo, categoria, titulo, descripcion ) VALUES (%s, %s, %s, %s)', 
                            (articulo, categoria, titulo, descripcion ))
            mysql.connection.commit()
            flash('prueba ###publicacion agregada a la base de datos correctamente!!!####')
        except Exception as e:
            flash(f'Hubo un error al agregar a bd: {str(e)}')
            mysql.connection.rollback()
        finally:
            cursor.close()

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)