# #Per stampare l'ora corrente
from datetime import datetime

now = datetime.now()

log = open(f"file_esempio/log_{now}.txt","w")

# print(now)

# #Per isolare solo ore minuti e secondi
# #Formattiamo l'informazione come più ci piace
# current_time = now.strftime("%H:%M:%S")
# print(f"Ora corrente: {current_time}")

#rif: https://docs.python.org/3/library/time.html
import time

# t = time.localtime()
# print(t)
# #Formatto l'informazione
current_time = time.strftime("%A %d %B %Y", time.localtime())
print(f"Current time: {current_time}")
time.sleep(2)
print("Esco dopo 2 secondi")
time.sleep(0.2)#millisecondi
print("C")
time.sleep(2)
print("i")
time.sleep(2)
print("a")
time.sleep(2)
print("o")