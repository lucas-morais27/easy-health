from flask import render_template, request
from app import app

class SignupService:

    def authentication(self):

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        state = request.form['state']
        city = request.form['city']
        street = request.form['street']
        complement = request.form['complement']
        health_plan = request.form['health_plan']

        print(name)
        print(city)

        if request.method == "POST":

            body = {
                'name': name,
                'email': email,
                'password': password,
                'phone_number': phone_number,
                'address': {
                    'state': state,
                    'city': city,
                    'street': street,
                    'complement': complement
                },
                'health_plan': health_plan
            }
        

    @app.route('/sign-up')
    def render_signup():
        return render_template('sign-up.html')
    