from queue import Queue
import time

#Створити чергу заявок
queue = Queue()

def generate_request():
    new_request = time.time()
    print(new_request)
    queue.put(new_request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Заявка з ID:{request} виконана')
    else:
        print('Наразі черга пуста, нових заявок немає')


while True:
    generate_request()
    process_request()
    time.sleep(1)

