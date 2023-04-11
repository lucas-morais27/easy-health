from global_variables import BASE_URL
from requests import get, post
from unittest import TestCase, main

CLIENTS_URL = f'{BASE_URL}/clients'

class TestClient(TestCase):

    def test_create_user(self):
        body = {
            'name': 'User Name',
            'email': 'user_email@email.com',
            'password': 'userpassword',
            'phone_number': 889999999,
            'address': {
                'state': 'RN',
                'city': 'Natal',
                'street': 'Avenida Salgado Filho',
                'complement': 'Ap 123'
            },
            'health_plan': 'unimed'
        }
        response = post(CLIENTS_URL, json=body)
        self.assertEqual(response.status_code, 201, response.json())
        self.assertIn('id', response.json().keys())
        self.assertTrue(response.json().get('id'))
        body.pop('password')
        data = response.json()
        data['address'].pop('client')
        data['address'].pop('id')
        for k in body.keys():
            self.assertEqual(data.get(k), body.get(k))

    def test_get_user(self):
        print(get(f'{CLIENTS_URL}').json())        

if __name__ == '__main__':
    main()
