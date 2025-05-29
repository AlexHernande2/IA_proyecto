# ValuBot – Chatbot de Predicción de Precios de Inmuebles
**ValuBot** es un chatbot inteligente que predice el valor de un inmueble o su arriendo usando técnicas de *Machine Learning*. Utiliza PyCaret para entrenar un modelo de regresión y responder de forma interactiva a los datos ingresados por el usuario a través de Streamlit.

# Requisitos
## Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- Las siguientes librerías:

```bash
pip install pandas pycaret streamlit
```
---

## Estructura de archivos y rutas importantes

### Archivo de entrenamiento
- El modelo se entrena con el archivo `DatosFinales.csv`
- Asegúrate de que se encuentre en la siguiente ruta (ajusta si es necesario):
  ```
  C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/DatosFinales.csv
  ```

>  **Nota:** Modifica la ruta al archivo CSV si tu ubicación local es diferente.

###  Modelo preentrenado
- El archivo `modeloB.pkl` **no debe existir** inicialmente.
- Será generado automáticamente al ejecutar la clase `ia.ipynb`.

---

## Inicialización del modelo
Antes de usar el chatbot, ejecuta el preprocesamiento y entrenamiento del modelo en:
```
ia.ipynb
```
Este notebook crea el archivo `modeloB.pkl` y deja el sistema listo para usar.
---
##  Cambios necesarios en `home.py`

### Ruta del modelo entrenado:
```python
modelo = load_model('C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/src/modeloB')
```
###  Ruta del logo:
```python
st.sidebar.image("C:/Users/edwin/OneDrive - Universidad de Boyacá/Escritorio/IA_proyecto/imagenes/logo.jpg", use_container_width=True)
```
---
## Ejecución
Para correr la aplicación:
1. Abre una terminal.
2. Navega a la carpeta `src`:
   ```bash
   cd ruta/a/IA_proyecto/src
   ```
3. Ejecuta:
   ```bash
   streamlit run home.py
   ```
---
