from email import header
import pandas as pd  

tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados.to_string())


# filtro 1 quiero tener todos los datos de los analistas 1
#tablaAnalistas1=tablaEmpleados[tablaEmpleados['cargo']=="analista1"].head(50)


#archivoHTML=tablaAnalistas1.to_html()
#archivoTEXTO=open("datosanalistas1.html","w")
#archivoTEXTO.write(archivoHTML)
#archivoTEXTO.close()


#tablaAnalistas2=tablaEmpleados[tablaEmpleados['cargo']=="analista2"].head(50)


#archivoHTML=tablaAnalistas2.to_html()
#archivoTEXTO=open("datosanalistas2.html","w")
#archivoTEXTO.write(archivoHTML)
#archivoTEXTO.close()

tablafiltro=tablaEmpleados[(tablaEmpleados['salario']>=5000000) & (tablaEmpleados['edad']<30)]
print(tablafiltro)

archivoHTML=tablafiltro.to_html()
archivoTEXTO=open("Datosfiltro.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()



