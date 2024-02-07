import requests
import os

def descargar_imagen(url, carpeta_destino="./img"):
    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener el nombre de archivo de la URL
    nombre_base = "img"
    extension = url.split('.')[-1]
    contador = 1

    while True:
        nombre_archivo = os.path.join(carpeta_destino, f"{nombre_base}{contador}.{extension}")

        if not os.path.exists(nombre_archivo):
            break

        contador += 1

    try:
        # Realizar la solicitud para descargar la imagen
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()

        # Escribir la imagen en el archivo local
        with open(nombre_archivo, 'wb') as archivo:
            for bloque in respuesta.iter_content(1024):
                archivo.write(bloque)

        print(f"Imagen descargada con éxito: {nombre_archivo}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return False

if __name__ == "__main__":
    while True:
        # Solicitar al usuario que ingrese la URL de la imagen
        url_imagen = input("Ingresa la URL de la imagen: ")

        # Llamar a la función para descargar la imagen y verificar si la descarga fue exitosa
        exito_descarga = descargar_imagen(url_imagen)

        # Preguntar al usuario si desea descargar otra imagen
        respuesta = input("¿Quieres descargar otra imagen? (yes/no): ").lower()

        if respuesta not in ('yes', 'y'):
            break  # Salir del bucle si la respuesta no es 'yes' o 'y'
