#!/usr/bin/env python3
from src.bank_handler import BankLeumiXlsxParser

def main():
    df = BankLeumiXlsxParser.xlsx("test/leumi_bank_test.xlsx")

