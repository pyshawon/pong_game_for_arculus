import pygame
import sys
import random
from math import *

pygame.init() # initialize pygame

width = 800
height = 600
display = pygame.display.set_mode((width, height)) # set view Size
pygame.display.set_caption("Arculus Pong Game")
clock = pygame.time.Clock()

background = (0, 109, 69)
white = (236, 240, 241)
ball_color = (0,252,0)

margin = 4 
scoreLeft = scoreRight = scoreTop = scoreBottom = 0 # default Score
maxScore = 20 # max score

font = pygame.font.SysFont("Small Fonts", 30)
largeFont = pygame.font.SysFont("Small Fonts", 60)

 
class Paddle:
    """
    :Const - Position "Left", "Right", "Top", "Bottom"
    :Method - Paddle viewing position and moving position
    """
    def __init__(self, position):
        self.paddleSpeed = 6
        if position in ["Left", "Right"]:
            self.w = 10
            self.h = self.w*8

            if position == "Left":
                self.x = 1.5*margin
            else:
                self.x = width - 1.5*margin - self.w
            self.y = height/2 - self.h/2

        if position in ["Top", "Bottom"]:
            self.h = 10
            self.w = self.h*8

            if position == "Top":
                self.y = 1.5*margin
            else:
                self.y = height - 1.5*margin - self.h
                
            self.x = width/2 - self.w/2
    
    def show(self):
        # Draw Paddle
        pygame.draw.rect(display, white, (self.x, self.y, self.w, self.h))

    def move_left_right(self, ydir):
        self.y += self.paddleSpeed*ydir
        if self.y < 0:
            self.y -= self.paddleSpeed*ydir
        elif self.y + self.h> height:
            self.y -= self.paddleSpeed*ydir

    def move_top_bottom(self, ydir):
        self.x += self.paddleSpeed*ydir
        if self.x < 0:
            self.x -= self.paddleSpeed*ydir
        elif self.x + self.w> width:
            self.x -= self.paddleSpeed*ydir


# define 4 paddles
leftPaddle = Paddle("Left")
rightPaddle = Paddle("Right")
topPaddle = Paddle("Top")
bottomPaddle = Paddle("Bottom")

class Ball:
    """
    :Const - Color of the ball
    :Methods - Ball position and moveing angle of the ball
               Update Score value.
    """
    def __init__(self, color):
        self.r = 20
        self.x = width/2 - self.r/2
        self.y = height/2 -self.r/2
        self.color = color
        self.angle = random.randint(-75, 75)
        if random.randint(0, 1):
            self.angle += 180
        
        self.speed = 8

  
    def show(self):
        # Draw ball
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.r, self.r))


    def move(self):
        global scoreLeft, scoreRight, scoreTop, scoreBottom
        self.x += self.speed*cos(radians(self.angle))
        self.y += self.speed*sin(radians(self.angle))
        # Update Score value and set angle
        if self.x + self.r > width - margin:
            scoreLeft += 1
            self.angle = 180 - self.angle
        if self.x < margin:
            scoreRight += 1
            self.angle = 180 - self.angle
        if self.y < margin:
            scoreBottom += 1
            self.angle = -self.angle
        if self.y + self.r  >= height - margin:
            scoreTop += 1
            self.angle = -self.angle

   
    def ball_moving_angle(self):
        # left Paddle Hit
        if self.x < width/2:
            if leftPaddle.x < self.x < leftPaddle.x + leftPaddle.w:
                if leftPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                    self.angle = -45
                if leftPaddle.y + 10 < self.y < leftPaddle.y + 20 or leftPaddle.y + 10 < self.y + self.r< leftPaddle.y + 20:
                    self.angle = -30
                if leftPaddle.y + 20 < self.y < leftPaddle.y + 30 or leftPaddle.y + 20 < self.y + self.r< leftPaddle.y + 30:
                    self.angle = -15
                if leftPaddle.y + 30 < self.y < leftPaddle.y + 40 or leftPaddle.y + 30 < self.y + self.r< leftPaddle.y + 40:
                    self.angle = -10
                if leftPaddle.y + 40 < self.y < leftPaddle.y + 50 or leftPaddle.y + 40 < self.y + self.r< leftPaddle.y + 50:
                    self.angle = 10
                if leftPaddle.y + 50 < self.y < leftPaddle.y + 60 or leftPaddle.y + 50 < self.y + self.r< leftPaddle.y + 60:
                    self.angle = 15
                if leftPaddle.y + 60 < self.y < leftPaddle.y + 70 or leftPaddle.y + 60 < self.y + self.r< leftPaddle.y + 70:
                    self.angle = 30
                if leftPaddle.y + 70 < self.y < leftPaddle.y + 80 or leftPaddle.y + 70 < self.y + self.r< leftPaddle.y + 80:
                    self.angle = 45
        else:
            # Right Paddle Hit
            if rightPaddle.x + rightPaddle.w > self.x  + self.r > rightPaddle.x:
                if rightPaddle.y < self.y < leftPaddle.y + 10 or leftPaddle.y < self.y + self.r< leftPaddle.y + 10:
                    self.angle = -135
                if rightPaddle.y + 10 < self.y < rightPaddle.y + 20 or rightPaddle.y + 10 < self.y + self.r< rightPaddle.y + 20:
                    self.angle = -150
                if rightPaddle.y + 20 < self.y < rightPaddle.y + 30 or rightPaddle.y + 20 < self.y + self.r< rightPaddle.y + 30:
                    self.angle = -165
                if rightPaddle.y + 30 < self.y < rightPaddle.y + 40 or rightPaddle.y + 30 < self.y + self.r< rightPaddle.y + 40:
                    self.angle = 170
                if rightPaddle.y + 40 < self.y < rightPaddle.y + 50 or rightPaddle.y + 40 < self.y + self.r< rightPaddle.y + 50:
                    self.angle = 190
                if rightPaddle.y + 50 < self.y < rightPaddle.y + 60 or rightPaddle.y + 50 < self.y + self.r< rightPaddle.y + 60:
                    self.angle = 165
                if rightPaddle.y + 60 < self.y < rightPaddle.y + 70 or rightPaddle.y + 60 < self.y + self.r< rightPaddle.y + 70:
                    self.angle = 150
                if rightPaddle.y + 70 < self.y < rightPaddle.y + 80 or rightPaddle.y + 70 < self.y + self.r< rightPaddle.y + 80:
                     self.angle = 135

        if self.y < height/2:
            # Top Paddle Hit
            if topPaddle.y < self.y < topPaddle.y + topPaddle.h:
                if topPaddle.x < self.x < topPaddle.x + 10 or topPaddle.x < self.x + self.r< topPaddle.x + 10:
                    self.angle = 45
                if topPaddle.x + 10 < self.x < topPaddle.x + 20 or topPaddle.x + 10 < self.x + self.r< topPaddle.x + 20:
                    self.angle = 30
                if topPaddle.x + 20 < self.x < topPaddle.x + 30 or topPaddle.x + 20 < self.x + self.r< topPaddle.x + 30:
                    self.angle = 15
                if topPaddle.x + 30 < self.x < topPaddle.x + 40 or topPaddle.x + 30 < self.x + self.r< topPaddle.x + 40:
                    self.angle = 10
                if topPaddle.x + 40 < self.x < topPaddle.x + 50 or topPaddle.x + 40 < self.x + self.r< topPaddle.x + 50:
                    self.angle = -10
                if topPaddle.x + 50 < self.x < topPaddle.x + 60 or topPaddle.x + 50 < self.x + self.r< topPaddle.x + 60:
                    self.angle = -15
                if topPaddle.x + 60 < self.x < topPaddle.x + 70 or topPaddle.x + 60 < self.x + self.r< topPaddle.x + 70:
                    self.angle = -30
                if topPaddle.x + 70 < self.x < topPaddle.x + 80 or topPaddle.x + 70 < self.x + self.r< topPaddle.x + 80:
                    self.angle = -45
        else:
            # Bottom Paddle Hit
            if bottomPaddle.y + bottomPaddle.h > self.y  + self.r > bottomPaddle.y:
                if bottomPaddle.x < self.x < topPaddle.x + 10 or topPaddle.x < self.x + self.r< topPaddle.x + 10:
                    self.angle = 135
                if bottomPaddle.x + 10 < self.x < bottomPaddle.x + 20 or bottomPaddle.x + 10 < self.x + self.r< bottomPaddle.x + 20:
                    self.angle = 150
                if bottomPaddle.x + 20 < self.x < bottomPaddle.x + 30 or bottomPaddle.x + 20 < self.x + self.r< bottomPaddle.x + 30:
                    self.angle = 165
                if bottomPaddle.x + 30 < self.x < bottomPaddle.x + 40 or bottomPaddle.x + 30 < self.x + self.r< bottomPaddle.x + 40:
                    self.angle = -170
                if bottomPaddle.x + 40 < self.x < bottomPaddle.x + 50 or bottomPaddle.x + 40 < self.x + self.r< bottomPaddle.x + 50:
                    self.angle = -190
                if bottomPaddle.x + 50 < self.x < bottomPaddle.x + 60 or bottomPaddle.x + 50 < self.x + self.r< bottomPaddle.x + 60:
                    self.angle = -165
                if bottomPaddle.x + 60 < self.x < bottomPaddle.x + 70 or bottomPaddle.x + 60 < self.x + self.r< bottomPaddle.x + 70:
                    self.angle = -150
                if bottomPaddle.x + 70 < self.x < bottomPaddle.x + 80 or bottomPaddle.x + 70 < self.x + self.r< bottomPaddle.x + 80:
                     self.angle = -135

def showScore():
    """
    Display Score in the game windo
    """
    leftScoreText = font.render("LEFT- " + str(scoreLeft), True, white)
    rightScoreText = font.render("RIGHT- " + str(scoreRight), True, white)
    topScoreText = font.render("TOP- " + str(scoreTop), True, white)
    bottomScoreText = font.render("BOTTOM- " + str(scoreBottom), True, white)

    display.blit(leftScoreText, (3*margin, 5*margin))
    display.blit(rightScoreText, (3*margin, 15*margin))
    display.blit(topScoreText, (3*margin, 25*margin))
    display.blit(bottomScoreText, (3*margin, 35*margin))


def gameOver():
    """
    Game will over if any of the pkayer score is equal maxScore=20.
    View Winner Name.
    """
    if scoreLeft == maxScore or \
        scoreRight == maxScore or \
            scoreTop == maxScore or \
                scoreBottom == maxScore:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close()
                    if event.key == pygame.K_r:
                        reset()
            if scoreLeft == maxScore:
                playerWins = largeFont.render("LEFT PLAYER WINDS", True, white)
            elif scoreRight == maxScore:
                playerWins = largeFont.render("RIGHT PLAYER WINDS", True, white)
            elif scoreTop == maxScore:
                playerWins = largeFont.render("TOP PLAYER WINDS", True, white)
            elif scoreBottom == maxScore:
                playerWins = largeFont.render("BOTTOM PLAYER WINDS", True, white)

            display.blit(playerWins, (width/2 - 250, height/2))
            pygame.display.update()

def reset():
    """
    Reset all players score to 0
    """
    global scoreLeft, scoreRight, scoreTop, scoreBottom
    scoreLeft = 0
    scoreRight = 0
    scoreTop = 0
    scoreBottom = 0

def close():
    """
    Exit the game
    """
    pygame.quit()
    sys.exit()