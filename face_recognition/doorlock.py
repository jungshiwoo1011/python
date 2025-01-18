import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
from deepface import DeepFace

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
        
        self.create_widgets()
        self.setup_camera()

    def create_widgets(self):
        self.display = tk.Entry(self.master, width=30, font=("Helvetica", 18))
        self.display.grid(row=1, column=0, columnspan=3, pady=10)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#'
        ]

        row_val = 2
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(self.master, text=button, width=10, height=3, font=("Helvetica", 18), command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        tk.Button(self.master, text="얼굴 등록", width=10, height=3, font=("Helvetica", 18), command=self.register_face).grid(row=row_val, column=0, columnspan=3, padx=5, pady=5)

    def setup_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.label = tk.Label(self.master)
        self.label.grid(row=0, column=0, columnspan=3)
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
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
            if self.registered_face_path is not None:
                try:
                    result = DeepFace.verify(img1_path=self.registered_face_path, img2_path=frame, enforce_detection=False)
                    if result["verified"]:
                        messagebox.showinfo("성공", "얼굴 인식 성공! 문이 열렸습니다!")
                        self.cap.release()
                        self.master.quit()
                except Exception as e:
                    print(f"얼굴 인식 중 오류 발생: {e}")
        else:
            black_frame = np.zeros_like(frame)
            img = Image.fromarray(black_frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

    def register_face(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite(self.registered_face_path, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            messagebox.showinfo("성공", "얼굴이 등록되었습니다!")

    def button_click(self, value):
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
            self.display.insert(tk.END, value)

    def check_password(self):
        if self.input_password.endswith(self.password):
            messagebox.showinfo("성공", "문이 열렸습니다!")
        else:
            messagebox.showerror("오류", "비밀번호가 틀렸습니다!")
        self.reset_input()

    def prompt_old_password(self):
        self.change_mode = True
        self.verify_old = True
        self.display.delete(0, tk.END)
        messagebox.showinfo("알림", "기존 비밀번호를 입력하세요")

    def verify_old_password(self):
        if self.input_password == self.password:
            self.input_password = ""
            self.display.delete(0, tk.END)
            messagebox.showinfo("알림", "새 비밀번호를 입력하세요")
            self.verify_old = False
        else:
            messagebox.showerror("오류", "기존 비밀번호가 틀렸습니다!")
            self.change_mode = False
            self.verify_old = False
        self.reset_input()

    def verify_new_password(self):
        new_password = self.input_password
        if len(new_password) >= 4:
            self.password = new_password[-4:]  # 비밀번호의 뒷자리 4자리만 저장
            messagebox.showinfo("성공", "비밀번호가 변경되었습니다!")
        else:
            messagebox.showerror("오류", "비밀번호는 최소 4자리여야 합니다!")
        self.change_mode = False
        self.reset_input()

    def reset_input(self):
        self.input_password = ""
        self.display.delete(0, tk.END)

    def reset_input_timer(self):
        if self.reset_timer:
            self.master.after_cancel(self.reset_timer)
        self.reset_timer = self.master.after(5000, self.reset_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = DoorLock(root)
    root.mainloop()