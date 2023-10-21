# -*- coding: utf-8 -*-
import pygame
pygame.init()

#화면크기 설정
screen_width = 1920
screen_height = 1020
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (제목창)
pygame.display.set_caption("정시우 존잘")

#이벤트 루프 - 종료까지 대기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#종료처리
pygame.quit()