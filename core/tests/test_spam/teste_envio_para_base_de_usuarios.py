from core.spam.enviador_de_email import Enviador
from core.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )