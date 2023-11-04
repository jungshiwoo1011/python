# -*- coding: utf-8 -*-
import pygame
pygame.init()
import random

#화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("정시우 스파이더맨")

#FPS
clock = pygame.time.Clock()

#이동속도 고정해주기
character_speed = 1

bg = pygame.image.load("pygame/source/bg.png")

#스프라이트 불러오기
character = pygame.image.load("pygame/source/character.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height / 2)- (character_height / 2)

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프 - 종료까지 대기
running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #추가한 이미지들을 화면에 띄우기
    character_xPos += to_x * dt
    character_yPos += to_y * dt

    # 가로 스크린내 안벗어나게
    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    # 가로 스크린내 안벗어나게
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height
        
    #screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    
    
    pygame.display.update()

#종료처리
pygame.quit()