import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import serial
import time
import threading

class DoorLock:
    def __init__(self, master):
        self.master = master
        self.master.title("도어락")
        self.password = "1234"  # 초기 비밀번호 설정
        self.input_password = ""
        self.star_count = 0  # '*' 버튼 누른 횟수
        self.change_mode = False  # 비밀번호 변경 모드 여부
        self.verify_old = False  # 기존 비밀번호 확인 모드 여부
        self.reset_timer = None  # 타이머 초기화
        self.registered_face_path = "registered_face.jpg"  # 등록된 얼굴 이미지 경로
        try:
            self.arduino = serial.Serial('COM9', 9600)  # 아두이노와 시리얼 통신 설정 (포트 번호는 환경에 맞게 변경)
            time.sleep(2)  # 시리얼 통신 안정화 대기
        except serial.SerialException as e:
            print(f"오류: 아두이노 연결 실패: {e}")
            self.arduino = None
        self.face_detected = False  # 얼굴 인식 여부
        
        self.create_widgets()
        self.setup_camera()
        self.start_serial_thread()

    def create_widgets(self):
        self.display = tk.Label(self.master, text="", font=("Helvetica", 18))
        self.display.grid(row=1, column=0, columnspan=3, pady=10)

    def setup_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.detect_face(frame)
        self.master.after(10, self.update_frame)

    def detect_face(self, frame):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            self.face_detected = True
            self.display.config(text="비밀번호를 누르세요")
        else:
            self.face_detected = False
            self.display.config(text="")

    def register_face(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite(self.registered_face_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            print("성공: 얼굴이 등록되었습니다!")

    def button_click(self, value):
        if not self.face_detected:
            return
        if self.arduino:
            self.arduino.write(b'B')  # 버튼 누를 때 비프음
        self.reset_input_timer()
        if value == '#':
            if self.change_mode:
                if self.verify_old:
                    self.verify_old_password()
                else:
                    self.verify_new_password()
            else:
                self.check_password()
        elif value == '*':
            self.star_count += 1
            if self.star_count == 3:
                self.prompt_old_password()
                self.star_count = 0
        else:
            self.input_password += value
            self.display.config(text=f"입력된 비밀번호: {self.input_password}")

    def check_password(self):
        if self.input_password.endswith(self.password):
            print("성공: 문이 열렸습니다!")
            self.display.config(text="어서오세요")
            if self.arduino:
                self.arduino.write(b'O')  # 아두이노로 문 열림 신호 전송
            self.master.after(3000, self.reset_display)
        else:
            print("오류: 비밀번호가 틀렸습니다!")
        self.reset_input()

    def prompt_old_password(self):
        self.change_mode = True
        self.verify_old = True
        self.display.config(text="기존 비밀번호를 입력하세요")

    def verify_old_password(self):
        if self.input_password == self.password:
            self.input_password = ""
            self.display.config(text="새 비밀번호를 입력하세요")
            self.verify_old = False
        else:
            self.display.config(text="기존 비밀번호가 틀렸습니다!")
            self.change_mode = False
            self.verify_old = False
        self.reset_input()

    def verify_new_password(self):
        new_password = self.input_password
        if len(new_password) >= 4:
            self.password = new_password[-4:]  # 비밀번호의 뒷자리 4자리만 저장
            self.display.config(text="비밀번호가 변경되었습니다!")
        else:
            self.display.config(text="비밀번호는 최소 4자리여야 합니다!")
        self.change_mode = False
        self.reset_input()

    def reset_input(self):
        self.input_password = ""

    def reset_input_timer(self):
        if self.reset_timer:
            self.master.after_cancel(self.reset_timer)
        self.reset_timer = self.master.after(5000, self.reset_input)

    def reset_display(self):
        self.display.config(text="")
        if self.arduino:
            self.arduino.write(b'R')  # 아두이노로 서보모터 원래 위치로 복귀 신호 전송

    def start_serial_thread(self):
        if self.arduino:
            thread = threading.Thread(target=self.read_serial)
            thread.daemon = True
            thread.start()

    def read_serial(self):
        while True:
            if self.arduino and self.arduino.in_waiting > 0:
                try:
                    data = self.arduino.read().decode('utf-8', errors='ignore').strip()
                    self.master.after(0, self.button_click, data)
                except UnicodeDecodeError:
                    print("오류: 유효하지 않은 데이터 수신")

    def on_closing(self):
        if self.cap.isOpened():
            self.cap.release()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DoorLock(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()