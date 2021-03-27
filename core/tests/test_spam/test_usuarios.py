from core.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Felipe', email='felipematheus.ns0@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Felipe', email='felipematheus.ns0@gmail.com'),
        Usuario(nome='Matheus', email='fe_matheus@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

