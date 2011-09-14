import pygame
import pygame.gfxdraw
from pygame.locals import *

class dUG_game:
    def __init__( self):
        self._running = True
        self._surf_display = None
        self.size = self.width, self.height = 800, 600
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.gamestate = {}

    def on_init( self):
        numpass, numfail = pygame.init()
        if numfail!=0:
            print "Pygame init failed."
            return False
        self._surf_display = pygame.display.set_mode( self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        pygame.display.set_caption( "dUG")

    def on_event( self, event):
        if event.type==pygame.QUIT:
            self._running = False

    def on_loop( self):
        pass
    def on_render( self):
        self._surf_display.fill( pygame.Color( 255, 255, 255, 0))
        pygame.gfxdraw.aacircle( self._surf_display, self.width/2, self.height/2, 64, pygame.Color( 0, 0, 0, 255))
        pygame.gfxdraw.filled_circle( self._surf_display, self.width/2, self.height/2, 64, pygame.Color( 0, 0, 0, 255))
        pygame.display.flip()
        pass
    def on_cleanup( self):
        pygame.quit()

    def on_execute( self):
        if self.on_init()==False:
            self._running = False

        while( self._running):
            deltat = self.clock.tick( self.FPS)
            for event in pygame.event.get():
                self.on_event( event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__=="__main__":
    game = dUG_game()
    game.on_execute()

