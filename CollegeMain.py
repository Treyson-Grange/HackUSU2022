# main file


import pygame
import sys
import random
from functions import enemyFunctions
from functions import attackFunctions
from functions import helperFunctions

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('College Simulator')
clock = pygame.time.Clock()
BACKGROUND_COLOR = (0, 0, 0)
fps = 25

width = 40
height = 60
vel = 8

level = 1
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1)
attackList = []
playerHealth = 50

font = pygame.font.Font("Assets/Fonts/Pixeltype.ttf",75)
gameDone = False

while not gameDone:
    numLevels = 0
    yearPlaceHolder = 1
    classPlaceHolder = 1

    while True:
        event = pygame.event.wait()
        playerHealth = 50
        attackList = []
        healList = []
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:

                # levelDone = False
                break
        else:
            screen.fill((94, 129, 162))
            title_message = font.render("College Simulator", True, (0,0,0))
            title_message_rect = title_message.get_rect(center=(300, 300))
            play_message = font.render("Hit Enter To Play", False, (0,0,0))
            play_message_rect = play_message.get_rect(center = (300,350))
            duckie_menu = pygame.transform.scale(pygame.image.load('Assets/Sprites/duckie3.0.png'),(200,200))
            duckie_menu_rect = duckie_menu.get_rect(center = (400,400))

            screen.blit(title_message, (225, 100))
            screen.blit(play_message,(225,200))
            screen.blit(duckie_menu, duckie_menu_rect)

            pygame.display.update()

    levelDone = False
    numAttacks = 0
    while not levelDone:
        #level loop



        attackDone = False
        x = 50
        y = 275
        player_surf = pygame.transform.scale(pygame.image.load("Assets/Sprites/Protagonist2.png"),(50,70)).convert_alpha()
        player_rect = player_surf.get_rect(center = (x,y))

        # attack_surf = pygame.image.load(attackSprite)
        # heal_surf = pygame.image.load("Assets/Sprites/EnergyDrink.png")

        # levelTimer = 20
        levelTimer = helperFunctions.getNumBullets(numLevels, numAttacks)


        while not attackDone:
            #attack loop
            enemySprite = helperFunctions.getEnemySprite(numLevels)
            quotes = helperFunctions.getQuotes(numLevels)
            attackSprite = helperFunctions.getAttackSprite(numLevels, numAttacks)

            attack_surf = pygame.image.load(attackSprite)
            heal_surf = pygame.image.load("Assets/Sprites/EnergyDrink.png")


            #amount of bullets
            #speed of bullets
            #amount of health items


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    attackDone = True

            keys = pygame.key.get_pressed()

            if len(attackList) != 0:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    player_rect.x -= vel
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    player_rect.x += vel
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    player_rect.y -= vel
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    player_rect.y += vel

            if player_rect.y < 65:
                player_rect.y = 65
            if player_rect.y > 525:
                player_rect.y = 525
            if player_rect.x > 600:
                player_rect.x = 600
            if player_rect.x < 0:
                player_rect.x = 0

            screen.fill(BACKGROUND_COLOR)

            if event.type == timer:
                delay = random.random()
                if delay < .1:
                    if levelTimer != 0:
                        attackList.append(attack_surf.get_rect(center = (random.randint(900,1100),random.randint(100,525))))
                        levelTimer = levelTimer - 1
                        if levelTimer % 6 == 0:
                            healList.append(
                                heal_surf.get_rect(center=(random.randint(900, 1100), random.randint(100, 525))))
                        # print(len(attackList))
                    else:
                        # print(attackList[len(attackList) - 1].x)
                        if attackList[len(attackList) - 1].x <= 0:
                            attackDone = True


            #HealthBar
            #pygame.draw.rect(screen, REdm player_pos[0], width, height))
            pygame.draw.rect(screen, (0,255,0), (10 , 10, playerHealth * 8, 50))
            UI_text = font.render('Sleep',False,(255,255,255))
            UI_text_rect = UI_text.get_rect(center = (75,40))
            levelString = 'Year : ' + str(yearPlaceHolder)
            level_text = font.render(levelString,False,(255,255,255))
            level_text_rect = level_text.get_rect(center = (500, 40))
            classString = 'Class : ' + str(classPlaceHolder)
            level_text_class = font.render(classString,False,(255,255,255))
            level_text_class_rect = level_text_class.get_rect(center = (690,40))

            screen.blit(level_text_class,level_text_class_rect)
            screen.blit(level_text,level_text_rect)
            screen.blit(UI_text,UI_text_rect)
            screen.blit(player_surf,player_rect)
            enemyFunctions.generateEnemy(screen, numAttacks, quotes, enemySprite)
            attackFunctions.attackMovement(attackList,screen,attack_surf)
            attackFunctions.healMovement(healList, screen, heal_surf)


            pygame.display.update()
            clock.tick(30)

            playerHealth = attackFunctions.collisions(player_rect, attackList, playerHealth)
            playerHealth = attackFunctions.heal(player_rect, healList, playerHealth)
            if playerHealth <= 0:
                attackDone = True
                levelDone = True

        classPlaceHolder += 1
        numAttacks = numAttacks + 1


        if numAttacks == 4:
            numAttacks = 0
            yearPlaceHolder += 1
            classPlaceHolder = 1
            # levelDone = True
            numLevels = numLevels + 1

            # place tempmenue here?
            while True:
                event = pygame.event.wait()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        break
                else:
                    screen.fill((94, 129, 162))
                    title_message = font.render("Level Complete!", True, (0, 0, 0))
                    title_message_rect = title_message.get_rect(center=(300, 300))
                    play_message = font.render("Hit Enter To continue", False, (0, 0, 0))
                    play_message_rect = play_message.get_rect(center=(300, 350))
                    # duckie_menu = pygame.transform.scale(pygame.image.load('Assets/Sprites/duckie3.0.png'), (200, 200))
                    # duckie_menu_rect = duckie_menu.get_rect(center=(400, 400))

                    screen.blit(title_message, (225, 100))
                    screen.blit(play_message, (225, 200))
                    # screen.blit(duckie_menu, duckie_menu_rect)

                    pygame.display.update()

    # numLevels = numLevels + 1

        if numLevels == 4:
            levelDone = True

            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        break
                else:
                    screen.fill((94, 129, 162))
                    title_message = font.render("you got your degree!!!", True, (0, 0, 0))
                    title_message_rect = title_message.get_rect(center=(300, 300))
                    play_message = font.render("", False, (0, 0, 0))
                    play_message_rect = play_message.get_rect(center=(300, 350))
                    duckie_menu = pygame.transform.scale(pygame.image.load('Assets/Sprites/diploma.png'), (200, 200))
                    duckie_menu_rect = duckie_menu.get_rect(center=(400, 400))

                    screen.blit(title_message, (225, 100))
                    screen.blit(play_message, (225, 200))
                    screen.blit(duckie_menu, duckie_menu_rect)

                    pygame.display.update()


pygame.quit()
