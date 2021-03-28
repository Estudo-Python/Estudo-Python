from unittest.mock import Mock

import pytest

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Matheus', email='fe_matheus@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'felipe.nsilva@gmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
    enviador.enviar.assert_called_once_with(
        'felipe.nsilva@gmail.com',
        'fe_matheus@hotmail.com',
        'Estudo python',
        'Estudando Pytools'
    )
