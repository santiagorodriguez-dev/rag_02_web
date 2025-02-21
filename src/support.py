
import sys
sys.path.append("../")

import requests

def post_request(url, payload, headers=None):
    """
    Realiza una solicitud POST a la API dada con los parámetros especificados.

    :param url: URL de la API.
    :param payload: Diccionario con los datos a enviar en el cuerpo de la solicitud.
    :param headers: Diccionario con los encabezados opcionales (por defecto, 'Content-Type': 'application/json').
    :return: Respuesta de la API en formato JSON.
    """
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Lanza una excepción en caso de error HTTP
        return response.json()  # Devuelve la respuesta en formato JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

