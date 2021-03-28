import pytest
from core.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # SetUp
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # SetUp
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()
