import time
it=time.asctime(time.localtime(time.time()))
print(it)
dst=time.asctime(time.localtime(time.daylight))
print(dst)
print(time.altzone)
