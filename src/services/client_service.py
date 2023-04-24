from flask import Blueprint, render_template, request
from models.clientModel import ClientModel
from models.clientDAO import ClientDAO

client_bp = Blueprint('client', __name__)

class ClientService:

    @client_bp.route('/sign-up', methods=['GET', 'POST'])
    def create_client():

        msg = ''
        if request.method == 'POST':
            name = request.form["name"]
            email = request.form['email']
            password = request.form['password']
            phone_number = request.form['phone_number']

            print(name)
            print(email)
            print(password)
            print(phone_number)

            state = request.form['state']
            city = request.form['city']
            street = request.form['street']
            complement = request.form['complement']

            client = ClientModel(name, email, password, phone_number)
            print(client.name)
            print(client.email)
            print(client.password)
            print(client.phone_number)
            dao = ClientDAO()

            codigo = dao.create(client)

            if codigo > 0:
                msg = ("Cadastrado com sucesso!")
            else:
                msg = ("Erro ao cadastrar!")

        vartitulo = "Cadastro"
        return render_template("sign-up.html", titulo=vartitulo, msg=msg)
