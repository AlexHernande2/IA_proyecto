# IA_proyecto
# ValuBot – Chatbot de Predicción de Precios
ValuBot es un chatbot inteligente que predice el valor de un inmueble o arriendo usando técnicas de Machine Learning. Utiliza PyCaret para entrenar un modelo de regresión y responder de forma interactiva a preguntas del usuario.

# Requisitos
## Antes de ejecutar el proyecto, asegúrate de tener Python instalado
## Antes de ejecutar el chatbot, asegúrate de tener instaladas las siguientes librerías:
pandas, pycaret y streamlit
# El modelo se entrena con un archivo .csv llamado DatosFinales.csv. Asegúrate de tenerlo disponible en la siguiente ruta:
C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/DatosFinales.csv
# Nota: Modificar la ruta al archivo CSV en el código.
# Eliminar el archivo modeloB.pkl ya que cuando inicialice la clase ia.iynb este lo creara
# Inicialización del Modelo
Antes de usar el chatbot, se ejecuta el preprocesamiento y configuración del modelo todo la clase ia.ipynb


# Rutas que se deben cambiar en la clase home.py 
## Ruta del modelo entrenado :
modelo = load_model('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/src/modeloB')
## Ruta de la imagen del logo en el sidebar
 st.sidebar.image("C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/imagenes/logo.jpg", use_container_width=True)

