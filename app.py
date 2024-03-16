from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase 
from SignUp import SignUp

db = dbase.dbConnection()

app = Flask(__name__)

# Ruta para la página de decisión entre registro e inicio de sesión
@app.route('/')
def decision():
    return render_template('decision.html')

# Ruta para el registro de empleados
@app.route('/SignUp', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = db['EmployeesDetails']
        name = request.form['name']
        lastName = request.form['lastName']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        adress = request.form['adress']
        position = request.form['position']
        
        # Verificar el formato del email utilizando una expresión regular
        import re
        if not re.match(r'[\w.-]+@ejad\.com\.mx', email):
            return jsonify({'message': 'El formato del email no es válido. Debe ser de la forma example@ejad.com.mx'}), 400
    
        # Verificar si el email ya existe en la base de datos
        existing_user = users.find_one({'Email': email})
        if existing_user:
            return jsonify({'message': 'El email ya está registrado. Por favor, utiliza otro email.'}), 400
        
        if name and lastName and password and email and phone and adress and adress and position:
            user = SignUp(name,lastName,password,email,phone,adress,position)
            users.insert_one(user.toDBCollection())
            return redirect(url_for('home'))  # Redireccionar a la página principal
    
    # Si la solicitud no es POST o si hay un error en el registro, renderizar el formulario de registro
    return render_template('signup.html')


# Ruta para el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Verificar las credenciales en la base de datos
        user = db['EmployeesDetails'].find_one({'Email': email, 'Password': password})
        if user:
            return redirect(url_for('home'))  # Redireccionar a la página principal
        else:
            return jsonify({'message': 'Credenciales incorrectas'}), 401
    
    return render_template('login.html')

# Ruta para la página principal (home)
@app.route('/home')
def home():
    users = db['EmployeesDetails']
    usersReceived = users.find()
    return render_template('home.html', users=usersReceived)  # Renderizar la pantalla principal

# Método para eliminar un usuario
@app.route('/delete/<string:user_name>')
def delete(user_name):
    users = db['EmployeesDetails']
    users.delete_one({'name': user_name}) 
    return redirect(url_for('home'))

# Método para editar un usuario
@app.route('/edit/<string:user_name>', methods=['POST'])
def edit(user_name):
    users = db['EmployeesDetails']
    name = request.form['name']
    lastName = request.form['lastName']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    adress = request.form['adress']
    position = request.form['position']
    
    if name and lastName and password and email and phone and adress and adress and position:
        users.update_one({'name': user_name}, {'$set': {'name': name,'lastName': lastName,'password': password,'email': email,'phone': phone,'adress': adress,'position': position}})
        return redirect(url_for('home'))
    else:
        return notFound()

# Manejador de error 404
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)
