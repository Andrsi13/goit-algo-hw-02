from queue import Queue
import time

#Створити чергу заявок
queue = Queue()

def generate_request():
    new_request = time.time()
    print(f'Нова заявка з ID:{new_request}')
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

    user_input = input("Для завершення програми введіть 'exit' або '+' для продовження: ")
    if user_input.strip().lower() == 'exit':
        print("Програма завершила роботу.")
        break
    elif user_input.strip() == '+':
        continue


