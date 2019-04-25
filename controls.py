
controls = ["A", "B", "X", "Y", "L", "R", "ZR", "ZL", "Left", "Right", "Up","Down","+","-","TV","Home","SL","SR",
            "RE_Left","RE_Right","RE_Up","RE_Down","LE_Left","LE_Right","LE_Up","LE_Down"]
control_bit = {"btn-A":0x8000, "btn-B": 0x4000, "btn-X": 0x2000, "btn-Y":0x1000,"dpad-left":0x0800,"dpad-right":0x0400,"dpad-up":0x0200,"dpad-down":0x0100,
                "btn-zl":0x0080,"btn-zr":0x0040,"btn-L":0x0020,"btn-R":0x0010,"btn-start":0x0008,"btn-select":0x0004,"btn-home":0x0002,"left-stick-click":0x00040000,"right-stick-click":0x00020000}

class Controller:
    def __init__(self):
        self.reset()
    def update_sticks(self, lx, ly, rx, ry):
        self.Lx, self.Ly = lx, ly
        self.Rx, self.Ry = rx, ry
    def reset(self):
        self.Lx = 0
        self.Ly = 0
        self.Rx = 0
        self.Ry = 0
        self.buttons = {}
    def interpret(self, flags):
        for input, flag in control_bit.items():
            self.buttons[input] = flags & flag == flag
               