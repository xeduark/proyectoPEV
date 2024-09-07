import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración inicial
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Función para mostrar la página de login
def show_login():
    st.title('Página de Login')
    username = st.text_input('Nombre de usuario')
    password = st.text_input('Contraseña', type='password')

    if st.button('Iniciar sesión'):
        # Aquí puedes agregar lógica para verificar el nombre de usuario y la contraseña
        if username == 'usuario' and password == 'contraseña':  # Ejemplo de credenciales
            st.session_state.page = 'main'
        else:
            st.error('Nombre de usuario o contraseña incorrectos')

# Función para mostrar la página principal
def show_main():
    st.title('Explorador de Gráficos Interactivos')

    # Parámetros de entrada
    num_puntos = st.slider('Número de puntos de datos', 10, 1000, 100)
    tipo_grafico = st.selectbox('Tipo de gráfico', ['Líneas', 'Dispersión', 'Histograma'])

    # Generar datos aleatorios
    np.random.seed(0)
    datos = pd.DataFrame({
        'x': np.arange(num_puntos),
        'y': np.random.randn(num_puntos).cumsum()
    })

    # Crear gráfico basado en la selección del usuario
    fig, ax = plt.subplots()

    if tipo_grafico == 'Líneas':
        ax.plot(datos['x'], datos['y'], marker='o')
        ax.set_title('Gráfico de Líneas')
    elif tipo_grafico == 'Dispersión':
        ax.scatter(datos['x'], datos['y'])
        ax.set_title('Gráfico de Dispersión')
    elif tipo_grafico == 'Histograma':
        ax.hist(datos['y'], bins=30)
        ax.set_title('Histograma')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Mostrar gráfico en la aplicación
    st.pyplot(fig)

    # Mostrar algunos datos
    st.write('Datos generados:')
    st.dataframe(datos.head())

    # Botón para ir a la página de login
    if st.button('Ir a Login'):
        st.session_state.page = 'login'

# Navegación entre páginas
if st.session_state.page == 'login':
    show_login()
elif st.session_state.page == 'main':
    show_main()
