import time


def slow_print(text):
    for char in text:
        time.sleep(0.2)
        print(char, end=' ', flush=True)
