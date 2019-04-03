import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_falla, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_falla) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_falla, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_falla) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_falla, **k):
        message = None # Error message
        id_falla = config.check_secure_val(str(id_falla)) # HMAC id_falla validate
        result = config.model.get_fallas(int(id_falla)) # search for the id_falla
        result.id_falla = config.make_secure_val(str(result.id_falla)) # apply HMAC for id_falla
        return config.render.edit(result, message) # render fallas edit.html

    @staticmethod
    def POST_EDIT(id_falla, **k):
        form = config.web.input()  # get form data
        form['id_falla'] = config.check_secure_val(str(form['id_falla'])) # HMAC id_falla validate
        # edit user with new data
        result = config.model.edit_fallas(
            form['id_falla'],form['codigo_falla'],form['descripcion'],form['causa'],form['imagen'],form['id_coche'],
        )
        if result == None: # Error on udpate data
            id_falla = config.check_secure_val(str(id_falla)) # validate HMAC id_falla
            result = config.model.get_fallas(int(id_falla)) # search for id_falla data
            result.id_falla = config.make_secure_val(str(result.id_falla)) # apply HMAC to id_falla
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/fallas') # render fallas index.html
