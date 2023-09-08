import threading
import time
import random

balance = 100
lock = threading.Lock()#objeto que controla acesso e recurso da variavel.

def withdraw():
    global balance, lock
    for _ in range(10):
            lock.acquire()
            x = balance
            time.sleep(random.random()/100)
            balance = x - 1
            lock.release()
            
def deposit():
    global balance, lock
    for _ in range(9):
            lock.acquire()
            x = balance
            time.sleep(random.random()/100)
            balance = x + 1
            lock.release()
            
def perform_transactions():   
    
    
    p1 = threading.Thread(target=withdraw)
    p2 = threading.Thread(target=deposit)
    
    p1.start()
    p2.start()
    
    p1.join()#obriga que o codigo pare até que as threads sejam totalmente executadas
    p2.join()
    
    print("Final balance = {}".format(balance))

for _ in range(10):
    perform_transactions()
    balance = 100
