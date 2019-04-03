import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_coche, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_coche) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_coche, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_coche) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_coche, **k):
        message = None # Error message
        id_coche = config.check_secure_val(str(id_coche)) # HMAC id_coche validate
        result = config.model.get_coche(int(id_coche)) # search for the id_coche
        result.id_coche = config.make_secure_val(str(result.id_coche)) # apply HMAC for id_coche
        return config.render.edit(result, message) # render coche edit.html

    @staticmethod
    def POST_EDIT(id_coche, **k):
        form = config.web.input()  # get form data
        form['id_coche'] = config.check_secure_val(str(form['id_coche'])) # HMAC id_coche validate
        # edit user with new data
        result = config.model.edit_coche(
            form['id_coche'],form['marca'],form['modelo'],form['anio'],
        )
        if result == None: # Error on udpate data
            id_coche = config.check_secure_val(str(id_coche)) # validate HMAC id_coche
            result = config.model.get_coche(int(id_coche)) # search for id_coche data
            result.id_coche = config.make_secure_val(str(result.id_coche)) # apply HMAC to id_coche
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/coche') # render coche index.html
