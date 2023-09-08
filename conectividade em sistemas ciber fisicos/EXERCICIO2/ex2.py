import os
import shutil

#a) Imprima o diretório de trabalho corrente
print(os.getcwd())

#b) Crie os subdiretórios SUBDIR1 e SUBDIR2
#os.makedirs('SUBDIR1')
#os.makedirs('SUBDIR2')

#c) Copie o arquivo TEXTO.txt para o SUBDIR1
#shutil.copy2('teste.txt', 'SUBDIR1/teste.txt')

#d) Mova o arquivo TEXTO.txt do SUBDIR1 para o SUBDIR2
#shutil.move('SUBDIR1/teste.txt', 'SUBDIR2')

#e) Apague o SUBDIR1 e tudo o que estiver dentro
shutil.rmtree('SUBDIR1')
