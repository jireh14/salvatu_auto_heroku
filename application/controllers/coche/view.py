import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    def GET(self, id_coche):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_coche) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_coche):
        id_coche = config.check_secure_val(str(id_coche)) # HMAC id_coche validate
        result = config.model.get_coche(id_coche) # search for the id_coche data
        return config.render.view(result) # render view.html with id_coche data
