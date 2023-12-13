import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import MarkerCluster

# Carrega os dados do arquivo CSV
@st.cache
def load_data():
    df = pd.read_csv('directory.csv')
    return df

# Filtra os dados para mostrar apenas os locais do Starbucks
def filter_starbucks(df):
    starbucks_df = df[df['Brand'] == 'Starbucks']
    return starbucks_df

# Cria um mapa interativo usando o Folium
def create_map(df):
    st.title('Starbucks Locations Worldwide')

    # Encontra a localização central para inicializar o mapa
    geolocator = Nominatim(user_agent="starbucks_locator")
    location = geolocator.geocode("United States")
    center_map = [location.latitude, location.longitude]

    # Cria um mapa Folium centrado na localização central
    my_map = folium.Map(location=center_map, zoom_start=3)
    marker_cluster = MarkerCluster().add_to(my_map)

    # Adiciona marcadores para cada local do Starbucks
    for index, row in df.iterrows():
        if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
            folium.Marker([row['Latitude'], row['Longitude']], popup=row['Store Name']).add_to(marker_cluster)

    # Exibe o mapa usando o Streamlit
    st.write(my_map)

def main():
    st.set_page_config(page_title='Starbucks Locator', page_icon='☕')

    st.sidebar.title('Filtros')
    # Carrega os dados
    data = load_data()

    # Filtra os locais do Starbucks
    starbucks_data = filter_starbucks(data)

    # Exibe os dados filtrados
    st.write(f"Total de locais do Starbucks: {starbucks_data.shape[0]}")
    st.dataframe(starbucks_data)

    # Cria e exibe o mapa
    create_map(starbucks_data)

if __name__ == '__main__':
    main()