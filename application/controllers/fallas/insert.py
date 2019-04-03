import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_INSERT():
        return config.render.insert() # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input() # get form data

        # call model insert_fallas and try to insert new data
        config.model.insert_fallas(
            form['codigo_falla'],form['descripcion'],form['causa'],form['imagen'],form['id_coche'],
        )
        raise config.web.seeother('/fallas') # render fallas index.html
