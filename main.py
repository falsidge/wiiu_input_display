import threading

import display
import controls
import network

def main():
    controller = controls.Controller()
    gui = display.UserInterface()
    net = network.NetworkLogger()

    net_thread = threading.Thread(target=net.run, args=[controller])
    net_thread.daemon = True
    net_thread.start()
    gui.run(controller)

if __name__ == "__main__":
    main()