import pandas as pd
import os
import xlsxwriter


def read_excel(file_path):
    #Llama a checkear que exista el archivo antes de abrirlo. Si no es así
    # lo crea y ahí si va a poder leerlo y retornarlo.
    check_and_create_file(file_path)
    return pd.read_excel(file_path)
    

def initialize_excel(df, file_path):
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    try:
        # Crea un ExcelWriter
        with pd.ExcelWriter(file_path) as writer:
            # Escribe cada DataFrame en una hoja diferente
            df.to_excel(writer, sheet_name='Gastos', index=False)
            df1.to_excel(writer, sheet_name='Ahorros e inversiones', index=False)
            df2.to_excel(writer, sheet_name='Objetivos', index=False)
    except Exception as e:
        print(e)
    
    
    
def check_and_create_file(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame()        
        initialize_excel(df, file_path)
        print(f"Archivo creado en {file_path}")
        return df
    else:
        print(f"El archivo ya existe en {file_path}")
        return 0