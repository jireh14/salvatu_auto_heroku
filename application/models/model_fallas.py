import web
import config

db = config.db


def get_all_fallas():
    try:
        return db.select('fallas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_fallas(id_falla):
    try:
        return db.select('fallas', where='id_falla=$id_falla', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_fallas(id_falla):
    try:
        return db.delete('fallas', where='id_falla=$id_falla', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_fallas(codigo_falla,descripcion,causa,imagen,id_coche):
    try:
        return db.insert('fallas',codigo_falla=codigo_falla,
descripcion=descripcion,
causa=causa,
imagen=imagen,
id_coche=id_coche)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_fallas(id_falla,codigo_falla,descripcion,causa,imagen,id_coche):
    try:
        return db.update('fallas',id_falla=id_falla,
codigo_falla=codigo_falla,
descripcion=descripcion,
causa=causa,
imagen=imagen,
id_coche=id_coche,
                  where='id_falla=$id_falla',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
