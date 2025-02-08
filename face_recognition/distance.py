import serial
import pygame
import time
import cv2

# Initialize serial connection
ser = serial.Serial('COM6', 9600)  # Adjust 'COM6' to your serial port

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ultrasonic Sensor Visualization")
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Initialize camera
cap = cv2.VideoCapture(0)

running = True
screen_on = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ser.in_waiting > 0:
        distance = ser.readline().decode('utf-8').strip()
        try:
            distance = float(distance)
        except ValueError:
            continue

        if distance <= 30:
            if not screen_on:
                screen_on = True
        else:
            if screen_on:
                screen_on = False

        if screen_on:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (800, 600))  # Resize frame to fit screen
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)  # Rotate frame 90 degrees counterclockwise
                frame_surface = pygame.surfarray.make_surface(frame)
                screen.blit(frame_surface, (0, 0))
        else:
            screen.fill((0, 0, 0))  # Clear screen

        text = small_font.render(f"{distance} cm", True, (255, 255, 255))
        screen.blit(text, (750 - text.get_width(), 10))  # Position text in the top-right corner
        pygame.display.flip()

    time.sleep(0.1)

cap.release()
pygame.quit()
ser.close()