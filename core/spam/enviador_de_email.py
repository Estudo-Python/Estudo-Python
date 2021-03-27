class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido
        return remetente


class EmailInvalido(Exception):
    pass