import requests


def buscar_avatar(usuario):
    """
    Busca avatar do usuario no github
    :param usuario: str com o nome do usuario no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    link = requests.get(url)
    return link.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('jr1os'))
    print(buscar_avatar('Al1rios'))
