import pygame
import json


class UserInterface:
    def __init__(self):
        pygame.init()
        self.running = True
        self.load_resource()
        self.set_size((1280, 671))
    
    def update(self):
        self._handle_events()
        self.redraw(self.controller)
    def load_resource(self):
        with open("resource/gamepad/skin.json") as f:
            data = json.load(f)
        self.data = data
        self.base = data["general"]["background"]
        self.sticks = {}
        for stick in self.data["sticks"]:
            self.sticks[stick] = pygame.image.load("resource/gamepad/"+stick+".png")
            if self.data["sticks"][stick]["clickable"]:
                self.sticks[stick + "-click"] = pygame.image.load("resource/gamepad/"+stick+"-click.png")
        
            if self.sticks[stick].get_rect()[2:] != self.data["sticks"][stick]["size"]:
                self.sticks[stick] = pygame.transform.scale(self.sticks[stick], self.data["sticks"][stick]["size"] )
            if self.data["sticks"][stick]["clickable"] and self.sticks[stick + "-click"].get_rect()[2:] != self.data["sticks"][stick]["size"]:
                self.sticks[stick + "-click"] = pygame.transform.scale(self.sticks[stick], self.data["sticks"][stick]["size"] )

        self.buttons = {}   
        for button in self.data["buttons"]:
            self.buttons[button] = pygame.image.load("resource/gamepad/"+button+".png")
            if self.buttons[button].get_rect()[2:] != self.data["buttons"][button]["size"]:
                self.buttons[button] = pygame.transform.scale(self.buttons[button], self.data["buttons"][button]["size"] )

    def set_size(self, size):
        self.background = pygame.image.load("resource/gamepad/"+self.base+".png")
        self._surface = pygame.display.set_mode(size)
    def redraw(self, controller):
        self._surface.fill((0,0,0))
        self._surface.blit(self.background,(0,0))
        for stick in self.data["sticks"]:
            s = self.data["sticks"][stick]
            x, y = s["position"]
            w, h = s["size"]
            if stick == "left-stick":
                if s["clickable"] and "left-stick-click" in controller.buttons and controller.buttons["left-stick-click"]:
                    self._surface.blit(self.sticks[stick+"-click"],(x - w/2 + s["radius"]*controller.Lx, y - h/2 - s["radius"]*controller.Ly))
                else:
                    self._surface.blit(self.sticks[stick],(x - w/2 + s["radius"]*controller.Lx, y - h/2 - s["radius"]*controller.Ly))
            elif stick == "right-stick":
                if s["clickable"] and "right-stick-click" in controller.buttons and controller.buttons["right-stick-click"]:
                    self._surface.blit(self.sticks[stick+"-click"],(x - w/2 + s["radius"]*controller.Lx, y - h/2 - s["radius"]*controller.Ly))
                else:
                    self._surface.blit(self.sticks[stick],(x - w/2 + s["radius"]*controller.Rx, y - h/2 - s["radius"]*controller.Ry))
        for button in self.data["buttons"]:
            if button in controller.buttons and controller.buttons[button]:
                x, y = self.data["buttons"][button]["position"]
                w, h = self.data["buttons"][button]["size"]
                self._surface.blit(self.buttons[button], (x-w/2,y-h/2))
        pygame.display.flip()
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False

    def run(self, controller):
        self.controller = controller
        clock=pygame.time.Clock()
        while self.running:
            self.update()

            clock.tick(60)
        pygame.quit()