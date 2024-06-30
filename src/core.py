import pandas as pd
import os


import excel_handler as exc_h

excel_file = "balance.xlsx"
file_path = f"C:/Users/Usuario/Desktop/Finance App Project/wealth_management/files/{excel_file}"


#==================== PROGRAMA PRINCIPAL ====================

wealth_file = exc_h.read_excel(file_path)


