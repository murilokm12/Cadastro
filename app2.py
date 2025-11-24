from flask import Flask, redirect, render_template, request, url_for



app = Flask(__name__)



# 1- criar a rota para acessar a pagina home e depois uma rota paraa acessar a pagina produtos
# 2- criar uma lista de objetos (produtos)
# 3 cosumir a lista na pagina ome 


products = [{
    'nome':'camisetas',
    'qtd_estoque':155,
    'img_url':'https//:camisas',
    'id':'produto1'
},
{
     'nome':'calças',
    'qtd_estoque':312,
    'img_url':'https//:calças',
     'id':'prodto2'
}


]

@app.route('/')
def index():
    return render_template('home.html',produtos=products)





# @app.route('/podutos',methods= ['POST'])


# def produtos():
# nome = request.form['nome']
# estoque = request.form['qtd_estoque']
# url = request.form['qtd_estoque']
# produto = request.form['img_url']
# produto = request.form['id']

# products.append({
#         'nome': produto1,
#         'qtd_estoque': produtos2
#     })




app.run(debug=True)



