import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no GitHub
    :param usuario: str com nome de usuário no github
    :return: str com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    response = requests.get(url).json()
    return response['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('felipeno'))
