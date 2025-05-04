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

@app.route('/livros', methods=['GET', 'POST'])
def livros():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor_id = request.form['autor_id']
        categoria_id = request.form['categoria_id']
        cursor.execute("INSERT INTO livros (titulo, autor_id, categoria_id) VALUES (%s, %s, %s)", (titulo, autor_id, categoria_id))
        conn.commit()
        return redirect('/livros')
    
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('livros.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)
