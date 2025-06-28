from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd
client = Client("http://172.20.11.35:8080")
#El formato del CSV tiene que tener como primera fila "Fecha,Estacion,Evento"
df=pd.read_csv("C:/Users/Allen/OneDrive/Desktop/Universidad2025/ModeloEntrenadoSantiaguito/Lahar_FiltradoV.csv")
estacion=df["Estacion"].str.split(expand=True)
estacion.columns=["EstacionVolcan","Banda","Servidor","Localizacion"]
df=pd.concat([df,estacion],axis=1)

for i in range (len(df)):
    if (df.at[i,"Evento"]=="Lahar"):
        ti=UTCDateTime(df.at[i, "Fecha"])
    elif (df.at[i,"Evento"]=="Noise"):
        tf=UTCDateTime(df.at[i, "Fecha"])
        st = client.get_waveforms("GI", df.at[i,"EstacionVolcan"], df.at[i,"Localizacion"], df.at[i,"Banda"], ti, tf)
        network = "GI"
        station = df.at[i, "EstacionVolcan"]
        location = df.at[i, "Localizacion"]
        channel = df.at[i, "Banda"]
        filename = f"{network}.{station}.{location}.{channel}.{ti.year}.{ti.julday:03d}.mseed"
        st.write(filename, format="MSEED")

    