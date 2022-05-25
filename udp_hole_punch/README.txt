UDP "HOLE PUNCH" P2P Communication

server.py for rendezvous to exchange IPs and Ports. Is not required, you can hard code IPs and Ports in client.py of each machine

client.py connects to rendezvous server and sends its ip and port. Once two clients connect to server the server sends the opposite clients info to each client. Client then creates a hole in the firewall with a “UDP Hole Punch” and starts listening on its port. After both clients create hole punch clients can send messages back and forth. Not limited to text can sent files by something like cat. “UDP Hole” will close after ~15 seconds and clients will have to punch holes again or you can add “keep alive” messages to keep the “hole” open
