import pandas as pd
import excel_handler as exc_h



#excel_file = "balance.xlsx"
#file_path = f"C:/Users/Usuario/Desktop/Finance App Project/wealth_management/files/{excel_file}"


#==================== PROGRAMA PRINCIPAL ====================


wealth_file = exc_h.read_excel()
data_to_write = {
    "Gastos": [1, 2, 3, 4, 5]  #Datos a añadir a una columna específica
}
df = pd.DataFrame(data_to_write)

#Acá según lo que vaya ingresando voy a agregar info en esa determinada hoja
sheet = 'Gastos'
exc_h.write_excel(df, sheet)
