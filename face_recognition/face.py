import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

try:
    # Initialize camera and face detector
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Font setup for Korean text
    font_path = "C:/Windows/Fonts/gulim.ttc"
    font_size = 36

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 찾을 수 없습니다.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Create background
        if len(faces) >= 2:
            bg = np.zeros_like(frame)
            bg[:] = (0, 0, 255)  # Red background
        else:
            bg = np.zeros_like(frame)  # Black background

        # Process faces and set message
        if len(faces) == 0:
            message = "입장대기중"
        elif len(faces) == 1:
            message = "어서오세요"
            for (x, y, w, h) in faces:
                bg[y:y+h, x:x+w] = frame[y:y+h, x:x+w]
                cv2.rectangle(bg, (x, y), (x+w, y+h), (255, 0, 0), 2)
        else:
            message = "한명씩 입장하세요"
            for (x, y, w, h) in faces:
                bg[y:y+h, x:x+w] = frame[y:y+h, x:x+w]
                cv2.rectangle(bg, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Convert to PIL for Korean text
        pil_img = Image.fromarray(bg)
        draw = ImageDraw.Draw(pil_img)
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text position
        bbox = draw.textbbox((0, 0), message, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = (frame.shape[1] - text_width) // 2
        text_y = (frame.shape[0] - text_height) // 2

        # Draw text
        draw.text((text_x, text_y), message, font=font, fill=(255, 255, 255))
        result = np.array(pil_img)

        cv2.imshow('Face Detection', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()