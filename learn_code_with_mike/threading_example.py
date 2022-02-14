import threading
import time

def func(sleep_time=10):
    print("**start")
    time.sleep(sleep_time)

    print("**end: slept for %d seconds" % sleep_time)




t = threading.Thread(target=func, args=(3,))
t.start()

t.join()  # wait for thread to finish before continuing

print("end")  # Without t.join(), this may execute first, before thread start

