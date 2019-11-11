import time
import threading
from pynput import keyboard

i = 0
seconds = 0
minute = 0

def on_press(key):
    global i
    i += 1
    print(f"{key}, {i}")
    #print(f"{key}", sep = " ", end = " ", flush = True)

def on_release(key):
    if(key == keyboard.Key.esc):
        t.cancel()
        return False

def timer():
    global t, seconds, minute
    t = threading.Timer(1.0, timer)    
    t.start()
    
    seconds += 1
    #print(f"Fino ad ora sono state digitate {i} caratteri in {seconds} secondi [{minute} minuti]")
    if(seconds % 60 == 0):
        minute += 1
        media = i/seconds
        print(f"Fino ad ora sono stati digitati {i} caratteri in {seconds} secondi [{minute} minuti]")
        print("La media e' di {0:.2f} al secondo".format(media))

def main():
    timer()
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
    

if __name__ == "__main__":
    main()
    