import pytest

from unittest.mock import Mock
from core import github_api


@pytest.fixture()
def avatar_url(mocker):
    resp_mock = Mock()

    get_mock = mocker.patch('core.github_api.requests.get')
    get_mock.return_value = resp_mock

    url = 'https://avatars.githubusercontent.com/u/62901711?v=4'
    resp_mock.json.return_value = {'avatar_url': url}

    return url


def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('felipeno')
    assert 'https://avatars.githubusercontent.com/u/62901711?v=4' == url


def teste_integracao_buscar_avatar():
    url = github_api.buscar_avatar('felipeno-ambev')
    assert 'https://avatars.githubusercontent.com/u/79462474?v=4' == url
