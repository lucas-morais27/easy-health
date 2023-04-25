from flask import Blueprint, render_template, request
from models import db
from controller.healthplan_controller import HealthPlanController
from controller.address_client_controller import AddressClientController

client_bp = Blueprint('client', __name__)

class ClientController():

    @client_bp.route('/sign-up/client', methods=['GET', 'POST'])
    def create():
        msg = ''
        if request.method == 'POST':
            health_plan = request.form['health_plan']
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            phone_number = request.form['phone_number']

            state = request.form['state']
            city = request.form['city']
            street = request.form['street']
            complement = request.form['complement']

            if HealthPlanController().create(health_plan):

                sql = "INSERT INTO client(health_plan, active, name, email, password, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor = db.cursor()
                cursor.execute(sql, (health_plan, 1, name, email, password, phone_number,))
                db.commit()

                


                if AddressClientController().create(1, state, city, street, complement):
                    msg = ("Cadastrado com sucesso!")
                else:
                    msg = ("Erro ao cadastrar!")

        return render_template("sign-up-client.html", msg=msg)
            
        
    def authenticate(email, password):
        try:
            sql = "SELECT * FROM client WHERE email=%s AND password=%s"
            cursor = db.cursor()
            cursor.execute(sql, (email, password))
            usuario = cursor.fetchone()
            return usuario 
        except:
            return None
        
    def find(id):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM client WHERE id=%s"
            cursor.execute(sql, (id,))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0
        
    def find(self, email):
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM client WHERE email=%s"
            cursor.execute(sql, (email))
            funcionario = cursor.fetchone()
            return funcionario
        except:
            return 0
        
    def update(client):
        try:
            sql = "UPDATE client " \
                  "SET cpf=%s, nome=%s, rua=%s, bairro=%s, cep=%s, numero=%s, telefone=%s, email=%s, sexo=%s WHERE id=%s"

            cursor = db.cursor()
            cursor.execute(sql, (client.cpf, client.nome, client.rua, client.bairro,
                                 client.cep, client.numero, client.telefone, client.email, client.sexo, client.id))
            db.commit()
            return cursor.rowcount
        except:
            return 0
        
    def disable(id):
        try:
            sql = "UPDATE client SET active=0 WHERE id=%s"
            cursor = db.cursor()
            cursor.execute(sql, (id,))
            db.commit()
            return cursor.rowcount
        except:
            return 0
        
    def delete(id):
        try:
            sql = "DELETE FROM client WHERE id = %s"
            cursor = db.cursor()
            cursor.execute(sql, (id,))
            db.commit()
            return cursor.rowcount
        except:
            return 0
