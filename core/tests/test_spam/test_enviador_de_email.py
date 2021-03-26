from core.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'felipematheus.ns0@gmail.com',
        'felipe.nsilva@ambevtech.com.br',
        'Estudo Python',
        'Testando pytest'
        )
    assert 'felipematheus.ns0@gmail.com' in resultado
