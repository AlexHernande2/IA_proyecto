import streamlit as st 



st.set_page_config(
    page_title="Streamly - An Intelligent Streamlit Assistant",
    page_icon="https://aunoa.ai/wp-content/uploads/2024/05/tipos-de-chatbots.webp",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={ 

    }
)
st.title("ChatBot")


def main():



    # Insert custom CSS for glowing effect
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

   
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSF-buRQZyR0ho0m8qS2XCmw_8QBnTZKqbYw&s"
    st.sidebar.markdown(
            f'<img src="{image_url}" class="cover-glow">',
            unsafe_allow_html=True
    )
    st.sidebar.markdown("---")



    st.sidebar.markdown("---")

    modo = st.sidebar.radio("Selecciona una opción:", ["Vender casa", "Arrendar casa"], index=0)
    if modo == "Vender casa":
        st.subheader("Dime que tipo de venta quieres")
        tipo_casa = st.selectbox("Tipo de propiedad:", ["Casa", "Apartamento", "Lote"])
        zona= st.selectbox("Ubicación", ["Norte","Sur", "Centro "])
        if st.button("Enviar información de venta"):
            st.success("Información de venta enviada correctamente.")
            st.write("**Resumen:**")
            st.write(f"- Tipo: {tipo_casa}")
            st.write(f"- Zona: {zona}")
            # st.write(f"- Precio: {precio}")



    st.sidebar.markdown("---")

    st.sidebar.markdown("""
        ### Basic Interactions
        - **Compra de casas**: Si quieres saber cuanto vale una s.
        - **No sé que poner**: No sé que poner.
        - **No sé que poner**: No sé que poner.
        """)


if __name__ == "__main__":
    main()

