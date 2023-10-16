import os
import shutil


def encontrar_sefip_importar_conectividade(path_default):

    path = path_default


    try:

        for file in os.listdir(path):
            # for subfile in os.listdir(os.path.join(path, file)):
            if file.split('.')[-1] == 'SFP':
                path_found = os.path.join(path, file)
    except:
        pass
    
    print(path_found)

    return path_found


def limpar_pasta_sefip_c():

    path = 'C:\Program Files (x86)\CAIXA\Arquivos'

    for folder in os.listdir(path):
        print(os.path.join(path, folder))
        try:
            shutil.rmtree(os.path.join(path, folder))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    encontrar_sefip_importar_conectividade('W:\\Pessoal\\Clientes\\DAROS EDIFICAÇÕES E OBRAS LTDA - 270\\FOLHA DE PAGAMENTO\\2023\\07.2023')
    
    