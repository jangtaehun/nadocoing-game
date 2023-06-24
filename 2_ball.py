import pygame
import os

pygame.init()

screen_width = 640
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("ZZonddeok game")

clock = pygame.time.Clock() #FPS

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환
background = pygame.image.load(os.path.join(image_path, "background.png"))


stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
stage_y_pos = screen_height - stage_height

character = pygame.image.load(os.path.join(image_path, "char.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = (screen_height) - stage_height - character_height
character_to_x = 0
character_speed = 8

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10
weapons = []

ball_images = [
    pygame.image.load(os.path.join(image_path, "ball1.png")),
    pygame.image.load(os.path.join(image_path, "ball2.png")),
    pygame.image.load(os.path.join(image_path, "ball3.png")),
    pygame.image.load(os.path.join(image_path, "ball4.png"))]
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
    "to_y": -6, # y축 이동방향,
    "init_spd_y": ball_speed_y[0]})# y 최초 속도


running = True
while running:
    dt = clock.tick(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) #weapons리스트에 리스트로 x, y좌표를 넣어준다.
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    character_x_pos += character_to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 / 무기의 y값에 스피드값을 빼 무기를 위로 가게 만든다.
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    #공 위치
    for ball_idx, ball_val in enumerate(balls):
        #리스트를 0, 1, 2, 3...으로 나누는 것
        #0
        #{'pos_x': 50, 'pos_y': 50, 'img_idx': 0, 'to_x': 3, 'to_y': -6, 'init_spd_y': -18}
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        print(ball_idx)
        print(ball_val)
        print(ball_pos_x)
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        print(ball_pos_x)
        print(ball_pos_y)
        print(ball_img_idx)
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, stage_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update()

pygame.quit()