import folium
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import pandas as pd

st.title("Centros Deportivos Juegos Olimpicos París 2024")

# Cargar los datos
df = pd.read_csv("paris-2024-sites-de-competition.csv", sep=";")

# Texto de introducción
stream = """Les presento esta interfaz donde pueden encontrar las ubicaciones y eventos de los centros deportivos de los 
los juegos olimpicos París 2024!🥇
Bienvenidos.
"""  

st.write(stream)

# Filtro principal por categoría
st.header("Selecciona la categoría que deseas visualizar")
categories = df['category_id'].unique()
selected_category = st.selectbox("Selecciona si deseas olimpicos o paralimpicos", categories)

# Filtrar el DataFrame por la categoría seleccionada
df_filtered = df[df["category_id"] == selected_category]
df_filtered.latitude = df_filtered.latitude.astype(str).str.replace(',', ".")
df_filtered.longitude = df_filtered.longitude.astype(str).str.replace(',', ".")
df_filtered.latitude = pd.to_numeric(df_filtered.latitude)
df_filtered.longitude = pd.to_numeric(df_filtered.longitude)


# Filtro por deporte basado en la categoría seleccionada
st.header("Selecciona la sede por deporte")
sports = df_filtered['Sports'].unique()
selected_sport = st.selectbox("Selecciona por deporte", sports)

df_filtered_by_sport = df_filtered[df_filtered["Sports"] == selected_sport]
st.write(df_filtered_by_sport[["Nom_Site", "start_date", "end_date"]])

# Filtro por fecha de inicio basado en la categoría
st.header("Selecciona las sedes por fecha de inicio")
start_dates = df_filtered['start_date'].unique()
selected_date = st.selectbox("Selecciona por fecha de inicio", start_dates)

df_filtered_by_date = df_filtered[df_filtered["start_date"] == selected_date]
st.write(df_filtered_by_date[["Nom_Site", "Sports", "end_date"]])

# Mostrar los puntos en el mapa

st.header("Mapa de Sedes Deportivas")
map_ = folium.Map(location=[df_filtered["latitude"].mean(), df_filtered["longitude"].mean()], zoom_start=6)

marker_cluster = MarkerCluster().add_to(map_)
for _, row in df_filtered.iterrows():
        folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=f"{row['Nom_Site']} - {row['Sports']}",
        ).add_to(marker_cluster)
            
st_folium(map_, width=700, height=450)  
        
        
        
   
    