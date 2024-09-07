import streamlit as st

# Configuración inicial
if 'page' not in st.session_state:
    st.session_state.page = 'login'

# Función para mostrar la página de login
def show_login():
    st.title('Página de Login')
    username = st.text_input('Nombre de usuario')
    password = st.text_input('Contraseña', type='password')

    if st.button('Iniciar sesión'):
        
        if username == 'usuario' and password == 'contraseña':  # Ejemplo de credenciales
            st.session_state.page = 'main'
        else:
            st.error('Nombre de usuario o contraseña incorrectos')

# Función para mostrar la página principal
def show_main():
    st.title('Página Principal')
    st.write('Bienvenido a la página principal.')
    if st.button('Cerrar sesión'):
        st.session_state.page = 'login'

# Navegación entre páginas
if st.session_state.page == 'login':
    show_login()
elif st.session_state.page == 'main':
    show_main()
