import tkinter as tk
import serial
import time

try:
    # 아두이노와의 시리얼 통신 설정
    arduino = serial.Serial('COM10', 9600)  # COM 포트는 실제 연결된 포트로 변경 필요
    time.sleep(2)  # 아두이노 초기화 시간 대기
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

led_5_state = False
led_10_state = False

def all_on():
    global led_5_state, led_10_state
    arduino.write(b'H5\n')  # 아두이노에 'H5' 신호 전송 (5번 핀 LED 켜기)
    arduino.write(b'H10\n')  # 아두이노에 'H10' 신호 전송 (10번 핀 LED 켜기)
    arduino.write(b'B51\n')  # 아두이노에 'B51' 신호 전송 (5번 핀 LED 밝기 1)
    arduino.write(b'B101\n')  # 아두이노에 'B101' 신호 전송 (10번 핀 LED 밝기 1)
    led_5_state = True
    led_10_state = True
    led_5_brightness.set(1)
    led_5_brightness.config(state=tk.NORMAL)
    led_10_brightness.set(1)
    led_10_brightness.config(state=tk.NORMAL)

def all_off():
    global led_5_state, led_10_state
    if led_5_state and led_10_state:
        arduino.write(b'L5\n')   # 아두이노에 'L5' 신호 전송 (5번 핀 LED 끄기)
        arduino.write(b'L10\n')  # 아두이노에 'L10' 신호 전송 (10번 핀 LED 끄기)
        led_5_state = False
        led_10_state = False
        led_5_brightness.config(state=tk.DISABLED)
        led_10_brightness.config(state=tk.DISABLED)

def set_brightness_5(val):
    if led_5_state and led_10_state:
        brightness = int(val)
        arduino.write(f'B5{brightness}\n'.encode())  # 아두이노에 밝기 값 전송 (5번 핀)

def set_brightness_10(val):
    if led_5_state and led_10_state:
        brightness = int(val)
        arduino.write(f'B10{brightness}\n'.encode())  # 아두이노에 밝기 값 전송 (10번 핀)

# tkinter GUI 설정
root = tk.Tk()
root.title("Arduino LED Control")

all_on_button = tk.Button(root, text="ALL ON", command=all_on, width=30, height=3)
all_on_button.pack(pady=20)

all_off_button = tk.Button(root, text="ALL OFF", command=all_off, width=30, height=3)
all_off_button.pack(pady=20)

led_5_brightness = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue LED Brightness", command=set_brightness_5, state=tk.DISABLED, length=400)
led_5_brightness.pack(pady=20)

led_10_brightness = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Red LED Brightness", command=set_brightness_10, state=tk.DISABLED, length=400, resolution=1)
led_10_brightness.pack(pady=20)

root.mainloop()

# 아두이노와의 시리얼 통신 종료
arduino.close()