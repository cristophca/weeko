# Bienvenidos al programa de línea de comandos 'weeko' desarrollado con Python.
## Descripción:
El programa realizará una copia de seguridad semanal de los archivos que se encuentren en una carpeta especifica.
## Uso:
El programa acepta un parámetro obligatorio y dos opcionales:
1. Parámetro obligatorio: Se debe introducir la ruta de la carpeta a copiar.
2. Parámetros opcional (--exclude): Donde se debe especificar (Separadas por coma) las extensiones que no se deben incluir en la copia de seguridad.
3. Parámetro opcional (--verbose): Imprime por pantalla los nombre y su valor MD5 de todos los ficheros copiados.

## Instalación:
1. Descarga el codigo con el siguiente comando:
'''
git clone https://github.com/cristophca/weeko.git
'''
2. Crea y activa el entorno virtual:
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Instala las librerias necesarias que se encuentran en el fichero `requierements.txt`:
```
pip install -r requirements.txt
```

   
