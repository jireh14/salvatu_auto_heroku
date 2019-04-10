import web

db_host = 'localhost'
db_name = 'salva'
db_user = 'salva'
db_pw = 'salva.2019'
'''
db_host = 'bqmayq5x95g1sgr9.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'sg7ffsy17wro9gze'
db_user = 'pbcuzizlwoprp2rq'
db_pw = 'kmxqle54xdy723d4'
'''
db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )