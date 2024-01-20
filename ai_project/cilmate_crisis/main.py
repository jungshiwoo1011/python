import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("아쿠아베인")

# 폰트 및 이미지 설정
font = pygame.font.Font("c:/Windows/Fonts/malgun.ttf", 36)  # 맑은 고딕 폰트 사용
player_image = pygame.image.load("ai_project/cilmate_crisis/emage/fuckinggoodguy.png")
enemy_image = pygame.image.load("ai_project/cilmate_crisis/emage/motherfucker2.png")
background_image = pygame.image.load("ai_project/cilmate_crisis/emage/fuckingdoor.jpg")

# 배경 이미지 크기를 화면 크기로 조절
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 플레이어 설정
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_speed = 20

# 무기 설정
bullets = []
bullet_speed = 10

# 적 설정
enemies = []
enemy_speed = 10  # 적이 움직이는 속도 조절
enemy_spawn_frequency = 60  # 적 생성 빈도 조절 (숫자가 클수록 적이 적게 나옴)

# 시작 화면 텍스트 및 이미지 설정
intro_text = [
    "2050년 해수면 상승으로 의해 몰디브랑 일본이 잠겼다",
    "그다음으로 우리나라가 잠길 지경이다",
    "이르 지켜본 일론 머스크는 화성으로 이주 하자는 계획을 발표했지만",
    "오직 돈이 많은 극소수만 갈 수 있는 것 이었다",
    "어쩔 수없이 남은 사람들은 개인용 요트나 선박, 고층 건물에서 사는 사람들이 많아졌다",
    "돈이 많은 사람 중 하나는 그냥 바다 아래에다가 자신만의 아지트를 지어 사는 사람도 있다",
    "그렇게 5년이 지난 2055년 나 정우는 고층 아파트에 사는 사람이다",
    "이곳은 높아서 해수면 상승에 대한 두려움이 없는 곳이다",
    "하지만 늘 사람들의 위협에는 문제가 생긴다",
    "그것도 범죄자 같은 사람들. 그 사람들로부터 집을 보호하기 위해 부대에서 가져온 장비들로 처단해야한다"
]

# 게임오버 텍스트 설정
game_over_text = font.render("게임 오버! 스페이스 키를 누르면 재시작", True, red)
game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))

# 텍스트 및 이미지 렌더링
text_y = screen_height // 2 - len(intro_text) * 15
for line in intro_text:
    text = font.render(line, True, white)
    text_rect = text.get_rect(center=(screen_width // 2, text_y))
    screen.blit(text, text_rect)
    text_y += 30

# 시작 화면 업데이트
pygame.display.flip()

# 대기 화면 (5초 동안 표시)
pygame.time.wait(5000)

# 게임 루프
frame_count = 0
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # 배경 그리기
        screen.blit(background_image, (0, 0))

        # 사용자 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_size // 2, player_y])

        # 총알 이동 및 그리기
        for bullet in bullets:
            bullet[1] -= bullet_speed
            pygame.draw.rect(screen, white, [bullet[0], bullet[1], 5, 10])

        # 적 생성
        if frame_count % enemy_spawn_frequency == 0:
            enemy_x = random.randint(0, screen_width - enemy_image.get_width())
            enemy_y = 0
            enemies.append([enemy_x, enemy_y])

        # 적 이동 및 그리기
        for enemy in enemies:
            enemy[1] += enemy_speed
            screen.blit(enemy_image, (enemy[0], enemy[1]))

        # 충돌 체크
        for bullet in bullets:
            for enemy in enemies:
                if (
                    bullet[0] < enemy[0] + enemy_image.get_width()
                    and bullet[0] + 5 > enemy[0]
                    and bullet[1] < enemy[1] + enemy_image.get_height()
                    and bullet[1] + 10 > enemy[1]
                ):
                    bullets.remove(bullet)
                    enemies.remove(enemy)

        # 플레이어 그리기
        screen.blit(player_image, (player_x, player_y))

        # 게임 오버 체크
        for enemy in enemies:
            if enemy[1] >= screen_height - enemy_image.get_height():
                game_over = True

        # 화면 업데이트
        pygame.display.flip()

        # 프레임 카운트 증가
        frame_count += 1

    else:  # 게임 오버 상태
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # 게임 재시작
                game_over = False
                frame_count = 0
                enemies = []
                bullets = []

    pygame.time.Clock().tick(30)
