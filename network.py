import socket
import controls

HOST = ''
PORT = 4406


class NetworkLogger:
    def __init__(self):
        print("Test")
        self.connect()
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.socket.bind((HOST,PORT))
    def run(self, controller):
        while True:
            data = self.socket.recvfrom(4096)
            data = data[0].decode('utf-8').split()
            if data[0] == "Input":
                controller.update_sticks(float(data[2]), float(data[3]), float(data[4]), float(data[5]))
                controller.interpret(int(data[1]))
        '''
        if data.startswith("mag") or data.startswith("acc"):

            stick_timeout += 1
            if stick_timeout > 2:
                ui.update(controller)
            continue
        if data[0] not in controls:
            continue
        stick_timeout = 0
        data = data.rstrip().split()
        if data[1] in controls:
            controller.update_sticks(float(data[5]), float(data[7]), float(data[9]), float(data[11]))
        else:
            controller.update_sticks(float(data[4]), float(data[6]), float(data[8]), float(data[10]))
        ui.update(controller)
        print(data)
'''