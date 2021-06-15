
import argparse
import os
import datetime
import hashlib 
import shutil
import logging
from colorama import Fore, Style
import tqdm
import time
#python weeko.py original -e .pyc -v

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Directorio origen')
    parser.add_argument(
        '-e','--exclude', 
        help= 'Lista de extensiones no incluidas',
    )
    parser.add_argument(
        '-v','--verbose', 
        help= 'Imprime por pantalla los nombres y valores MD5 copiados',
        action='store_true'
    )

args = parser.parse_args()
file_path = args.path
excludes = args.exclude.split(',')

#Función MD5
def get_hash(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        m.update(f.read())
    return m.hexdigest()  


#1. Calculo del día que es hoy y creación de la carpeta de destino de las copias.
date = datetime.date.today()
today_number = date.weekday()

turn_name = {
            0:'lunes', 1:'martes',
            2:'miercoles', 3:'jueves',
            4:'viernes', 5:'sabado', 6:'domingo',
}
binder_name = turn_name.get(today_number)

os.makedirs(binder_name, exist_ok=True)

#2. Lee los contenidos del directorio origen.
files = os.listdir(file_path)
#2.1. Ficheros aceptados del directorio origen
files_ok = []
for fn in os.listdir(file_path):
    nomb, ext = os.path.splitext(fn)

    if ext in excludes:
        print(Fore.RED + f' Archivo {fn} excluido')
        print(Style.RESET_ALL + ' ')
    else:
        
        #path_ok = file_path + '/' + fn
        hash_md5 = get_hash(f'{file_path}/{fn}')
        #copia de directorio.
        src = f'{file_path}/{fn}'
        dst = f'{binder_name}'
        copy_file = shutil.copy(src, dst)
        #Guardar el registro de cada operación en el fichero log.
        logging.basicConfig(filename='weeko.log', level=logging.INFO)
        logging.info(f'Copia de {fn} en la capeta {binder_name}\n(MD5 {hash_md5:<32})')      
        #Mostrar por pantalla  el codigo hash y el nombre del fichero si -v es activado
        if args.verbose:
            print(Fore.GREEN + f"{fn:<28} \n {hash_md5:<32}")
            
        for i in tqdm.tqdm(fn):
            time.sleep(.1)
        


    
            






 



    
       
            




