from settings import *
from os import system as sys
from platform import system


cleaner = {'Windows': 'cls',
           'Linux': 'clear'}[system()]


sys(cleaner)
print(nux.format(
                    login_user="----",
                    network_status=internet_on(),))