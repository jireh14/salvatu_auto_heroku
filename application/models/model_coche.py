import web
import config

db = config.db


def get_all_coche():
    try:
        return db.select('coche')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_coche(id_coche):
    try:
        return db.select('coche', where='id_coche=$id_coche', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_coche(id_coche):
    try:
        return db.delete('coche', where='id_coche=$id_coche', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_coche(marca,modelo,anio):
    try:
        return db.insert('coche',marca=marca,
modelo=modelo,
anio=anio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_coche(id_coche,marca,modelo,anio):
    try:
        return db.update('coche',id_coche=id_coche,
marca=marca,
modelo=modelo,
anio=anio,
                  where='id_coche=$id_coche',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
