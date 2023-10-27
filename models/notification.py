from sqlalchemy import Column, Table,Sequence
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
id_sequence = Sequence('notification_id_seq', metadata=meta)

notifications = Table(
    "notification",
    meta,
    Column("id",Integer, id_sequence, primary_key=True, server_default=id_sequence.next_value()),
    Column("fecha",String(50)),    
    Column("asunto",String(50)),
    Column("message",String(50)),
    Column("email",String(50))
)

meta.create_all(engine)