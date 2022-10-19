import time
from threading import Thread


def minhaThreadLegal():
    for i in range(10):
        time.sleep(5)
        print("oi... eu sou a thread")


t1 = Thread(target=minhaThreadLegal)
t1.start()


while True:
    print('Estou rodando...')
    time.sleep(.5)

print("Encerrando msg")