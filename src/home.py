import streamlit as st 
import time 
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

st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #0000;
        padding: 10px 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .header-container img {
        width: 100px;
          /* animation: blink 1.2s infinite; */
    }

    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }

    .header-title {
        text-align: center;
        flex-grow: 1;
        font-size: 2.5em;
        font-weight: bold;
        color: white;
    }
    </style>

    <div class="header-container">
        <img src="https://cdn.pixabay.com/animation/2024/04/09/09/56/09-56-25-230_512.gif" alt="bot-izq" />
        <div class="header-title">ValuBot</div>
        <img src="https://cdn.pixabay.com/animation/2023/01/07/11/02/11-02-30-972_512.gif" alt="bot-der" />
    </div>
    """,
    unsafe_allow_html=True
)

def main():

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

        st.subheader("Dime que tipo de vivienda quieres vender")
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

        if tipo_vivienda == "Apartamento" and niveles > 2:
            st.error("Los apartamentos no pueden tener más de 2 niveles.")
        else:
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
                escribir_mensaje(f"🧠 Pensando...", velocidad=0.08)
                time.sleep(1)
                escribir_mensaje(f"💰 El precio estimado de la 🏡propiedad es: ${precio_estimado:,.0f}", velocidad=0.08)
          
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
        estrato_opciones = estratos_por_sector.get(sector, [])
        estrato = st.selectbox("Estrato:", estrato_opciones, key="estrato_arriendo")

        if tipo_vivienda == "Apartamento" and niveles > 2:
            st.error("Los apartamentos no pueden tener más de 2 niveles.")
        else:
            if st.button("Enviar información de venta"):
                datos_usuario = pd.DataFrame([{
                        'tipo_vivienda': tipo_vivienda,
                        'niveles': niveles,
                        'tipo_contrato': arrendar,
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
                escribir_mensaje(f"🧠 Pensando...", velocidad=0.08)
                time.sleep(1)
                escribir_mensaje(f"💰 El precio estimado del arriendo de la 🏡propiedad es: ${precio_estimado:,.0f}", velocidad=0.08)

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

