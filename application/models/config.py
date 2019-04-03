import web

db_host = 'localhost'
db_name = 'salva'
db_user = 'salva'
db_pw = 'salva.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )