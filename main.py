import comm

"""
import sys
import glob
import serial
import datetime
import json

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except Exception as e:
            print(f"{datetime.datetime.now()} - AVISO - {e}")
            pass
    return result

def saveConfig(port, baud):
    data = {"PORT" : port, "BAUD" : baud}
    with open("cfg.json", "w") as cfg_file:
        json.dump(data, cfg_file, indent=2)
    cfg_file.close()

def loadConfig():
    cfg_file = open("cfg.json", "r")
    cfg_data = json.load(cfg_file)
    port = cfg_data["PORT"]
    baud = cfg_data["BAUD"]
    cfg_file.close()
    return port, baud
"""    

def Main():
    
    try:
        port, baud = comm.loadConfig()
        sp = serial.Serial(port = port,
                           baudrate = baud,
                           parity = serial.PARITY_NONE,
		                   stopbits = serial.STOPBITS_ONE,
		                   bytesize = serial.EIGHTBITS,
		                   timeout = 1)
    except:
        s_port = comm.listPorts()
        baudrate = [2400, 4800, 9600, 19200, 38400, 57600, 115200]
        
        if len(s_port) > 0:
            print("\nPortas disponíveis:")
            for i in range (0, len(s_port)):
                #print(serial_ports())
                print(f"{i} - {s_port[i]}")
        else:
            print("\nNão há portas seriais disponíveis.")
            exit()

        selected_port = int(input("\nSelecione o número da porta desejada: "))

        print("\nVelocidade de comunicação:")
        for i in range (0, len(baudrate)):
            print(f"{i} - {baudrate[i]}")

        selected_br = int(input("\nSelecione a velocidade da porta desejada: "))
        
        print(f"\nSelecionada porta '{s_port[selected_port]}' com velocidade {baudrate[selected_br]}")

        sp = serial.Serial(port = s_port[selected_port],
                        baudrate = baudrate[selected_br],
                        parity = serial.PARITY_NONE,
                        stopbits = serial.STOPBITS_ONE,
                        bytesize = serial.EIGHTBITS,
                        timeout = 1)

        saveConfig(s_port[selected_port], baudrate[selected_br])
        print("\nConfigurações salvas.\n")

    while True:
        
        x = b''
        packet = ""

        while x != b'\n':
            x = sp.read()
            packet += x.decode("utf-8", "ignore")
        print(packet)

if __name__ == '__main__':
    Main()
    
    