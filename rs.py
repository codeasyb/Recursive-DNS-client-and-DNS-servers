import sys
import socket as soc

queries = []
def dns_table():
	try:
		file = open("PROJI-DNSRS.txt", "r")
		i = 0
		for tokens in file:
			strings = tokens.split()
			queries.append(Dns(strings[0], strings[1], strings[2])) 
			i += 1
	except soc.error as err:
		print("Error opening file: {}".format(err))
	print("[RS]: Dns table ready")
	file.close()
 
def findhostnames(tokens):
    for entry in queries:
        if entry.host.lower() == tokens.lower():
            return entry
    return entry

class Dns:
	def __init__(self, host, ip, flag):
		self.host = host
		self.ip = ip
		self.flag = flag

	def toString(self):
		return "{} {} {}".format(self.host, self.ip, self.flag)

def server_listening():
	try:
		rs = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		print("[RS]: Connected successfully")
	except soc.error as err:
		print("Error connecting to client {}".format(err))

	server_address = ('', listenPort)
	rs.bind(server_address)
	rs.listen(1)
		
	print("[RS]: Open port: {}".format(listenPort))

	while True:
		conn, addr = rs.accept()
		hostname = '!empty'
		while hostname != "":
			hostname = conn.recv(200).decode("utf-8")
			
			print("[C]: {}".format(hostname))

			if hostname != "":
				found = findhostnames(hostname).toString()
				print("[RS]: {}".format(found))
				conn.send(found.encode("utf-8"))
	rs.close()
					
if __name__ == '__main__':
 	listenPort = int(sys.argv[1])
	dns_table()
	server_listening()





