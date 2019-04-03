import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_coche, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_coche) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_coche, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_coche) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_coche, **k):
        message = None # Error message
        id_coche = config.check_secure_val(str(id_coche)) # HMAC id_coche validate
        result = config.model.get_coche(int(id_coche)) # search  id_coche
        result.id_coche = config.make_secure_val(str(result.id_coche)) # apply HMAC for id_coche
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_coche, **k):
        form = config.web.input() # get form data
        form['id_coche'] = config.check_secure_val(str(form['id_coche'])) # HMAC id_coche validate
        result = config.model.delete_coche(form['id_coche']) # get coche data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_coche = config.check_secure_val(str(id_coche))  # HMAC user validate
            id_coche = config.check_secure_val(str(id_coche))  # HMAC user validate
            result = config.model.get_coche(int(id_coche)) # get id_coche data
            result.id_coche = config.make_secure_val(str(result.id_coche)) # apply HMAC to id_coche
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/coche') # render coche delete.html 
