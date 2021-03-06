import pytest

from core.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['felipematheus.ns0@gmail.com', 'foo@bar.com.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'felipe.nsilva@ambevtech.com.br',
        'Estudo Python',
        'Testando pytest'
    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', [' ', 'foobar.com.br'])
def test_email_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'felipe.nsilva@ambevtech.com.br',
            'Estudo Python',
            'Testando pytest'
        )
