import turtle
import math

from vertex import Vertex

VERTEX_RADIUS = 20
X_CENTER = 100
Y_CENTER = -175
X_LEFT_ARC = -100
Y_DOWN_ARC = -200
RAISE_LENGTH = 80
turtle.speed(0)


def set_vertex_position(length):
    vertices = []
    x = -100
    y = -200
    for i in range(length):
        if i <= length / 4:
            vertices.append(Vertex(x, y, i))
            x += 100
        elif i < length / 1.5:
            vertices.append(Vertex(x, y, i))
            x -= 100
            y += 100
        else:
            vertices.append(Vertex(x, y, i))
            y -= 100
    return vertices


def draw_self(x, y, is_direct):
    turtle.up()
    turtle.goto(x, y + VERTEX_RADIUS)
    angle = math.atan2(y - Y_CENTER, x - X_CENTER) * 180 / math.pi
    turtle.setheading(angle + 270)
    turtle.down()
    turtle.circle(25, 313)
    if is_direct:
        turtle.stamp()
    turtle.setheading(0)


def draw_line(x_from, y_from, x_to, y_to, is_direct):
    turtle.up()
    turtle.goto(x_from, y_from + VERTEX_RADIUS)
    angle = -math.atan2(y_from - y_to, x_to - x_from) * 180 / math.pi
    turtle.setheading(angle)
    turtle.down()
    turtle.goto(x_to, y_to + VERTEX_RADIUS)
    if is_direct:
        turtle.backward(VERTEX_RADIUS)
        turtle.stamp()
    turtle.setheading(0)


def draw_down_arc(x_from, y_from, x_to, y_to, is_direct, e):
    turtle.up()
    turtle.goto(x_from, y_from + VERTEX_RADIUS)
    turtle.down()
    turtle.goto((x_from + x_to) / 2, y_to - e)
    draw_line((x_from + x_to) / 2, y_to - e - VERTEX_RADIUS, x_to, y_to, is_direct)


def draw_left_arc(x_from, y_from, x_to, y_to, is_direct, e):
    turtle.up()
    turtle.goto(x_from, y_from + VERTEX_RADIUS)
    turtle.down()
    turtle.goto(x_to - e, (y_from + y_to) / 2 + VERTEX_RADIUS)
    draw_line(x_to - e, (y_from + y_to) / 2, x_to, y_to, is_direct)


def draw_hypotenuse_arc(x_from, y_from, x_to, y_to, is_direct, e):
    turtle.up()
    turtle.goto(x_from, y_from + VERTEX_RADIUS)
    turtle.down()
    turtle.goto(abs((x_from + x_to) / 2) + e, abs((y_from + y_to) / 2) + e)
    draw_line(abs((x_from + x_to) / 2) + e, abs((y_from + y_to) / 2) + e - VERTEX_RADIUS, x_to, y_to, is_direct)


def draw_vertices(vertices):
    for i in range(len(vertices)):
        turtle.up()
        turtle.goto(vertices[i].pos_x, vertices[i].pos_y)
        turtle.down()
        turtle.begin_fill()
        turtle.circle(VERTEX_RADIUS)
        turtle.end_fill()
        turtle.color('white')
        turtle.write(f'{vertices[i].num + 1}', False, 'center', ('Arial', VERTEX_RADIUS, 'normal'))
        turtle.color('black')


def draw_edges(matrix, vertices, is_direct):
    n = len(matrix)
    for i in range(n):
        for j in range((0 if is_direct else i), n):
            if matrix[i][j]:
                e = RAISE_LENGTH
                if matrix[i][j] == matrix[j][i] and is_direct and i > j:
                    e = 140
                if i == j:
                    draw_self(vertices[i].pos_x, vertices[i].pos_y, is_direct)
                elif vertices[i].pos_y == vertices[j].pos_y == Y_DOWN_ARC and abs(vertices[i].pos_x - vertices[j].pos_x) > 100:
                    draw_down_arc(vertices[i].pos_x, vertices[i].pos_y, vertices[j].pos_x, vertices[j].pos_y, is_direct, e)
                elif vertices[i].pos_x == vertices[j].pos_x == X_LEFT_ARC and abs(vertices[i].pos_y - vertices[j].pos_y) > 100:
                    draw_left_arc(vertices[i].pos_x, vertices[i].pos_y, vertices[j].pos_x, vertices[j].pos_y, is_direct, e)
                elif abs(vertices[j].pos_x - vertices[i].pos_x) == abs(vertices[i].pos_y - vertices[j].pos_y) > 100:
                    draw_hypotenuse_arc(vertices[i].pos_x, vertices[i].pos_y, vertices[j].pos_x, vertices[j].pos_y, is_direct, e)
                else:
                    if e == 140:
                        draw_line(vertices[i].pos_x, vertices[i].pos_y, (vertices[i].pos_x + vertices[j].pos_x) / 2 + 30, (vertices[i].pos_y + vertices[j].pos_y) / 2 - 30, False)
                        draw_line((vertices[i].pos_x + vertices[j].pos_x) / 2 + 30, (vertices[i].pos_y + vertices[j].pos_y) / 2 - 30, vertices[j].pos_x, vertices[j].pos_y, is_direct)
                    else:
                        draw_line(vertices[i].pos_x, vertices[i].pos_y, vertices[j].pos_x, vertices[j].pos_y, is_direct)


def draw_graph(matrix, is_direct):
    vertices = set_vertex_position(len(matrix))
    draw_edges(matrix, vertices, is_direct)
    draw_vertices(vertices)
    turtle.hideturtle()
