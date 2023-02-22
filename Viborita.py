import pygame, sys
import random

#Constantes
DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600

class Intro:
    """ Una clase para representar la introduccion y el creador del juego """
    def __init__(self):
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)

        #Fonts & load
        madeBy_font = pygame.font.Font("./Assets/Fonts/Comfortaa-Regular.ttf", 24)
        self.snake_png   = pygame.image.load("./Assets/Images/Intro & Tutorial/Snake.png")

        #Renders
        self.madeBy = madeBy_font.render("Hecho por", True, (0,0,0))
        self.autor  = madeBy_font.render("Delmas Leonardo", True, (0,0,0))

        #Rects
        self.madeBy_rect = self.madeBy.get_rect(center=(400,220))
        self.snake_rect  = self.snake_png.get_rect(center=(400,300))
        self.autor_rect  = self.autor.get_rect(center=(400,380))

    def drawElements(self, monoColor, rgb, timer):
        """ Dibuja los elementos en pantalla """
        if timer < 12:
            self.screen.fill((monoColor, monoColor, monoColor))
        else:
            self.screen.fill(rgb)
        self.screen.blit(self.madeBy, self.madeBy_rect)
        self.screen.blit(self.snake_png, self.snake_rect)
        self.screen.blit(self.autor, self.autor_rect)
        self.madeBy.set_alpha(monoColor)
        self.snake_png.set_alpha(monoColor)
        self.autor.set_alpha(monoColor)
    
    def updateRGB(self, red, green, blue):
        """ Devuelve los valores actualizados de las variables rgb """
        if red < 255:
            red += 1
        if green < 50:
            green += 1
        if blue < 50:
            blue += 1
        return (red,green,blue)

    def updateMonochrome(self, monoColor, timer):
        """ Devuelve los valores actualizados de la variable monoColor """
        if monoColor < 255 and timer < 6:
            return monoColor + 1
        elif monoColor > 0 and timer > 6:
            return monoColor - 1
        else:
            return monoColor

    def run(self):

        monoColor = 0
        timer = 0
        rgb = (0,0,0)
        fps = pygame.time.Clock()
        self.snake_png.set_alpha(0)

        while timer < 18:

            fps.tick(60)
            timer = pygame.time.get_ticks() // 1000 #Milisegundos a segundos
            pygame.display.update()
            self.drawElements(monoColor, rgb, timer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if timer < 12:
                monoColor = self.updateMonochrome(monoColor, timer) #Negro -> Blanco (& viceversa)
            elif timer > 12:
                rgb = self.updateRGB(rgb[0], rgb[1], rgb[2]) #Negro -> Rojo

class Tutorial:
    """ Una clase para representar las instrucciones y controles del juego """
    def __init__(self):
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)

        #Fonts & load
        skip_font         = pygame.font.Font("./Assets/Fonts/Pixel Sans Serif.ttf", 12)
        self.controls_png = pygame.image.load("./Assets/Images/Intro & Tutorial/InstructionsControls.png")
        self.lose_png     = pygame.image.load("./Assets/Images/Intro & Tutorial/InstructionsLose.png")
        self.win_png      = pygame.image.load("./Assets/Images/Intro & Tutorial/InstructionsWin.png")

        #Renders
        self.skip = skip_font.render('"Esc" para saltar el tutorial', True, (0,0,0))

        #Rects
        self.controls_png_rect = self.controls_png.get_rect(topleft=(0,0))
        self.lose_png_rect     = self.lose_png.get_rect(topleft=(0,0))
        self.win_png_rect      = self.win_png.get_rect(topleft=(0,0))
        self.skip_rect         = self.skip.get_rect(topleft=(480,570))

    def drawElements(self, rgb, timer):
        """ Dibuja los elementos en pantalla """
        self.screen.fill(rgb)
        if timer < 28:
            self.screen.blit(self.controls_png, self.controls_png_rect)
        elif timer < 38:
            self.screen.blit(self.lose_png, self.lose_png_rect)
        elif timer < 48:
            self.screen.blit(self.win_png, self.win_png_rect)
        if ((timer % 2 ) == 0) and (timer < 48):
            self.screen.blit(self.skip, self.skip_rect)

    def updateRGB(self, red, green, blue):
        """ Devuelve los valores actualizados de las variables rgb """
        if red > 80:
            red -= 1
        if green < 180:
            green += 1
        if blue < 100:
            blue += 1
        return (red,green,blue)

    def run(self):

        timer = 0
        loadingXCoords = -799
        rgb = (255,50,50)
        fps = pygame.time.Clock()

        while timer < 52:
                            
            fps.tick(60)
            pygame.display.update()
            timer = pygame.time.get_ticks() // 1000 #Milisegundos a segundos
            self.drawElements(rgb, timer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        timer = 999

            if timer < 48:
                pygame.draw.rect(self.screen, (0, 0, 0), (loadingXCoords, 596 , 800, 12))
                loadingXCoords += 0.44

            if (timer > 48) and (timer < 52):
                rgb = self.updateRGB(rgb[0], rgb[1], rgb[2])

class Snake:
    """ Una clase para representar a la vibora """
    def __init__(self, screen):
        self.setCoords()
        self.screen = screen
    
    def setCoords(self):
        """ Inicializa las coordenadas y direccion de la vibora """
        self.coords = [(40,300),(20,300)]
        self.dir = ["Right","Right"]
    
    def drawSnake(self):
        """ Dibuja la cola, cuerpo y cabeza de la serpiente en pantalla """
        self.head = pygame.image.load("./Assets/Images/Snake/SnakeHead"+self.dir[0]+".png").convert_alpha()
        self.head_rect = self.head.get_rect(topleft=self.coords[0])
        self.screen.blit(self.head, self.head_rect)
        for i in range(1,len(self.coords)-1):
            if self.dir[i] == self.dir[i+1]:
                self.body = pygame.image.load("./Assets/Images/Snake/SnakeBody"+self.dir[i]+".png").convert_alpha()
            else:
                turnPoint = {("Right","Up"):"TL_CW"  , ("Up","Right"):"BR_CCW",
                             ("Down","Right"):"TR_CW", ("Right","Down"):"BL_CCW",
                             ("Left","Down"):"BR_CW" , ("Down","Left"):"TL_CCW",
                             ("Up","Left"):"BL_CW"   , ("Left","Up"):"TR_CCW"}
                self.body = pygame.image.load("./Assets/Images/Snake/SnakeBody"+turnPoint[(self.dir[i],self.dir[i+1])]+".png").convert_alpha()

            self.body_rect = self.body.get_rect(topleft=self.coords[i])
            self.screen.blit(self.body, self.body_rect)

        last_index = len(self.coords) - 1
        self.tail = pygame.image.load("./Assets/Images/Snake/SnakeTail"+self.dir[last_index]+".png")
        self.tail_rect = self.tail.get_rect(topleft=self.coords[last_index])
        self.screen.blit(self.tail, self.tail_rect)
    
    def moveRight(self):
        self.dir[0] = "Right"
    def moveDown(self):
        self.dir[0] = "Down"
    def moveLeft(self):
        self.dir[0] = "Left"
    def moveUp(self):
        self.dir[0] = "Up"
    
    def move(self):
        """ Mueve de casillero a la vibora dependiendo de la direccion actual de esta """
        coordsCopy = self.coords[:-1]
        dirCopy = self.dir[:-1]

        if self.dir[0] == "Right":
            coordsCopy.insert(0,((coordsCopy[0][0] + 20),coordsCopy[0][1]))
            dirCopy.insert(0,"Right")
        elif self.dir[0] == "Down":
            coordsCopy.insert(0,(coordsCopy[0][0],(coordsCopy[0][1] + 20)))
            dirCopy.insert(0,"Down")
        elif self.dir[0] == "Left":
            coordsCopy.insert(0,((coordsCopy[0][0] - 20),coordsCopy[0][1]))
            dirCopy.insert(0,"Left")
        elif self.dir[0] == "Up":
            coordsCopy.insert(0,(coordsCopy[0][0],(coordsCopy[0][1] - 20)))
            dirCopy.insert(0,"Up")

        self.coords = coordsCopy[:]
        self.dir = dirCopy[:]
        
    def eatFood(self):
        """ Aumenta el tamanio de la vibora """
        self.coords.append([None,None])
        self.dir.append(None)
        self.eatSound()

    def eatSound(self):
        """ Reproduce un sonido de comer """
        random_sound = str(random.choice(["LD","BM","LA","LG","JG","JS","BD","CA"]))
        eat_sound = pygame.mixer.Sound("./Assets/Sounds/Eat"+random_sound+".wav")
        eat_sound.set_volume(0.4)
        eat_sound.play()

class Food:
    """ Una clase para representar la comida """
    def __init__(self, screen, snake_coords):
        self.newCoords(snake_coords)
        self.random_food = str(random.choice(["Apple","Banana","Brine","Orange"]))
        self.screen = screen
    
    def drawFood(self):
        """ Dibuja la comida en pantalla """
        self.food_png = pygame.image.load("./Assets/Images/Food/"+self.random_food+".png")
        self.food_rect_png = self.food_png.get_rect(topleft=(self.x,self.y))
        self.screen.blit(self.food_png, self.food_rect_png)

    def newFood(self, snake_coords):
        """ Genera nueva comida """
        self.random_food = str(random.choice(["Apple","Banana","Brine","Orange"]))
        self.newCoords(snake_coords)
    
    def newCoords(self, snake_coords):
        """ Genera nuevas coordenadas para la comida """
        self.x = random.randint(1,((DISPLAY_WIDTH//20)-2)) * 20
        self.y = random.randint(1,((DISPLAY_HEIGHT//20)-2)) * 20
        while (self.x,self.y) in snake_coords:
            self.x = random.randint(1,((DISPLAY_WIDTH//20)-2)) * 20
            self.y = random.randint(1,((DISPLAY_HEIGHT//20)-2)) * 20

class Score:
    """ Una clase para representar el puntaje """
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.record = 0

    def increaseScore(self):
        """ Aumenta el puntaje """
        self.score += 1

    def resetScore(self):
        """ Reinicia el puntaje """
        if self.isRecord(): self.record = self.score
        self.score = 0
    
    def isRecord(self):
        """ Valida si el puntaje actual supero al puntaje record """
        if (self.score > self.record):
            return True
        else:
            return False

    def drawScore(self):
        """ Dibuja el puntaje en pantalla """
        pygame.draw.rect(self.screen, (0,0,0), (728,558,60,30), border_radius=8, width=1)
        score_font = pygame.font.Font(None, 24)
        score_text = score_font.render(str(self.score), True, (0,0,0))
        score_rect = score_text.get_rect(center=(757,574))

        self.screen.blit(score_text, score_rect)

class Pause:
    """ Una clase para disponer de una pausa en mitad de la partida de juego """
    def __init__(self, screen):
        self.screen = screen

        #Fonts & load
        pause_font    = pygame.font.Font("./Assets/Fonts/Sunny Spells.ttf", 128)
        continue_font = pygame.font.Font("./Assets/Fonts/Comfortaa-Regular.ttf", 36)
        self.shadow_png    = pygame.image.load("./Assets/Images/Intro & Tutorial/Shadow.png")

        #Renders
        self.pauseText       = pause_font.render("PAUSA", True, (150,200,255))
        self.continueText    = continue_font.render('"ESC"   para reanudar el juego', True, (255,255,255))
        
        #Rects
        self.pause_rect      = self.pauseText.get_rect(center=(400,150))
        self.continue_rect   = self.continueText.get_rect(center=(400,400))
        self.shadow_rect_png = self.shadow_png.get_rect(topleft=(0,0))

        self.shadow_png.set_alpha(100)

    def drawElements(self):
        """ Dibuja los elementos en pantalla """
        self.screen.blit(self.shadow_png, self.shadow_rect_png)
        self.screen.blit(self.pauseText, self.pause_rect)
        self.screen.blit(self.continueText, self.continue_rect)
    
    def main(self):

        pause = True
        self.drawElements()
        clock = pygame.time.Clock()

        while pause:

            clock.tick(60)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE):
                        pause = False

class GameOver:
    """ Una clase para representar el fin del juego """
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score

    def updateScoreRGB(self, red, green, blue):
        """ Devuelve los valores actualizados de las variables rgb """
        if (red >= 0 and red <= 255):
            if green == 0:
                if red < 255: red += 1
            elif green == 255:
                if red > 0: red -= 1
        if (green >= 0 and green <= 255):
            if blue == 0:
                if green < 255: green += 1
            elif blue == 255:
                if green > 0: green -= 1
        if (blue >= 0 and blue <= 255):
            if red == 0:
                if blue < 255: blue += 1
            elif red == 255:
                if blue > 0: blue -= 1
        return (red,green,blue)

    def main(self):

        #Fonts & load
        gameOver_font   = pygame.font.Font("./Assets/Fonts/Sunny Spells.ttf", 128)
        continue_font   = pygame.font.Font("./Assets/Fonts/Comfortaa-Regular.ttf", 36)
        scoreCount_font = pygame.font.Font("./Assets/Fonts/Comfortaa-Regular.ttf", 48)
        shadow_png      = pygame.image.load("./Assets/Images/Intro & Tutorial/Shadow.png")

        #Renders
        gameOver      = gameOver_font.render("FIN DEL JUEGO", True, (255,175,175))
        scoreText     = continue_font.render("Tu puntaje fue de:", True, (255,255,255))
        scoreCount    = scoreCount_font.render(str(self.score.score), True, (255,255,255))
        continueText1 = continue_font.render('"ENTER"   para jugar otra vez', True, (255,255,255))
        continueText2 = continue_font.render('  "ESC"     para salir del juego', True, (255,255,255))

        #Rects
        gameOver_rect   = gameOver.get_rect(center=(400,100))
        score_rect      = scoreText.get_rect(center=(400,200))
        scoreCount_rect = scoreCount.get_rect(center=(400,300))
        continue_rect1  = continueText1.get_rect(topleft=(140,410))
        continue_rect2  = continueText2.get_rect(topleft=(144,490))
        shadow_rect_png = shadow_png.get_rect(topleft=(0,0))

        shadow_png.set_alpha(100)

        #Draw text & other
        self.screen.blit(shadow_png, shadow_rect_png)
        self.screen.blit(gameOver, gameOver_rect)
        pygame.draw.rect(self.screen, (0,0,0), (310,265,180,60), border_radius=5, width=0)
        pygame.draw.rect(self.screen, (255,255,255), (310,265,180,60), border_radius=5, width=2)
        self.screen.blit(scoreText, score_rect)
        self.screen.blit(scoreCount, scoreCount_rect)
        self.screen.blit(continueText1, continue_rect1)
        self.screen.blit(continueText2, continue_rect2)

        pause = True
        rgb = (255,0,0)
        clock = pygame.time.Clock()
        record = self.score.isRecord()
        UPDATE_SCORE_COLOR = pygame.USEREVENT
        pygame.time.set_timer(UPDATE_SCORE_COLOR,5)

        while pause:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == UPDATE_SCORE_COLOR and record:
                    rgb = self.updateScoreRGB(rgb[0],rgb[1],rgb[2])
                    scoreCount = scoreCount_font.render(str(self.score.score), True, rgb)
                    newRecordText = continue_font.render("¡Nuevo record!", False, rgb)
                    newRecordText_rect = newRecordText.get_rect(center=(400,350))
                    pygame.draw.rect(self.screen, rgb, (310,265,180,60), border_radius=5, width=2)
                    self.screen.blit(newRecordText, newRecordText_rect)
                    self.screen.blit(scoreCount, scoreCount_rect)
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_RETURN):
                        pause = False
                    elif (event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    break

            pygame.display.flip()

class Game:
    """ Una clase para representar el juego """
    def __init__(self):
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.snake = Snake(self.screen)
        self.score = Score(self.screen)
        self.food = Food(self.screen, self.snake.coords)
        self.pause = Pause(self.screen)
        self.gameOver = GameOver(self.screen, self.score)

    def retry(self):
        """ Reinicia los valores de todos los elementos por defecto para una nueva partida """
        self.generateTerrain()
        self.score.resetScore()
        self.snake.setCoords()
        self.food.newFood(self.snake.coords)

    def cornerCollision(self):
        """ Valida si hubo colision entre la vibora y una esquina de la pantalla """
        if self.snake.coords[0][0] > DISPLAY_WIDTH - 40:
            return True
        elif self.snake.coords[0][1] > DISPLAY_HEIGHT - 40:
            return True
        elif self.snake.coords[0][0] < 20:
            return True
        elif self.snake.coords[0][1] < 20:
            return True
        return False

    def selfCollision(self):
        """ Valida si hubo colision entre la vibora y ella misma """
        for pos in range(len(self.snake.coords) - 1):
            snake_head = (self.snake.coords[0][0], self.snake.coords[0][1])
            snake_body = (self.snake.coords[pos+1][0], self.snake.coords[pos+1][1])
            if snake_head == snake_body:
                return True
        return False

    def isLimit(self, x, y):
        """ Valida si las coordenadas pasadas por parametro se encuentran en las casillas limites de la pantalla """
        if (x >= 20 and x < DISPLAY_WIDTH-20) and (y >= 20 and y < DISPLAY_HEIGHT-20):
            return False
        return True

    def generateTerrain(self):
        """ Genera un terreno con casillas de hierba aleatorias """
        self.terrainPaths = {}
        corners = {(0,0):"./Assets/Images/Terrain/Wall TL.png",
                   ((DISPLAY_WIDTH-20),0):"./Assets/Images/Terrain/Wall TR.png",
                   (0,(DISPLAY_HEIGHT-20)):"./Assets/Images/Terrain/Wall BL.png",
                   ((DISPLAY_WIDTH-20),(DISPLAY_HEIGHT-20)):"./Assets/Images/Terrain/Wall BR.png"}

        for x in range(0,DISPLAY_WIDTH,20):
            for y in range(0,DISPLAY_HEIGHT,20):
                if self.isLimit(x, y) == False:
                    random_num = str(random.choices([0,1,2,3,4], weights=(80,10,4,3,1))[0])
                    path = "./Assets/Images/Terrain/Grass " + random_num + ".png"
                elif (x,y) in corners:
                    path = corners[(x,y)]
                else:
                    if (x == 0) and (y > 0):
                        path = "./Assets/Images/Terrain/Wall L.png" # relleno IZQUIERDA
                    elif (x > 0) and (y == 0):
                        path = "./Assets/Images/Terrain/Wall T.png" # relleno ARRIBA
                    elif (x == DISPLAY_WIDTH-20) and (y > 0):
                        path = "./Assets/Images/Terrain/Wall R.png" # relleno DERECHA
                    elif (x > 0) and (y == DISPLAY_HEIGHT-20):
                        path = "./Assets/Images/Terrain/Wall B.png" # relleno ABAJO

                self.terrainPaths[(x,y)] = pygame.image.load(path)

    def drawTerrain(self):
        """ Dibuja el terreno generado en pantalla """
        for key, value in self.terrainPaths.items():
            self.grass_rect = value.get_rect(topleft=key)
            self.screen.blit(value, self.grass_rect)

    def drawElements(self):
        """ Dibuja los elementos en pantalla """
        self.drawTerrain()
        self.food.drawFood()
        self.snake.drawSnake()
        self.score.drawScore()

    def countdown(self):
        """ Realiza y dibuja en pantalla una cuenta regresiva """
        TIMER_EVENT = pygame.USEREVENT+1
        pygame.time.set_timer(TIMER_EVENT,1000)

        countdown_font = pygame.font.Font(None, 256)

        counter = 3

        self.drawElements()
        countdown_text = countdown_font.render(str(counter), True, (0,0,0))
        countdown_rect = countdown_text.get_rect(center=(DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
        self.screen.blit(countdown_text, countdown_rect)
        
        clock = pygame.time.Clock()
        while counter > 0:

            clock.tick(30)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == TIMER_EVENT:
                    counter -= 1
                    self.drawElements()
                    countdown_text = countdown_font.render(str(counter), True, (0,0,0))
                    countdown_rect = countdown_text.get_rect(center=(DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
                    self.screen.blit(countdown_text, countdown_rect)
                    if counter == 0:
                        pygame.time.set_timer(TIMER_EVENT, 0)
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def main(self):

        clock = pygame.time.Clock()
        self.generateTerrain()
        self.countdown()

        while True:

            self.drawElements()
            pygame.display.flip()
            clock.tick(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.dir[0] != "Down":
                        self.snake.moveUp()
                    elif event.key == pygame.K_DOWN and self.snake.dir[0] != "Up":
                        self.snake.moveDown()
                    elif event.key == pygame.K_RIGHT and self.snake.dir[0] != "Left":
                        self.snake.moveRight()
                    elif event.key == pygame.K_LEFT and self.snake.dir[0] != "Right":
                        self.snake.moveLeft()
                    elif (event.key == pygame.K_ESCAPE):
                        self.pause.main()
                    break

            if self.food.food_rect_png.colliderect(self.snake.head_rect):
                self.food.newFood(self.snake.coords)
                self.snake.eatFood()
                self.score.increaseScore()

            if self.cornerCollision() or self.selfCollision():
                self.gameOver.main()
                self.retry()
                self.countdown()

            self.snake.move()

if __name__ == '__main__':
    pygame.init()
    intro = Intro()
    tutorial = Tutorial()
    game = Game()
    
    icon = pygame.image.load("./Assets/Images/snakeLogo.png")
    pygame.display.set_caption("Viborita")
    pygame.display.set_icon(icon)
    
    intro.run()
    tutorial.run()
    game.main()