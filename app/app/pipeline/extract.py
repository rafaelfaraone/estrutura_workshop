import glob #Biblioteca para listar arquivos '
import os
import pandas as pd
import fnmatch

from typing import List  

path2 = r"C:\Users\Rafael\Desktop\input"

arquivos_xlsx = []
def extract_from_excel (path2: str) -> List[pd.DataFrame]:

    for caminho_raiz, _, arquivos in os.walk(path2):
        for nome_arquivo in arquivos:
            # Verifica se o arquivo possui a extensão .xlsx
            if fnmatch.fnmatch(nome_arquivo, '*.xlsx'):
                # Se sim, adiciona o caminho completo do arquivo à lista
                caminho_completo = os.path.join(caminho_raiz, nome_arquivo)
                arquivos_xlsx.append(caminho_completo)
                #print (caminho_completo)

    data_frame_list = []
    for file in arquivos_xlsx:      
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path2)
    print (data_frame_list)