class ProfessionalModel():
    def __init__(self, provides_home_service, specialty, council_registration, twitter, insta, linkedin, bio, name, email, password, phone_number):
        self.provides_home_service = provides_home_service
        self.specialty = specialty
        self.council_registration = council_registration
        self.twitter = twitter
        self.insta = insta
        self.linkedin = linkedin
        self.bio = bio
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def get_id(self):
        return self.id
