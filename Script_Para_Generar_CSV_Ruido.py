import pandas as pd
from datetime import datetime, timedelta

# Archivo de entrada y salida
archivo_entrada = 'CatalogoRecortadoDeSwarmDelRuido.csv'
archivo_salida = 'Ruido_filtrado.csv'
intervalo=3

# Leer archivo como una sola columna
df = pd.read_csv(archivo_entrada, header=None,names=["Fecha", "Estacion", "Evento"])
print(df)
for i in range(len(df)):
    if df.loc[i,"Evento"]=="Cultural":
        fecha1=df.loc[i-1,"Fecha"]
        fecha2=datetime.strptime(fecha1, "%Y-%m-%d %H:%M:%S")+timedelta(hours=intervalo)
        df.at[i,"Fecha"]=fecha2
df.to_csv("Ruido_Filtrado.csv",index=False) #Genera CSV para descargar los mseed
#Guardar el CSV de ruido
noise = pd.DataFrame(columns=["Estacion", "Fecha_inicial", "Evento"])

for i in range(0, len(df), 2):
    estacion = df.loc[i, "Estacion"]
    fecha_inicial = df.loc[i, "Fecha"]
    Evento= "eq"
    noise.loc[len(noise)] = [estacion, fecha_inicial, Evento]

# Guardar sin encabezados ni índice
noise.to_csv("noise.txt", header=False, index=False)

