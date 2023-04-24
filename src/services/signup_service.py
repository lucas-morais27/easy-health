from flask import render_template, request, redirect, url_for
from app import app, db
from flask import jsonify
from models.clientModel import ClientModel
from models.client_address_model import AddressModel

class SignupService:

    @app.route('/sign-up/client', methods=['GET', 'POST'])
    def register(self):

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        state = request.form['state']
        city = request.form['city']
        street = request.form['street']
        complement = request.form['complement']
        health_plan = request.form['health_plan']

        address = AddressModel(state=state, city=city, street=street, complement=complement)

        db.session.add(address)
        db.session.commit()

        client = ClientModel(name=name, email=email, password=password, phone_number=phone_number, health_plan=health_plan, address=address)

        test = ClientModel(name='Joana', email='AA@AA', password='bbbb', phone_number=232323, state='asdasd', city='asdas', street='apdi', complement='casa', health_plan='farmacia')

        db.session.add(client)
        db.session.commit()

        teste = client.query.get(client)
        if teste is not None:
            return True
        else:
            return False

        

    @app.route('/sign-up')
    def render_signup():
        return render_template('sign-up.html')
    