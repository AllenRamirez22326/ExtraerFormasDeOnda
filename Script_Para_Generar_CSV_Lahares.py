import pandas as pd
from datetime import datetime, timedelta

# Archivo de entrada y salida
archivo_entrada = 'CatalogoLaharesSTG10HHZSwarm.csv'
archivo_salida = 'lahar_filtrado.csv'

intervalo=2 #Número de horas a considerar

# Leer archivo como una sola columna
df = pd.read_csv(archivo_entrada, header=None,names=["Fecha", "Estacion", "Evento"])

#print(df)
for i in range(len(df)):
    if df.loc[i,"Evento"]=="Noise":
        fecha1=df.loc[i-1,"Fecha"]
        fecha2=datetime.strptime(fecha1, "%Y-%m-%d %H:%M:%S")+timedelta(hours=intervalo)
        df.at[i,"Fecha"]=fecha2
df.to_csv("Lahar_FiltradoV.csv",index=False) #Genera CSV para descargar los mseed

training_events = pd.DataFrame(columns=["Estacion", "Fecha_inicial", "Fecha_final"])

for i in range(0, len(df), 2):
    estacion = df.loc[i, "Estacion"]
    fecha_inicial = df.loc[i, "Fecha"]
    fecha_final = df.loc[i + 1, "Fecha"]
    training_events.loc[len(training_events)] = [estacion, fecha_inicial, fecha_final]

# Guardar sin encabezados ni índice
training_events.to_csv("training_events.txt", header=False, index=False)


