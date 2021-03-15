import sys
import socket as soc

def client(host, s_argv, t_argv):
    # socket 1 with RS server
	try:	
		rc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		rshost = soc.gethostname()
		rserver_ip = soc.gethostbyname(host)
		print("[C]: Connected with {} at port: {}".format(rserver_ip, s_argv))
	except soc.error as err:
		print("Error connecting to {}".format(err))
		exit()

	rserver_bind = (rserver_ip, s_argv)
	rc.connect(rserver_bind)

	# open and write 
	fp = open("PROJI-HNS.txt", "r") 
	fw = open('HW2out.txt','w')
	
	for line in fp:		
		rc.send(line.rstrip().encode("utf-8"))
		rs_response = rc.recv(256).encode("utf-8")
		print("[RS]: {}".format(rs_response))

		check_rs = rs_response.split()
  
		if check_rs[2] == 'A':
			fw.write(rs_response + '\n')
		else:
			# socket closes when it is not used
			# create new connection everytime it checks for a dns look up
			ts = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
			tshost = soc.gethostname()
			tserver_ip = soc.gethostbyname(tshost)
			tserver_bind = (tserver_ip, t_argv)
			ts.connect(tserver_bind)
			print("[TS]: Connected to {} at port: {}".format(tserver_ip, t_argv))
			ts.send(line.rstrip().encode("utf-8"))
			t_server_response = ts.recv(200).decode("utf-8")
			print("[TS]: {}".format(t_server_response))				
	
			fw.write(t_server_response + '\n')	
	fp.close()
	fw.close()
	rc.close()
	exit()

if __name__ == '__main__':
	host = sys.argv[1]
	rs_argv = int(sys.argv[2])
	ts_argv = int(sys.argv[3])
	client(host, rs_argv, ts_argv)

