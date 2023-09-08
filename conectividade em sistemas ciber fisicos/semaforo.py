import socket
import threading

semaphore = threading.BoundedSemaphore(2)
def TrataCliente(conn, addr):

    while True:
        data = conn.recv(100)
        print('{} enviou {}'.format(addr,data))
        if not data:
            break
 
    print('{} encerrou'.format(addr))
    semaphore.release()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(('', 9999))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5)

print('aguardando conexoes em ', 9999)

while True:
    conn, addr = s.accept()
    print('recebi uma conexao do cliente ', addr)
    semaphore.acquire()
    t = threading.Thread( target=TrataCliente, args=(conn,addr,))
    t.start()
    

