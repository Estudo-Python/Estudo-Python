from unittest.mock import Mock

from core import github_api


def teste_buscar_avatar():
    resp_mock = Mock()
    github_api.requests.get = Mock(return_value=resp_mock)  # Isolando .get de requests
    resp_mock.json.return_value = {'avatar_url': 'https://avatars.githubusercontent.com/u/62901711?v=4'}

    url = github_api.buscar_avatar('felipeno')
    assert 'https://avatars.githubusercontent.com/u/62901711?v=4' == url