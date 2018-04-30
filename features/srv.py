import  socket
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 1234))
sock.listen(1)
conn, addr = sock.accept()

#print ('connected:', addr)
time = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
#text = time
conn.send(time.encode())
conn.close()
exit()