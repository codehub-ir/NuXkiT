class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'

nux = """
          ___             ___     
         /\__\           /__/|    
        /::|  |         |  |:|    
       /:|:|  |         |  |:|    
      /:/|:|  |__     __|  |:|    
     /:/ |:| /\__\   /__/\_|:|____
     \/__|:|/:/  /   \  \:\/:::::/
         |:/:/  /     \  \::/~~~~ 
         |::/  /       \  \:\     
         /:/  /         \  \:\    
         \/__/           \__\/    
                              
  >> F E A T U R E D  C O D E H U B <<

_
 |- Login %s{login_user:s}%s
 |- Network %s{network_status:s}%s
⎻""" % (colors.bold, colors.end,
        colors.bold, colors.end)

login_url = 'http://codehub.pythonanywhere.com/api/v1/admin/login/'
logout_url = 'http://codehub.pythonanywhere.com/api/v1/admin/logout/'

snippet_url = 'http://codehub.pythonanywhere.com/api/v1/admin/snippet/'
team_url = 'http://codehub.pythonanywhere.com/api/v1/admin/team/'
suggest = 'http://codehub.pythonanywhere.com/api/v1/admin/suggest/'

server_url = 'http://codehub.pythonanywhere.com/'