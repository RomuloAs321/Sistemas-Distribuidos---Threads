# 10 threads são incrementadas em um contador global. 
# O uso de lock garante que apenas uma thread modifique o contador por vez
# evitando condições de corrida e garantindo a integridade dos dados.


import threading
contador = 0
lock = threading.Lock()

def incrementa():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

threads = []
for i in range(10):
    thread = threading.Thread(target=incrementa)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Contador final: {contador}")
