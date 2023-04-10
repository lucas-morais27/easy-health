import pprint
from requests import post
import global_variables
import unittest

PROF_URL = f'{global_variables.BASE_URL}/professional'


class TestProfessional(unittest.TestCase):

    def test_create_professional(self):
        body = {
            'name': 'User Professional 2',
            'email': 'professional2@email.com',
            'password': 'strongcomplicated1234',
            'phone_number': 849555555,
            'addresses': [
                {
                    'state': 'RN',
                    'city': 'Natal',
                    'street': 'Avenida Prudente de Morais',
                    'complement': 'AP 123 Bloco G'
                },
                {
                    'state': 'SP',
                    'city': 'São Paulo',
                    'street': 'Avenida 25 de Março',
                    'complement': 'AP 567 Bloco B'
                }
            ],
            'provides_home_service': True,
            'specialty': 'medicina',
            'subspecialties': ['dermo', 'nutri'],
            'accepted_health_plans': ['bradesco', 'hapvida'],
            'council_registration': 1802,
            'twitter': 'aaaaa',
            'insta': '@aaaa',
            'linkedin': 'aaaaa',
            'bio': 'aaaaaa'
        }
        response = post(PROF_URL, json=body)
        self.assertEqual(response.status_code, 201, response.content)
        pprint.pprint(response.json(), indent=4)


if __name__ == '__main__':
    unittest.main()
