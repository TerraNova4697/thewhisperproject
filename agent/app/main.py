import time


i = 0

while True:
    with open("myservice.log", "a") as f:
        f.write(f"New log written in file #{i}\n")
    i += 1
    time.sleep(3)
