import random
import threading
import time

fila = []
resultado = []
#evento = threading.Event()
condition = threading.Condition()

def Consumidor():
    global fila, resultado

    while True:
        try:
            x = fila.pop(0)
            print('\nCONSUMIDOR: processando tarefa {}'.format(x))
            time.sleep(2)
            resultado.append(x)
            
        except:
            #evento.set()
            #evento.clear()#se nao chamar o clear, o produtor nao para mais.
            condition.acquire()
            condition.notify()
            condition.release()
            time.sleep(2)
            
def Produtor():
    global fila, resultado
       
    for i in range(10):
        if len(fila) == 2:
            #evento.wait()
            condition.acquire()
            condition.wait()
            condition.release()
        fila.append(i)
        time.sleep(random.random())
        print('PRODUTOR: tarefas pendentes {}'.format(fila))

    while True:
        print('PRODUTOR: tarefas terminadas {}'.format(resultado))
        if len(fila) == 0:
           break
        time.sleep(1)
        
def Produtor2():
    global fila, resultado
       
    for i in range(11,20):
        if len(fila) == 2:
            #evento.wait()
            condition.acquire()
            condition.wait()
            condition.release()
        fila.append(i)
        time.sleep(random.random())
        print('PRODUTOR2: tarefas pendentes {}'.format(fila))

    while True:
        print('PRODUTOR2: tarefas terminadas {}'.format(resultado))
        if len(fila) == 0:
           break
        time.sleep(1)
        
         
t1 = threading.Thread(target=Consumidor)
t2 = threading.Thread(target=Produtor)
t3 = threading.Thread(target=Produtor2)

t1.start()
t2.start()
t3.start()

#B) ambos acordam ao mesmo tempo
#C) os produtores sao acordados de maneira aleatoria.