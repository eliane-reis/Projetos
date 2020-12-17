import streamlit as st
import pandas as pd

alimentos = pd.read_csv('alimentos.csv')
description = alimentos['description'].unique()

st.title('Athetic Fit')

st.title('Um pouco sobre voce:')

Idade = st.selectbox('Qual e a sua idade?', ['f', 'm'])

Peso = st.selectbox('Qual e o seu peso?', ['f', 'm'])

Altura = st.selectbox('Qual e a sua altura?', ['f', 'm'])

Sexo = st.selectbox('Qual e o seu sexo?', ['F', 'M'])

st.title('Como voce se alimentou hoje ?')

options = st.multiselect('Selecione seus alimentos:', description)

st.write('You selected:', options)

st.title('Ops, calorias sobrando ... ')

Calorias = st.selectbox('Calorias',['x', 'y'])

st.title('Calma, vamos dar uma forcinha !!!')

Atividade = st.selectbox('Atividade',['Correr', 'Andar de bicicleta', 'nadar'])
