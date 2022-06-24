#!/usr/bin/env python3
import pandas as pd
#  import openpyxl

class Database():
    '''Handle the database'''
    def __init__(self):
        self.database_path = "db.xlsx"
        self.db = {}

    def read(self):
        '''Because there are multiple sheet, I need to for loop on every sheet'''
        try:
            xls = pd.ExcelFile(self.database_path)
            df = pd.DataFrame([])
            for sheet_name in xls.sheet_names:
                self.db["sheet_name"] = pd.read_excel(self.database_path, sheet_name=sheet_name)
        except FileNotFoundError:
            print(f"The file {self.database_path} wasn't found, create new")
            try:
                df_empty = pd.DataFrame([])
                with pd.ExcelWriter(self.database_path) as writer:
                    df_empty.to_excel(writer, sheet_name="main")  
            except Exception:
                raise

    def __str__(self):
