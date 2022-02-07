#!/usr/bin/env python3
import pandas as pd
from lib.database_handler import Database



def test_database_read_db():
    db = Database()
    df = db.read_db()
    print(df)
