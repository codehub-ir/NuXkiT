from settings import *
from os import system as sys
import sys as program
from platform import system
import getpass
import requests


cleaner = {'Windows': 'cls',
           'Linux': 'clear'}[system()]


def connected_to_internet(url=server_url, timeout=5):

    try:
        _ = requests.get(url, timeout=timeout)
        return 'OK'
    except requests.ConnectionError:
        pass
    return 'ERROR'


def main(logged_in=False, username='', token=''):

    sys(cleaner)
    print(nux.format(
        login_user=username if logged_in else '----',
        network_status=connected_to_internet(),))

    if logged_in:
        while True:
            command = oinput('')
            if command.startswith('exi'):
                program.exit()
                data = {
                    'printable': False,
                }
            elif command.startswith('hel'):
                data = {
                    'printable': True,
                    'data': help,
                }
            elif command.startswith('sni'):
                data = {
                    'printable': True,
                    'data': commander(snippet_url, token),
                }
            elif command.startswith('tea'):
                data = {
                    'printable': True,
                    'data': commander(team_url, token),
                }
            elif command.startswith('sug'):
                data = {
                    'printable': True,
                    'data': commander(suggest_url, token),
                }
            elif command.startswith('cle'):
                sys(cleaner)
                data = {
                    'printable': False,
                }
            elif command.startswith('logout'):
                main()

            if data['printable']:
                print(data['data'], end='\n\n')
                data = {
                    'printable': False,
                }

    else:
        username = oinput('Username')
        password = getpass.getpass(prompt=param('Password'), stream=None)

        login_status = login(username, password)
        if login_status:
            main(logged_in=True, username=username, token=login_status)
        else:
            main()


def login(username, password):

    try:
        r = requests.post(
            login_url, json={'username': username, 'password': password}).json()
        return r['key']
    except:
        return False


def commander(url, token):

    snippets = requests.get(url, headers={
                            'Authorization': 'token {}'.format(token)}).json()
    return snippets


if __name__ == '__main__':
    main()
