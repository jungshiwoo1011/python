# -*- coding: utf-8 -*-
import pygame
import random
pygame.init()

user_name = input("name")

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
enemy_speed = 10

bg = pygame.image.load("pygame/source/bg.png")

#스프라이트 불러오기
character = pygame.image.load("pygame/source/character.png")
#스프라이트의 크기와 좌표 세팅하기 (움직임을 상정한 설정)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = screen_width / 2 - character_width / 2
character_yPos = screen_height - character_height

#두번째 스프라이트(적군) 생성
enemy = pygame.image.load("pygame\source\enemy.png")
#적군 스프라이트 크기 및 위치 지정
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = random.randint(0, (screen_width - screen_width))
enemy_yPos = 0

#폰트를 먼저 정해줘야함
game_font = pygame.font.Font(None, 40)

#게임 제한시간
total_time = 0

#시작시간 정보
start_ticks =pygame.time.get_ticks()

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

    enemy_yPos += enemy_speed
    if enemy_yPos > screen_height:
        enemy_yPos = 0
        enemy_speed = random.randint(1, 3)
        enemy_xPos = random.randint(0, screen_width - enemy_width)

    #충돌 처리하기
    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    #충돌이벤트 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌! 충돌!")
        running = False

    #타이머 집어넣기
    #경과시간 계산
    elapsed_time =(pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(f"time : {str(int(total_time + elapsed_time))}", False, (255, 255, 255))
    userName = game_font.render(f"{user_name}'s time", False, (255, 255, 255))

    #screen.fill((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))
    
    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(userName, (10, 10))
    screen.blit(timer, (10, 50))
    
    
    pygame.display.update()

#종료처리
pygame.quit()