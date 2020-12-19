import socket
from IPy import IP

def DefaultNumber(Port):
    if Port == '':
        Port = 100
        return Port
    else:
        Port = int(Port)
        return Port

def MultiIP(IPAddress, Port):
    print('\nScanning ' + str(IPAddress) + ' :')
    Scan(IPv4(IPAddress), Port)
    print('IP Address of ' + str(IPAddress) + ' is: ' + IPv4(IPAddress))

def IPv4(IPro):
    try:
        IP(IPro)
        return IPro
    except ValueError:
        return socket.gethostbyname(IPro)

def Seperator(IPs):
    if ',' in IPAddress:
        for IPplus in IPAddress.split(','):
            MultiIP(IPplus.strip(' '), Port)
    else:
        Scan(IPAddress, Port)

def Scan(IPAddress, Port):
    C = 0
    O = 0
    for Port in range(1, Port+1):
        try:
            sock = socket.socket()
            sock.settimeout(.5)
            sock.connect((IPAddress, Port))
            print('Port ' + str(Port) + ' is Open')
            O+= 1
        except:
            print('Port ' + str(Port) + ' is Closed')
            C+= 1

    print('Number of Closed Ports: ' + str(O))

try:
    IPAddress = input('Enter Website Name/IP Address(For 2 or More Target use Comma(,)): ')
    Port = input('Enter Number of Ports (Default is 100: )')
    Port = DefaultNumber(Port)
    Seperator(IPAddress)
except ValueError:
    print('Invalid Entry')

