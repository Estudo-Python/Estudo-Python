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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
    assert len(usuarios) == enviador.quantidade_de_emails_enviados
