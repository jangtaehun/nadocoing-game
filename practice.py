import pygame
import os

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환


ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png")),
    pygame.image.load(os.path.join(image_path, "ball4.png"))]
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값
balls = []

balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
    "to_y": -6, # y축 이동방향,
    "init_spd_y": ball_speed_y[0]})# y 최초 속도


for ball_idx, ball_val in enumerate(balls):
    print(ball_idx, ball_val)
    #리스트를 0, 1, 2, 3...으로 나누는 것
    #0
    #{'pos_x': 50, 'pos_y': 50, 'img_idx': 0, 'to_x': 3, 'to_y': -6, 'init_spd_y': -18}
    ball_pos_x = ball_val["pos_x"]
    ball_pos_y = ball_val["pos_y"]
    ball_img_idx = ball_val["img_idx"]
    print(ball_pos_x)
    print(ball_pos_y)
    ball_size = ball_images[ball_img_idx].get_rect().size
    ball_width = ball_size[0]
    ball_height = ball_size[1]

    if ball_pos_x < 0 or ball_pos_x > 640 - ball_width:
        ball_val["to_x"] = ball_val["to_x"] * -1  # 벽에 부딪히면 튕겨라

    if ball_pos_y >= 720 - 50 - ball_height:
        ball_val["to_y"] = ball_val["init_spd_y"]  # 무대에 부딪히면 튕겨라
    else: # 그 외의 모든 경우에는 속도를 증가
        ball_val["to_y"] += 0.5

    ball_val["pos_x"] += ball_val["to_x"]
    ball_val["pos_y"] += ball_val["to_y"]



for idx, val in enumerate(balls):
    ball_pos_x = val["pos_x"]
    ball_pos_y = val["pos_y"]
    ball_img_idx = val["img_idx"]
    print(ball_pos_x)
    print(ball_pos_y)
    print(ball_img_idx)