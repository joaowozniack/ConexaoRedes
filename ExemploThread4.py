import time
from threading import Thread

rodando = True

def minhaThreadLegal(msg, t):
    for i in range(10):
        time.sleep(t)
        print(msg)
        if not rodando:
            break
    print("Encerrando thread")


t1 = Thread(target=minhaThreadLegal, args=("oi... sou a thread 1", 2))
t1.start()

t2 = Thread(target=minhaThreadLegal, args=("oi... sou a thread 2", 0))
t2.start()

while t1.is_alive() or t2.is_alive():
    print('Estou rodando...')
    time.sleep(.5)
    rodando = False

print("Encerrando msg")