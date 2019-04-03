import web
import config
import json


class Api_coche:
    def get(self, id_coche):
        try:
            # http://localhost:8080/api_coche?user_hash=12345&action=get
            if id_coche is None:
                result = config.model.get_all_coche()
                coche_json = []
                for row in result:
                    tmp = dict(row)
                    coche_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(coche_json)
            else:
                # http://0.0.0.0:8080/api_coche?user_hash=12345&action=get&id_coche=1
                result = config.model.get_coche(int(id_coche))
                coche_json = []
                coche_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(coche_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            coche_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(coche_json)

# http://0.0.0.0:8080/api_coche?user_hash=12345&action=put&id_coche=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, marca,modelo,anio):
        try:
            config.model.insert_coche(marca,modelo,anio)
            coche_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(coche_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_coche?user_hash=12345&action=delete&id_coche=1
    def delete(self, id_coche):
        try:
            config.model.delete_coche(id_coche)
            coche_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(coche_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_coche?user_hash=12345&action=update&id_coche=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_coche, marca,modelo,anio):
        try:
            config.model.edit_coche(id_coche,marca,modelo,anio)
            coche_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(coche_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            coche_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(coche_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_coche=None,
            marca=None,
            modelo=None,
            anio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_coche=user_data.id_coche

            marca=user_data.marca

            modelo=user_data.modelo

            anio=user_data.anio

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_coche)
                elif action == 'put':
                    return self.put(marca,modelo,anio)
                elif action == 'delete':
                    return self.delete(id_coche)
                elif action == 'update':
                    return self.update(id_coche, marca,modelo,anio)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
