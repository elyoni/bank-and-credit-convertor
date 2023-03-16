#!/usr/bin/env python3
import pandas as pd
#  import openpyxl

class Database():
    '''Handle the database'''
    def __init__(self):
        self.database_path = "db.xlsx"
        self.main_db = None
        self.bank_history = None

    def read_main_db(self):
        # TODO: Add verification if 'Main' sheet exists
        self.main_db = pd.read_excel(self.database_path, sheet_name="Main")
        print(self.main_db)

    def read_bank_history(self):
            #  for sheet_name in xls.sheet_names:
        # TODO: Add verification if 'Total' sheet exists
        bank_history_sheet = pd.read_excel(self.database_path, sheet_name="BankHistory", index_col=0)
        print("\n", bank_history_sheet.index)
        #  print("Amount", bank_history_sheet["Amount"].iat[0])
        #  self.bank_history = bank_history_sheet["Date"].iat[0]

    def add_new_bank_data(self, bank_data):
        pass

    def add_new_creditcard_data(self, bank_data):
        pass

    def read(self):
        '''I am reading only the first two sheets, the Main and Total'''
        # TODO: Add verification if the database file exists if not create new one
        try:
            self.read_main_db()
            self.read_bank_history()
        except FileNotFoundError:
            print(f"The file {self.database_path} wasn't found, create new")
            try:
                df_empty = pd.DataFrame([])
                with pd.ExcelWriter(self.database_path) as writer:
                    df_empty.to_excel(writer, sheet_name="main")  
            except Exception:
                raise

    #  def __str__(self):
