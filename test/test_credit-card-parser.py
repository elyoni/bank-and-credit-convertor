#!/usr/bin/env python3
import pandas as pd
from lib.credit_card_handler import CreditCardMaxXlsxParser
def test_credit_card_parser():
    df = CreditCardMaxXlsxParser.xlsx("test/max-credit-card_test.xlsx")
    print("\n",df)


