# pip install opencv-python
# pip install moviepy

import cv2
from moviepy.editor import *
import numpy as np


def generate_video(string):
    # Создаем временное изображение с текстом
    text = string
    if len(text) == 0:
        return print("Введите строку, на английском языке, длиной не менее одного символа!!")
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 8
    thickness = 15
    duration = 2400
    text_width, text_height = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_y_percent = 100

    image = np.zeros((text_height, text_height, 3), dtype=np.uint8)
    image[:] = (255, 0, 255)
    # Сохранение сгенерированного изображения
    cv2.imwrite("Leetcode\it-solution\\blank.jpg", image)
    text_y = int((text_y_percent * text_height) / 100)


   # Создаем список кадров видео с изменяющимся положением текста
    n_frames = int(text_width * 100 / duration)
    frames = []
    for x_offset in range(0, text_width, n_frames):  # Изменение положения текста по оси X
        frame = cv2.imread("Leetcode\it-solution\\blank.jpg")
        frame = cv2.putText(frame, text, (10 - x_offset, text_y), font, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)
        frames.append(frame)

    # Создаем видео с бегущей строкой
    clip = ImageSequenceClip(frames, durations=[0.1] * len(frames))
    clip = clip.fx(vfx.resize, width=text_height)  # Изменение размера видео

    # Сохраняем видео
    output_video = "output.mp4"
    clip.write_videofile(output_video, fps=24)

    print("Видео с бегущей строкой успешно сгенерировано!")

# Тестовый пример
generate_video("")