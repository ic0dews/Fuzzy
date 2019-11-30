import socket
import time
import sys
import threading

banner = ('''
███████╗██╗   ██╗███████╗███████╗██╗   ██╗
██╔════╝██║   ██║╚══███╔╝╚══███╔╝╚██╗ ██╔╝
█████╗  ██║   ██║  ███╔╝   ███╔╝  ╚████╔╝ 
██╔══╝  ██║   ██║ ███╔╝   ███╔╝    ╚██╔╝  
██║     ╚██████╔╝███████╗███████╗   ██║   
╚═╝      ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
                                                - Written and Designed by: cyphres
                                        ''')
print(banner)
connection = input("What is the address of target connection?: )
port = 21

server_address = (connection, port)

def connection(self):
	try:
		print("[+] Connecting...")
		sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(10) #10 Second timeout, change this to whatever you want.
		sc.connect(server_address)
		print("[+] Connection Established")
		connected = True
		if connected == True:
			userinput = input("Would you like to proceed? y/n: ")
			if userinput == "y":
				message = input("What packets would you like to send?: ")
				amount = input("How many times would you like to send the packets?: ")
				while amount > 0:
					sc.send(message)
					amount =- 1
				print('Data Recieved: ', repr(data))
			else:
				print("Alright Closing Connection")

	except:
		print("[-] Connection Refused")
		connected = False



--------------------------------------------------------------------------------
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def bar(self):
    for i in progressbar(range(100), 40):
        time.sleep(0.1)
---------------------------------------------------------------------------------

if __name__ == "__main__": 
    thead1 = threading.Thread(target=connection, args=(10,)) 
    thread2 = threading.Thread(target=bar, args=(10,)) 
  

    thread1.start() 
    thread2.start() 
  
    thread1.join()  
    thread2.join() 
