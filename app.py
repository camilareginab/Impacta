from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configurações do MySQL
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'CaCa',
    'database': 'biblioteca'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autores', methods=['GET', 'POST'])
def autores():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        cursor.execute("INSERT INTO autores (nome) VALUES (%s)", (nome,))
        conn.commit()
        return redirect('/autores')
    
    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('autores.html', autores=autores)

@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        cursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (nome,))
        conn.commit()
        return redirect('/categorias')
    
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('categorias.html', categorias=categorias)


if __name__ == '__main__':
    app.run(debug=True)
