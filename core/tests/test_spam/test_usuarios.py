from core.spam.db import Conexao
from core.spam.modelos import Usuario


def test_salvar_usuario():
    # SetUp
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    ##
    usuario = Usuario(nome='Felipe')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    # Tear Down
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
    ##


def test_listar_usuarios():
    # SetUp
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    ##
    usuarios = [Usuario(nome='Felipe'), Usuario(nome='Matheus')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    # Tear Down
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
    ##
