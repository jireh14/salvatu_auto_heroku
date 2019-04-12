import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model.get_all_fallas().list() # get fallas table list
        for row in result:
            row.codigo_falla = config.make_secure_val(str(row.codigo_falla)) 
        print result# apply HMAC to id_falla (primary key)
        return config.render.index(result) # render fallas index.html
