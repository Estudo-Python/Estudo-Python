import pytest

from core.spam.enviador_de_email import Enviador
from core.spam.main import EnviadorDeSpam
from core.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Felipe', email='felipematheus.ns0@gmail.com'),
            Usuario(nome='Matheus', email='fe_matheus@hotmail.com')
        ],
        [
            Usuario(nome='Matheus', email='fe_matheus@hotmail.com')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
    assert len(usuarios) == enviador.quantidade_de_emails_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        self.parametros_de_envio = None
        self.quantidade_de_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.quantidade_de_emails_enviados += 1
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Matheus', email='fe_matheus@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
    assert enviador.parametros_de_envio == (
        'felipe.nsilva@gmail.com',
        'fe_matheus@hotmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
