import Object
import Camera as cam
import Ray as ray
import pygame
import CoPoVe as cpv
import math
import Map

gradient = [(110, 0, 0), (100, 0, 0), (90, 0, 0), (80, 0, 0), (70, 0, 0), (60, 0, 0), (50, 0, 0), (40, 0, 0), (30, 0, 0), (20, 0, 0), (0, 0, 0)]
s = Object.Pygame(1300, 700)
camera = cam.Camera(cpv.Point(0, 0, 0), 1, math.pi/3, math.pi/2, 70)
del_ang_gor = camera.gfov // s.num_rays_gor
del_ang_vert = camera.vfov // s.num_rays_vert
a = Object.Plane(cpv.Point(10, 10, 10), 60, Object.ParametersPlane(10, 10, 5, 2000))
b = Object.Sphere(cpv.Point(5, 5, 5), 0, Object.ParametersSphere(100, 100, 10, 70))
mapp = Map.Map([a])
rays_gor = ray.Ray(camera.pos, camera.look_at + camera.gfov / 2)
rays_vert = ray.Ray(camera.pos, camera.look_at + camera.vfov / 2)
x_0 = rays_gor.pos.x
y_0 = rays_gor.pos.y
z_0 = rays_gor.pos.z

pygame.init()
sc = pygame.display.set_mode((s.width, s.height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                camera.pos.y += 10
            if event.key == pygame.K_s:
                camera.pos.y -= 10
            if event.key == pygame.K_a:
                camera.pos.x -= 10
            if event.key == pygame.K_d:
                camera.pos.x += 10
            if event.key == pygame.K_LEFT:
                camera.look_at -= math.pi / 6
            if event.key == pygame.K_RIGHT:
                camera.look_at += math.pi / 6
            if event.key == pygame.K_UP:
                camera.look_at += math.pi / 6
            if event.key == pygame.K_DOWN:
                camera.look_at -= math.pi / 6
            if event.key == pygame.K_BACKSPACE:
                camera.pos.z += 10

    cur_angle_gor = camera.look_at + camera.gfov//2
    for i in range(0, s.num_rays_gor):
        cur_angle_vert = camera.look_at + camera.vfov//2
        for p in range(0, s.num_rays_vert):
            min_dist = camera.draw_distance
            for k in range(len(mapp.arr)):
                for dist in range(1, camera.draw_distance + 1):
                    x = int(x_0 + dist * math.cos(cur_angle_gor))
                    y = int(y_0 + dist * math.sin(cur_angle_gor))
                    z = int(z_0 + dist * math.sin(cur_angle_vert))

                    if mapp.arr[k].contains(cpv.Point(x, y, z)):
                        min_dist = min(min_dist, dist)
                        break

            if min_dist <= camera.draw_distance:
                pygame.draw.rect(sc, gradient[int(min_dist // 7)], (i, p, (i + 1), (p + 1)))
            else:
                pygame.draw.rect(sc, gradient[10], (i, p, (i + 1), (p + 1)))
            cur_angle_vert -= del_ang_vert
        cur_angle_gor -= del_ang_gor

    pygame.display.flip()

# for dist in range(1, camera.draw_distance + 1):
#     x = x_0 + dist * math.cos(cur_angle)
#     y = y_0 + dist * math.sin(cur_angle)
#
#     for j in range(len(mapp.arr)):
#         if mapp.arr[j].contains(cpv.Point(x, y, z_0)):
#             min_dist = min(dist, min_dist)
#     else:
#         if min_dist > camera.draw_distance:
#             # break
