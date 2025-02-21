---
title: Chatbot RAG'S
description: Chatbot con información de RAGs sobre la Historia, Presente y Futuro de la IA (gpt-4o-mini de OpenAI)
---
# Chatbot RAG'S Web
Chatbot con información de RAGs sobre la Historia, Presente y Futuro de la IA (gpt-4o-mini de OpenAI)

## Características

- Streamlit
- Python 3

## Web

- Ejecucion de consulta
     
![images](https://github.com/santiagorodriguez-dev/rag_02_web/blob/main/images/01.PNG)

![images](https://github.com/santiagorodriguez-dev/rag_02_web/blob/main/images/02.PNG)

![images](https://github.com/santiagorodriguez-dev/rag_02_web/blob/main/images/03.PNG)

## Cómo usar

- Hay un fichero secrets.toml.example en el carpeta .streamlit del proyecto, renombrar sin el .example y cambiar por los datos correctos.
```bash
[security]
SECRET=''
API_URL='https://xxxxxxxxxxxxxxxxx/call_modelo'
```
- Crear un entorno virtual 
```bash
python -m venv venv
```
- Activar el entorno virtual en Windows
```bash
venv\Scripts\activate
```
- Activar el entorno virtual en macOS/Linux
```bash
source venv/bin/activate
```
- Clonar el repositorio localmente e instalar paquetes con pip 
```bash
pip install -r requirements.txt
```
- Ejecutar localmente usando 
```bash
streamlit run streamlit_app.py
```