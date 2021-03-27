import pygame
import time
import random

class Particle():
    def __init__(self, position):
        self.position = position
        self.lifetime = 250
        self.radius = 5
        self.color = pink
        self.gravity = 0.1
        self.xacc = random.randint(-100, 100)/100       # random number between -1.00 and 1.00, to be the x axis initial speed
        self.yacc = random.randint(-400, -200)/100      # random number between -4.00 and -2.00 to be the y axis upwards initial velocity
    def update(self):
        self.dead()
        self.show()
        self.colorchange()
        self.acceleration()
        self.boundaries()
    # updates particle gravity acceleration and position
    def acceleration(self):
        self.position = list(self.position)
        self.position[0] = (self.position[0]+self.xacc)
        self.position[1] = (self.position[1]+self.yacc)
        self.yacc += self.gravity
    # decreases the lifetime of each particle by 1(initially at 250), when lower than 0, it "dies", 
    def dead(self):
        self.lifetime += -1
        if self.lifetime < 0:
            particles.remove(self)
    # draw the particle in screen
    def show(self):
        self.color = tuple(self.color)
        self.position = tuple(self.position)
        pygame.draw.circle(screen, self.color, (self.position), self.radius)
    def colorchange(self):
        self.color = [abs(self.color[0]-1), abs(self.color[1]-1), abs(self.color[2]-1)]           # decreases the ammount of rgb by 1 each frame to give a "fade" look
    # detects if the particle hits screen borders
    def boundaries(self):                                                                 
        if self.position[0] >= width or self.position[0] <= 0:
            self.xacc *= -1
        if self.position[1] >= height or self.position[1] <=0:
            self.yacc *= -1


class ParticleEmitter(Particle):
    def __init__(self, position, toggle):
        super().__init__(self)
        self.count = 0
        self.position = position
        self.togglefollow = toggle
    def update(self): 
        self.addparticle()
        self.followstatic() 
    # define how much particles spawn for each frame
    def addparticle(self):
        self.count = (self.count +1 ) %2  # each 2 frames a particle is added
        if self.count == 0:
            p = Particle((self.position[0], self.position[1]))
            particles.append(p)
    # check if it should follow the mouse or not
    def followstatic(self):
        if self.togglefollow:
            self.position = list(self.position)
            self.position[0], self.position[1] = pygame.mouse.get_pos()
   

        


gameover= False

height = 400
width = 600

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
pink = [255, 192, 203]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame!")
clock = pygame.time.Clock()

togglefollow = 0

particles = []
emitters = []
while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:    # toggle follow mode, which create a emiiter object who follow your mouse cursor
                if togglefollow == 0:
                    togglefollow = 1
                    print("Toggle: Follow")
                else:
                    togglefollow = 0
                    print("Toggle: Static")
            if event.key == pygame.K_a:         # press "a" to spawn a particle emitter at your cursor x and y
                mx, my = pygame.mouse.get_pos() # alternativily you can press "q" to make it follow your cursor arround
                emitter = ParticleEmitter((mx, my), togglefollow)
                emitters.append(emitter)

            if event.key == pygame.K_c:   # remove oldest emiiters current on the screen, in other words, the first of the list
                emitters.pop(0)
            if event.key == pygame.K_d:   # print out the number of current particles and emitters in the screen
                print("particles: ", len(particles),"\nemitters: ", len(emitters))

    screen.fill(black)

    for emitter in emitters:
        emitter.update()        # calls a update for each emitter object
    for particle in particles:
        particle.update()       # calls a update for each particle object

    pygame.display.update()
    clock.tick_busy_loop(60)

pygame.quit()

