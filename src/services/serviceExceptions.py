from MySQLdb._exceptions import DataError
class ServiceExeption(Exception):
    pass

class EmailIndisponivel(Exception):
    def __init__(self) -> None:
        self.msg="Já existe um usuario com esse email, isso é um erro"
        super().__init__(self.msg)


class EmailInexistente(Exception):
    "Email inexistente"

class UsuarioDesativado(Exception):
    "Usuário desativo"

class SenhaIncorreta(Exception):
    "Senha incorreta"

class NenhumEncontrado(Exception):
    "Nenhum Profissional Encontrado"

class ErroNoBanco(DataError):
    def __init__(self, fonte:str) -> None:
        self.msg=f"Erro no em preenchimento de campo de: {fonte}"
        super().__init__(f"Erro de dado no banco MySQL, fonte do erro: {fonte},\
                          um ou mais campos podem estar com mais caracteres que o permitido")