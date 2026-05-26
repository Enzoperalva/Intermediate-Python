class Conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password
    
    def listen_inf_user(self):
        if not self.user or not self.password:
            return 'User incomplet'
        
        return f'{self.user} | {self.password}'

    @classmethod
    def create_with_auth(cls, user ,password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y


c1 = Conection.create_with_auth('Enzo', 1221874819)
print(c1.listen_inf_user())

print()

c2 = Conection()
c2.set_user('Enzo')
c2.set_password('@Enzo_2008')
print(c2.listen_inf_user())