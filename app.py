from flask import Flask, redirect, render_template, request, url_for
import sqlite3


app = Flask(__name__)

def init():
   conn = sqlite3.connect('alunix.db')
   cursor = conn.cursor()

   cursor.execute('''CREATE TABLE if not exists alunos(
                  
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome text,
                   email text,
                   idade integer)
                  
                  
                  ''')   



   conn.commit()  
   conn.close()

init()

@app.route('/deletar/<int:aluno_id>', methods= ['POST'])
def deletar(aluno_id):
    conn = sqlite3.connect('alunix.db')
    cursor = conn.cursor()
    cursor.execute(' DELETE FROM alunos WHERE id = ?' , (aluno_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/')
def index():
    conn = sqlite3.connect('alunix.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return render_template('index.html',  alunos = alunos  )

  

@app.route('/adicionar',methods= ['POST'])

def adicionar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    conn = sqlite3.connect('alunix.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO alunos( nome, email, idade)values(?,?,?)',(nome,  email,idade))   

    conn.commit()  
    conn.close()

    return redirect(url_for('index'))




app.run(debug=True)