import socket

from mt19937predictor import MT19937Predictor

SERVER = "138.197.193.132"
PORT = 5002

def connect(server, port):
    # open a connection to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    return s

def read_until(s, delim=b':'):
    buf = b''
    s.settimeout(1)
    while not buf.endswith(delim):
        try:
            buf += s.recv(1)
        except:
            break
        
    s.settimeout(None)
        
    return buf.decode("utf8")

# Init socket
s = connect(SERVER, PORT)

# Collect data for prediction
predictor = MT19937Predictor()

_ = read_until(s, b">>>")
for i in range(624):
    s.send(b"R")
    resp = read_until(s, b">>>")
    rand = int(resp.split(" based on ")[1].split("P")[0])

    predictor.setrandbits(rand, 32)
    print(f'Collected {i+1}/624 ({round((i+1)/624*100, 2)}%)')

# Win 30 times
RPS_WIN = {
    "R": "P",
    "P": "S",
    "S": "R"
}

for i in range(30):
    nextrand = predictor.getrandbits(32)
    opp = ["R", "P", "S"][nextrand % 3]
        
    move = RPS_WIN[opp]
    s.send(bytes(move, "utf8"))
    print(move)
    
    resp = read_until(s, b">>>")
    print(resp)
    
s.close()