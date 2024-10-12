from flask import g #"g" is a context object. "global" context objecrt.
import sqlite3


DB_URI = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:              #if db == None
        db = g._database = sqlite3.connect(DB_URI)
    return db