import sys
import socket
from datetime import datetime

if(len(sys.argv) == 2):
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Wrong arguments!')
    sys.exit()

print('-' * 20)
print(f'scanning target {target}')
print(f'starting time: {(datetime.now())}')

try:
    counter = 0
    for port in range(0, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        print(f'checking port {port}')
        if(result == 0):
            print(f'success on {port}')
        s.close()
except KeyboardInterrupt:
    print('exiting program')
    sys.exit()
except socket.gaierror:
    print('cannot resolve given hostname')
    sys.exit()
except socket.error:
    print('could not conect to a server')
    sys.exit()