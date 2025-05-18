import streamlit as st 

#prueba del modelo de Ml 

from pycaret.regression import load_model, predict_model
import pandas as pd

modelo = load_model('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/src/modelo_gbr')

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
    st.markdown("""
        <style>
        div[data-baseweb="select"] {
            box-shadow: 
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        /* Aplica a todos los number_input */
        input[type="number"] {
            box-shadow:
                0 0 5px #330000,
                0 0 10px #660000,
                0 0 15px #990000,
                0 0 20px #CC0000,
                0 0 25px #FF0000,
                0 0 30px #FF3333,
                0 0 35px #FF6666;
            border-radius: 10px;
            padding: 5px;
        }
        </style>
    """, unsafe_allow_html=True)


   
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSF-buRQZyR0ho0m8qS2XCmw_8QBnTZKqbYw&s"
    st.sidebar.markdown(
            f'<img src="{image_url}" class="cover-glow">',
            unsafe_allow_html=True
    )
    st.sidebar.markdown("---")



    st.sidebar.markdown("---")

    modo = st.sidebar.radio("Selecciona una opción:", ["Vender", "Arrendar "], index=0)
    if modo == "Vender casa":
        #prueba para lo de cpatura de datos del dataframe
        venta= "Venta"

        st.subheader("Dime que tipo de venta quieres")
        tipo_vivienda = st.selectbox("Tipo de propiedad:", ["Casa", "Apartamento"])
        niveles = st.number_input("Ingrese los niveles", min_value=1, step=1, max_value=4, format="%d")
        estado = st.selectbox(f"Estado de {tipo_vivienda} ", ["Nuevo", "Casi nuevo"])
        num_habitaciones = st.number_input("Ingrese el número de habitaciones", min_value=1, step=1, max_value=4, format="%d")
        num_banos = st.number_input("Ingrese el número de Baños", min_value=1, step=1, max_value=3, format="%d")
        area_construida= st.number_input("Ingrese los metros del area constuida", min_value=150, step=150, max_value=280, format="%d")
        parqueadero = st.selectbox("Parqueadero:", ["Si", "No"])
        sector= st.selectbox("Sector:", ["Norte", "Sur", "Centro"])
        estrato = st.selectbox("Estrato:", ["1","2", "3","4", "5", "6"])
        

        if st.button("Enviar información de venta"):
            datos_usuario = pd.DataFrame([{
                    'tipo_vivienda': tipo_vivienda,
                    'niveles': niveles,
                    'tipo_contrato': venta,
                    'estado': estado,
                    'num_habitaciones': num_habitaciones,
                    'num_banos': num_banos,
                    'area_construida': area_construida,
                    'parqueadero': parqueadero,
                    'sector': sector,
                    'estrato': estrato
                }])


            resultado = predict_model(modelo, data=datos_usuario)
            precio_estimado = resultado['prediction_label'][0]
            st.success(f"El precio estimado de la propiedad es: ${precio_estimado:,.0f}")
            st.success("Información dme venta enviada correctamente.")
            st.write("**Resumen:**")
            st.write(f"- Tipo: {tipo_vivienda}")
         
            # st.write(f"- Precio: {precio}")
    else:
        venta= "Arrendar"

        st.subheader("Dime que tipo de venta quieres")
        tipo_vivienda = st.selectbox("Tipo de propiedad:", ["Casa", "Apartamento"])
        niveles = st.number_input("Ingrese los niveles", min_value=1, step=1, max_value=4, format="%d")
        estado = st.selectbox(f"Estado de {tipo_vivienda} ", ["Nuevo", "Casi nuevo"])
        num_habitaciones = st.number_input("Ingrese el número de habitaciones", min_value=1, step=1, max_value=4, format="%d")
        num_banos = st.number_input("Ingrese el número de Baños", min_value=1, step=1, max_value=3, format="%d")
        area_construida= st.number_input("Ingrese los metros del area constuida", min_value=150, step=150, max_value=280, format="%d")
        parqueadero = st.selectbox("Parqueadero:", ["Si", "No"])
        sector= st.selectbox("Sector:", ["Norte", "Sur", "Centro"])
        estrato = st.selectbox("Estrato:", ["1","2", "3","4", "5", "6"])
        

 
    st.sidebar.markdown("---")

    st.sidebar.markdown("""
        ### Basic Interactions
        - **Compra de casas**: Si quieres saber cuanto vale una s.
        - **No sé que poner**: No sé que poner.
        - **No sé que poner**: No sé que ponem.
        """)


if __name__ == "__main__":
    main()

