from pong_core import *

def main():
    leftChange = rightChange = topChange = bottomChange = 0
    ball = Ball(ball_color)
    
    while True:
        for event in pygame.event.get():
            # Close Game Main Windo
            if event.type == pygame.QUIT:
                close()
            
            # Other key down
            if event.type == pygame.KEYDOWN:
                # Quit game by "q"
                if event.key == pygame.K_q:
                    close()
                # Reset game score by "r"
                if event.key == pygame.K_r:
                    reset()
                # Set "a" and "z" for Left Paddle
                if event.key == pygame.K_a:
                    leftChange = -1
                if event.key == pygame.K_z:
                    leftChange = 1

                # Set "k" and "m" for Right Paddle
                if event.key == pygame.K_k:
                    rightChange = -1
                if event.key == pygame.K_m:
                    rightChange = 1

                # Set "w" and "e" for Top Paddle
                if event.key == pygame.K_w:
                    topChange = -1
                if event.key == pygame.K_e:
                    topChange = 1

                # Set "o" and "p" for Bottom Paddle
                if event.key == pygame.K_o:
                    bottomChange = -1
                if event.key == pygame.K_p:
                    bottomChange = 1

            # Other key up
            if event.type == pygame.KEYUP:
                leftChange = 0
                rightChange = 0
                topChange = 0
                bottomChange = 0

        # Move all the Paddles based on the key press.
        leftPaddle.move_left_right(leftChange)
        rightPaddle.move_left_right(rightChange)
        topPaddle.move_top_bottom(topChange)
        bottomPaddle.move_top_bottom(bottomChange)

        # Move ball with the right angle.
        ball.move()
        ball.ball_moving_angle() 
        
        display.fill(background)
        showScore()

        # Draw ball in the windo
        ball.show()
        # Draw all the paddles in the windo
        leftPaddle.show()
        rightPaddle.show()
        topPaddle.show()
        bottomPaddle.show()
        
        # Gameover if any of the score is equal to the maxScore.
        gameOver()
        
        pygame.display.update()
        # View 40 F/S 
        clock.tick(40)

if __name__ == '__main__':
    main()
