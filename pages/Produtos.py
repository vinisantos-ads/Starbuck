import streamlit as st
import pandas as pd

# Carregar o arquivo CSV
file_path = "starbucks.csv"
df = pd.read_csv(file_path)

# Título do aplicativo
st.title("Starbucks Products Information")

# Exibir tabela com os dados do CSV
st.write("## Tabela de Dados")
st.write(df)

# Sidebar para filtrar por categoria
categories = df['Beverage_category'].unique()
selected_category = st.sidebar.selectbox("Selecione uma categoria", categories)

# Filtrar dados com base na categoria selecionada
filtered_df = df[df['Beverage_category'] == selected_category]

# Exibir gráfico de barras para calorias
st.write("## Gráfico de Calorias por Bebida na Categoria Selecionada")
st.bar_chart(filtered_df[['Beverage', 'Calories']].set_index('Beverage'))

# Exibir informações específicas de uma bebida escolhida
selected_beverage = st.selectbox("Selecione uma bebida para mais informações", filtered_df['Beverage'])
selected_beverage_info = filtered_df[filtered_df['Beverage'] == selected_beverage].squeeze()

st.write("## Informações Detalhadas da Bebida Selecionada")
st.write(selected_beverage_info)