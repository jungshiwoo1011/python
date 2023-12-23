import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# 창 크기 설정
width, height = 800, 800
window = pygame.display.set_mode((width, height))

# 배경 이미지 불러오기
background_image = pygame.image.load("pygame/source/bgcristmars.png")  # 배경 이미지 파일 경로 입력
background_image = pygame.transform.scale(background_image, (width, height))

# 눈 이미지 불러오기
snow_image = pygame.image.load("pygame/source/fuckingsnowsnow.png")  # 투명 배경의 눈 이미지 파일 경로 입력
snow_image = pygame.transform.scale(snow_image, (30, 30))  # 이미지 크기 조정



# 눈 생성
snow_list = []
for i in range(300):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    speed = random.randint(1, 3)  # 눈의 속도를 랜덤으로 설정
    snow_list.append([x, y, speed])

# 게임 루프
while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 배경 이미지 표시
    window.blit(background_image, (0, 0))

    # 눈 움직이기
    for i in range(len(snow_list)):
        window.blit(snow_image, (snow_list[i][0], snow_list[i][1]))  # 눈 이미지 표시
        snow_list[i][1] += snow_list[i][2]  # 눈을 아래로 이동시킴

        # 눈이 창 아래로 벗어나면 다시 위로 올리기
        if snow_list[i][1] > height:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, width)

    # 화면 업데이트
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # 초당 프레임 설정
