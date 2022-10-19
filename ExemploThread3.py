import time
from threading import Thread

def minhaThreadLegal(msg,t):
    for i in range(10):
        time.sleep(t)
        print(msg)
    print("Encerrando thread")

t1 = Thread(target=minhaThreadLegal, args=("oi..sou a thread 1",2))
t1.start()

t2 = Thread(target=minhaThreadLegal, args=("oi..sou a thread 2",1.5))
t2.start()

while t1.is_alive() or t2.is_alive():
    print('Estou rodando...')
    time.sleep(.5)

print("Encerrando msg")