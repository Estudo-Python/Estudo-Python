import requests


def buscar_avatar(usuario):
    """Busca o avatar de um usuário no GitHub

    :param usuario: str com nome de usuário no github
    :return: str com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    response = requests.get(url)
    return response.json()['avatar_url']
