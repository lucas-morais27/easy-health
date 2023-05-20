from MySQLdb._exceptions import DataError


class EmailIndisponivel(Exception):
    def __init__(self) -> None:
        self.msg="Já existe um usuario com esse email, isso é um erro"
        super().__init__(self.msg)


class EmailInexistente(Exception):
    def __init__(self) -> None:
        self.msg="Email inexistente"
        super().__init__(self.msg)

class UsuarioDesativado(Exception):
    def __init__(self) -> None:
        self.msg="Usuário desativo"
        super().__init__(self.msg)
    

class SenhaIncorreta(Exception):
    def __init__(self) -> None:
        self.msg="Senha Incorreta"
        super().__init__(self.msg)

class NenhumProfissionalEncontrado(Exception):
    def __init__(self) -> None:
        self.msg="Nenhum Profissional Encontrado"
        super().__init__(self.msg)
    
#DataError é uma class de Exception da biblioteca MySQLdb(biblioteca de conexão com banco MySQL)
#Esse erro é acionado quando o dado é incompativel com a coluna da tabela que está sendo gravado
class ErroNoBanco(DataError):
    def __init__(self, fonte:str) -> None:
        self.msg=f"Erro no em preenchimento de campo de: {fonte}"
        super().__init__(f"Erro de dado no banco MySQL, fonte do erro: {fonte},\
                          um ou mais campos podem estar com mais caracteres que o permitido \
                         ou com caracteres invalidos para o campo")
        
class SemRetorno(TypeError):
    def __init__(self, obj, identificador, valor) -> None:
        self.msg=f"Não Existe nenhum {obj} com {identificador} igual a {valor}"
        super().__init__(self.msg)

class ConflitoDeData(Exception):
    def __init__(self, date, description) -> None:
        self.msg=f"conflito de horario com outra consulta sua: {date} - {description}"
        super().__init__(self.msg)