import sqlalchemy as db
print(1)

engine = db.create_engine('mysql+pymysql://root:////@localhost/MyData')

connection = engine.connect()
metadata = db.MetaData()
table = db.Table('language', metadata, autoload=True, autoload_with=engine)

print(table.columns.keys())
print(1)