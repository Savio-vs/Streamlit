import streamlit as st
import pandas as pd
import numpy as np

'''
st.write("Tabela de Computadores do HQ")
list = pd.read_excel('HQ Computers.xlsx')

st.write(list)# leva a planilha para o navegador
              # de uma forma dinamica.

#st.dataframe(list.style.highlight_max(axis=0))

x = st.slider('x')  #  barra para o usuário interagir
st.write(x, 'squared is', x * x)

result = x ** (x/2)
st.write(x, '^' ,(x/2), '=' ,result)

'''

# >>> check box  
'Exibir mapa'
longitude = 0
latitude = 0
id = 0
# é criado caixas de seleção 
if st.checkbox('opção 1'):
    longitude = -10
    latitude = -50
    id = 1
if st.checkbox('opção 2'):
    longitude = -20
    latitude = -50
    id = 2
if st.checkbox('opção 3'):
    longitude = -20
    latitude = 120
    id =3 

# dependendo da caixa selecionada irá aparecer localizações diferentes no mapa.
if id == 1 :   # se a caixa for selecionada um mapa é impresso
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [1000, 100] + [longitude,latitude],
        columns=['lat', 'lon'])

    st.map(map_data) # imprimi na tela um mapa.
elif id == 2:
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [1000, 100] + [longitude,latitude],
        columns=['lat', 'lon'])

    st.map(map_data) # imprimi na tela um mapa.
elif id == 3:
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [1000, 100] + [longitude,latitude],
        columns=['lat', 'lon'])

    st.map(map_data) # imprimi na tela um mapa.
else:
    st.write("Caixa de seleção inativa")

# >>> caixa de seleção para várias opções

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
# criando uma caixa de seleção pegando uma coluna do
# dataframe acima como opções a serem selecionadas.
option = st.selectbox(
    'Which number do you like best?',
     df['first column']
)

second = st.selectbox(
    'Segundos?',
    df['second column']
)

'You selected: ', option # imprimi o texto e a variavel na tela.

'You selected second:', second

# >>> caixa de informações fixa na esquerda do video 
# adiciona uma caixa de seleção:
add_selectbox = st.sidebar.selectbox(
    'Qual a opção lhe representa melhor?',
    ('opção 1', 'opção 2', 'opção 3')
)

# adiciona uma barra movel de valores:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0
)
'mostrando o add_slider',add_slider


# >>> Alinhamento de obejtos

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))

if left_column.button('Press me!'):
    st.write(f"You are in {chosen} house!")

# Or even better, call Streamlit functions inside a "with" block:

    