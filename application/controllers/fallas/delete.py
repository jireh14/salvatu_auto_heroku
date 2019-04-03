import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_falla, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_falla) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_falla, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_falla) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_falla, **k):
        message = None # Error message
        id_falla = config.check_secure_val(str(id_falla)) # HMAC id_falla validate
        result = config.model.get_fallas(int(id_falla)) # search  id_falla
        result.id_falla = config.make_secure_val(str(result.id_falla)) # apply HMAC for id_falla
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_falla, **k):
        form = config.web.input() # get form data
        form['id_falla'] = config.check_secure_val(str(form['id_falla'])) # HMAC id_falla validate
        result = config.model.delete_fallas(form['id_falla']) # get fallas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_falla = config.check_secure_val(str(id_falla))  # HMAC user validate
            id_falla = config.check_secure_val(str(id_falla))  # HMAC user validate
            result = config.model.get_fallas(int(id_falla)) # get id_falla data
            result.id_falla = config.make_secure_val(str(result.id_falla)) # apply HMAC to id_falla
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/fallas') # render fallas delete.html 
