import sys
import socket as soc

queries = []
def dns_table():

	try:
		file = open("PROJI-DNSTS.txt", "r")
		i = 0
		for tokens in file:
			strings = tokens.split()
			queries.append(Dns(strings[0], strings[1], strings[2])) 
			i += 1
	except soc.error as err:
		print("Error opening file: {}".format(err))
	print("[TS]: Dns table ready")
	file.close()

class Dns:
	def __init__(self, host, ip, flag):
		self.host = host
		self.ip = ip
		self.flag = flag

	def toString(self):
		return "{} {} {}".format(self.host, self.ip, self.flag)

def server_listening():
	try:
		ts = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		print("[TS]: Connected successfully")
	except soc.error as err:
		print("Error connecting to client {}".format(err))

	server_address = ('', listenPort)
	ts.bind(server_address)
	ts.listen(1)
		
	print("[TS]: Open port: {}".format(listenPort))

	def findhostnames(tokens):
		for entry in queries:
			if entry.host.lower() == tokens.lower():
				return entry.toString()
		return False

 
	while True:
		conn, addr = ts.accept()
		hostname = conn.recv(200).decode("utf-8")

		found = findhostnames(hostname)
		print("[]=>{}".format(found))
		if found == False:
			found = "{} - Error:HOST NOT FOUND".format(hostname)
		print("[TS]: {}".format(found))
		conn.send(found.encode("utf-8"))
	# ts.close()
					
if __name__ == '__main__':
 	listenPort = int(sys.argv[1])
	dns_table()
	server_listening()
	
	





