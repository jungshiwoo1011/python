import tkinter as tk
import serial
import time

# 아두이노 설정
arduino = serial.Serial('COM11', 9600)
time.sleep(2)  # 아두이노 초기화 시간

class DoorLock:
    def __init__(self, master):
        self.master = master
        self.master.title("도어락")
        self.master.geometry("400x500")  # 화면 크기 조정
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
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.master, text=button, width=5, height=2, font=("Helvetica", 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

        self.label_result = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.label_result.grid(row=row_val, column=0, columnspan=3, pady=10)

    def setup_camera(self):
        # 카메라 설정 코드 (생략)
        pass

    def on_button_click(self, char):
        if char == '*':
            self.star_count += 1
            if self.star_count == 3:
                self.change_mode = True
                self.label_result.config(text="새 비밀번호를 입력하세요:")
                self.input_password = ""
            return

        if char == '#':
            if self.change_mode:
                self.password = self.input_password
                self.label_result.config(text="비밀번호가 변경되었습니다.")
                self.change_mode = False
            else:
                self.verify_password()
            self.input_password = ""
            self.star_count = 0
            return

        self.input_password += char
        self.display.delete(0, tk.END)
        self.display.insert(0, self.input_password)  # 비밀번호를 보여줌

        # 입력한 번호를 4초 뒤에 사라지게 설정
        if self.reset_timer:
            self.master.after_cancel(self.reset_timer)
        self.reset_timer = self.master.after(4000, self.clear_display)

    def clear_display(self):
        self.input_password = ""
        self.display.delete(0, tk.END)

    def verify_password(self):
        if self.password in self.input_password:
            self.label_result.config(text="비밀번호가 맞습니다. 문이 열립니다.")
            self.unlock_door()
        else:
            self.label_result.config(text="비밀번호가 틀렸습니다. 다시 시도하세요.")

    def unlock_door(self):
        # 아두이노에 신호 보내기
        arduino.write(b'1')
        time.sleep(4)
        arduino.write(b'0')

if __name__ == "__main__":
    root = tk.Tk()
    app = DoorLock(root)
    root.mainloop()

    # 프로그램 종료 시 아두이노 연결 해제
    arduino.close()