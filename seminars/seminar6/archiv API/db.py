import databases
import sqlalchemy
from settings import settings

db = databases.Database(settings.DATABASE_URL)
mdt = sqlalchemy.MetaData()
users_db = sqlalchemy.Table( "users", mdt,
                        sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
                        sqlalchemy.Column("login", sqlalchemy.String(32)),
                        sqlalchemy.Column("password", sqlalchemy.String(64)),
                        sqlalchemy.Column("email", sqlalchemy.String(128)),
                        )

posts_db = sqlalchemy.Table( "posts", mdt,
                        sqlalchemy.Column("id", sqlalchemy.Integer,primary_key=True),
                        sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'),
                                          nullable=False),
                        sqlalchemy.Column("post", sqlalchemy.String(1000)),
                        )

engine = sqlalchemy.create_engine(settings.DATABASE_URL,connect_args={"check_same_thread": False})
mdt.create_all(engine)


