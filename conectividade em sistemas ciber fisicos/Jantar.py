import threading
import random
import time

nomes = ['Aristotle', 'Kant', 'Spinoza', 'Marx', 'Russell']
pratos = [0,0,0,0,0]
garfo = []
threads = []
 
def filosofo(nome, left):
    global garfo
    global pratos
    right = left + 1
    if right > (len(nomes)-1):
        right = 0
    
    garfo.append(nome)
   
    print('Filoso {} sentou a mesa na posicao {}'.format(nome,pos));
    time.sleep(10)
 
    while True:

        print('\nquem esta com garfo: {}'.format(garfo))
        print('vezes que cada um comeu: {}\n'.format(pratos))

        if garfo[right] == 'vazio':
            garfo[right] = nome
            print('{} pegou o garfo da direita'.format(nome))
           
        if garfo[left] == 'vazio':
            garfo[left] = nome
            print('{} pegou o garfo da esquerda'.format(nome))

        if garfo[right] == garfo[left] == nome:
            print('{} esta comendo'.format(nome))
            time.sleep(5)
            garfo[right] = garfo[left] = 'vazio'
            print('{} terminou de comer e saiu da mesa'.format(nome))
            pratos[left] += 1
            #break
            #B) Execute novamente o código e verifique se programa está se 
            #comportando normalmente. Observe se algum processo entrou em STARVATION
            #Ocorre Starvation exemplo:vezes que cada um comeu: [0, 0, 9, 0, 11]
        else:
            print('\n{} não conseguiu comer e vai pensar'.format(nome))     
            if garfo[right] == nome:
                  garfo[right] = 'vazio'
            if garfo[left] == nome:
                  garfo[left] = 'vazio'
            time.sleep(random.randint(10,20))

pos = 0
for n in nomes:
    t = threading.Thread(target=filosofo, args=(n,pos,))
    threads.append(t)
    t.start()
    time.sleep(1)
    pos += 1

print("Todos os filósofos estão na mesa")
print(garfo)

for x in threads:
    x.join()

print('vezes que cada um comeu: {}\n'.format(pratos))
print("A mesa está vazia")