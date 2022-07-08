#!/usr/bin/env python3
import pandas as pd
from src.database_handler import Database



def test_database_read_db():
    db = Database()
    df = db.read()
    print("this is the df:", df)
