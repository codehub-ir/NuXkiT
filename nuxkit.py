from settings import *
from os import system as sys
from platform import system
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


def main(logged_in=False, username=''):

    sys(cleaner)
    print(nux.format(
        login_user=username if logged_in else '----',
        network_status=connected_to_internet(),))


if __name__ == '__main__':
    main()
