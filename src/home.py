import streamlit as st 
import time 

#prueba del modelo de Ml 

from pycaret.regression import load_model, predict_model
import pandas as pd

modelo = load_model('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/src/modeloB')

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
                0 0 5px #003300,
                0 0 10px #006600,
                0 0 15px #00cc00,
                0 0 20px #00ff00,
                0 0 25px #33ff33,
                0 0 30px #66ff66,
                0 0 35px #99ff99;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def escribir_mensaje(mensaje, velocidad=0.05):
        placeholder = st.empty()
        texto_mostrado = ""
        for letra in mensaje:
            texto_mostrado += letra
            placeholder.markdown(f"**{texto_mostrado}**")
            time.sleep(velocidad)

    #logo
    # image_url = "C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/imagenes/logo.jpg"
    # st.sidebar.markdown(
    #         f'<img src="{image_url}" class="cover-glow">',
    #         unsafe_allow_html=True
    # )
    st.sidebar.image("C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/imagenes/logo.jpg", use_container_width=True)

    st.sidebar.markdown("---")


    # Definir opciones de estrato según el sector
    estratos_por_sector = {
        "Norte": ["3", "4", "5", "6"],
        "Sur": ["1", "2", "3"],
        "Centro": ["2", "3", "4"]
    }
  
    st.sidebar.markdown("---")

    modo = st.sidebar.radio("Selecciona una opción:", ["Vender", "Arrendar"], index=0)
    if modo == "Vender":
        #prueba para lo de cpatura de datos del dataframe
        venta= "Venta"

        st.subheader("Dime que tipo de venta quieres")
        tipo_vivienda = st.selectbox("Tipo de propiedad:", ["Casa", "Apartamento"])
        niveles = st.number_input("Ingrese los niveles", min_value=1, step=1, max_value=4, format="%d")
        estado = st.selectbox(f"Estado de {tipo_vivienda} ", ["Nuevo", "Casi nuevo"])
        num_habitaciones = st.number_input("Ingrese el número de habitaciones", min_value=1, step=1, max_value=4, format="%d")
        num_banos = st.number_input("Ingrese el número de Baños", min_value=1, step=1, max_value=3, format="%d")
        area_construida= st.number_input("Ingrese los metros del area constuida", min_value=50, step=150, max_value=300, format="%d")
        parqueadero = st.selectbox("Parqueadero:", ["Si", "No"])
        sector = st.selectbox("Sector:", ["Norte", "Sur", "Centro"], key="sector_venta")
        estrato_opciones = estratos_por_sector.get(sector, [])
        estrato = st.selectbox("Estrato:", estrato_opciones, key="estrato_venta")

        

        if st.button("Enviar información de venta"):
            datos_usuario = pd.DataFrame([{
                    'tipo_vivienda': tipo_vivienda,
                    'niveles': niveles,
                    'tipo_contrato': venta,
                    'area_construida': area_construida,
                    'estado': estado,
                    'num_habitaciones': num_habitaciones,
                    'num_banos': num_banos,
                    'parqueadero': parqueadero,
                    'sector': sector,
                    'estrato': estrato
                }])

            print(datos_usuario)

            resultado = predict_model(modelo, data=datos_usuario)
            precio_estimado = resultado['prediction_label'][0]
            # st.success(f"El precio estimado de la propiedad es: ${precio_estimado:,.0f}")
            # st.success("Información de venta enviada correctamente.")
            escribir_mensaje(f"🎮 Pensando...", velocidad=0.08)
            time.sleep(1)
            escribir_mensaje(f"🍄 El precio estimado de la propiedad es: ${precio_estimado:,.0f}", velocidad=0.08)

  
         
            # st.write(f"- Precio: {precio}")
    else:
        arrendar= "Arrendar"
        st.subheader("Dime que tipo de vivienda quieres arrendar")
        tipo_vivienda = st.selectbox("Tipo de propiedad:", ["Casa", "Apartamento"])
        niveles = st.number_input("Ingrese los niveles", min_value=1, step=1, max_value=4, format="%d")
        estado = st.selectbox(f"Estado de {tipo_vivienda} ", ["Nuevo", "Casi nuevo"])
        num_habitaciones = st.number_input("Ingrese el número de habitaciones", min_value=1, step=1, max_value=4, format="%d")
        num_banos = st.number_input("Ingrese el número de Baños", min_value=1, step=1, max_value=3, format="%d")
        area_construida= st.number_input("Ingrese los metros del area constuida", min_value=50, step=150, max_value=300, format="%d")
        parqueadero = st.selectbox("Parqueadero:", ["Si", "No"])
        sector = st.selectbox("Sector:", ["Norte", "Sur", "Centro"], key="sector_arriendo")
        estrato = st.selectbox("Estrato:", ["1", "2", "3", "4", "5", "6"], key="estrato_arriendo")


        if st.button("Enviar información de venta"):
            datos_usuario = pd.DataFrame([{
                    'tipo_vivienda': tipo_vivienda,
                    'niveles': niveles,
                    'tipo_contrato': venta,
                    'area_construida': area_construida,
                    'estado': estado,
                    'num_habitaciones': num_habitaciones,
                    'num_banos': num_banos,
                    'parqueadero': parqueadero,
                    'sector': sector,
                    'estrato': estrato
                }])
            print(datos_usuario)
            resultado = predict_model(modelo, data=datos_usuario)
            precio_estimado = resultado['prediction_label'][0]
            st.success(f"Podría arrendar esta propiedad en : ${precio_estimado:,.0f}")
            st.success("Información de venta enviada correctamente.")
  
        print("Hola prueba")

 
    st.sidebar.markdown("---")

    st.sidebar.markdown("""
        ### Instrucciones Básicas
        - Selecciona una opción: Elige si deseas vender o arrendar una propiedad.
        - Completa el formulario: Ingresa los datos de la propiedad como tipo, niveles, habitaciones, baños, etc.
                        
        - Haz clic en "Enviar información": El sistema usará IA para estimar el valor de venta o arriendo.             
        - Revisa la predicción: Aparecerá una estimación basada en tus datos.


        """)


if __name__ == "__main__":
    main()

