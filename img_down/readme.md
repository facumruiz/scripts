# Script de Descarga de Imágenes

Este script en Python permite descargar imágenes desde una URL proporcionada por el usuario. Las imágenes se descargan en una carpeta especificada o en la carpeta predeterminada `./img`.

## Requisitos

- Python 3.x
- Biblioteca `requests` (se puede instalar con `pip install requests`)

## Uso

1. Ejecute el script en su entorno de Python.
2. Ingrese la URL de la imagen cuando se le solicite.
3. El script descargará la imagen en la carpeta especificada (o en `./img` por defecto).
4. Puede decidir si desea descargar otra imagen.

## Funcionalidades

- Verifica la existencia de la carpeta de destino y la crea si no existe.
- Genera nombres de archivo únicos para evitar conflictos.
- Proporciona mensajes de éxito o error después de intentar descargar una imagen.
- Maneja excepciones al realizar solicitudes HTTP.

## Ejemplo

```bash
Ingresa la URL de la imagen: https://example.com/image.jpg
Imagen descargada con éxito: ./img/img1.jpg
¿Quieres descargar otra imagen? (yes/no): yes
Ingresa la URL de la imagen: https://example.com/another_image.png
Imagen descargada con éxito: ./img/img2.png
¿Quieres descargar otra imagen? (yes/no): no
