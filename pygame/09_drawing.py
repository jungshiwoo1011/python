import pygame
import random
pygame.init()

#화면크기 설정
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("정시우 스파이더맨")

#FPS
clock = pygame.time.Clock()

#이벤트 루프 - 종료까지 대기
r = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #배경색 설정
    screen.fill((255, 255, 255))

    #직선그리기
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (screen_width, screen_height), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, screen_height), (screen_width, 0), 5)

    #measure = screen_width / 10

    #for i in range(10):
        #pygame.draw.line(screen, (0, 0, 0), (0, i*measure), (screen_height, i*measure), 2)
        #pygame.draw.line(screen, (0, 0, 0), (i*measure, 0), (i*measure, screen_width), 2)

    #pygame.draw.circle(screen, (0, 255, 100), (screen_width / 2, screen_height / 2), 100)
    
    #pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (screen_width / 2, screen_height / 2), r, 5)
    #r += 10
    #if r > 250:
        #r = 20

    #pygame.draw.rect(screen, (55, 55, 255), (screen_width / 2, screen_height / 2, 100, 100))
    pygame.draw.rect(screen, (155, 155, 55), (screen_width / 2, screen_height / 2, r, r), 5)
    r += 10
    if r > 250:
        r = 20



    pygame.display.update()

#종료처리
pygame.quit()