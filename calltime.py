from datetime import datetime
x=datetime.now()
print(x.strftime("%I : %M : %s : %p"))
print(x.strftime("%H : %M : %P"))