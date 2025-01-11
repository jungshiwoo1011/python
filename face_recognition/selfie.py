import cv2
import numpy as np
import time
import os
from datetime import datetime

def take_photos():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return []

    photos = []

    while len(photos) < 4:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow('Press Space to Take Photo', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            photos.append(frame)
            print(f'Photo {len(photos)} taken')
            time.sleep(1)  # Wait for 1 second before taking the next photo

    cap.release()
    cv2.destroyAllWindows()
    return photos

def create_collage(photos, layout):
    if len(photos) != 4:
        print("Error: Need exactly 4 photos to create a collage.")
        return None

    height, width = photos[0].shape[:2]

    if layout == '1x4':
        collage = np.zeros((height * 4, width, 3), dtype=np.uint8)
        for i in range(4):
            collage[i * height:(i + 1) * height, 0:width] = photos[i]
    elif layout == '2x2':
        collage = np.zeros((height * 2, width * 2, 3), dtype=np.uint8)
        collage[0:height, 0:width] = photos[0]
        collage[0:height, width:width * 2] = photos[1]
        collage[height:height * 2, 0:width] = photos[2]
        collage[height:height * 2, width:width * 2] = photos[3]
    else:
        print("Error: Invalid layout.")
        return None

    return collage

def save_collage(collage, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    collage_path = os.path.join(folder_path, f'photo_booth_collage_{timestamp}.jpg')
    cv2.imwrite(collage_path, collage)
    print(f"Collage saved as '{collage_path}'")

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    print("Press 'Q' for 1x4 layout or 'W' for 2x2 layout.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.putText(frame, "Press 'Q' for 1x4 layout or 'W' for 2x2 layout", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('Layout Selection', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            layout = '1x4'
            break
        elif key == ord('w'):
            layout = '2x2'
            break

    cap.release()
    cv2.destroyAllWindows()

    photos = take_photos()
    if len(photos) == 4:
        collage = create_collage(photos, layout)
        if collage is not None:
            folder_path = 'c:/Users/hjk99/Desktop/0111/face_recognition'
            save_collage(collage, folder_path)
            cv2.imshow('Photo Booth Collage', collage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        print("Error: Not enough photos taken.")

if __name__ == '__main__':
    main()