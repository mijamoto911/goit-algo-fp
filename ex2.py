import turtle

def draw_pythagoras_tree(branch_len, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_len)
        t.left(angle)
        draw_pythagoras_tree(0.7 * branch_len, t, angle, level-1)
        t.right(2 * angle)
        draw_pythagoras_tree(0.7 * branch_len, t, angle, level-1)
        t.left(angle)
        t.backward(branch_len)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("blue")
    t.width(2)
    t.speed(0)
    t.ht()

    level = int(input("Enter the level of recursion: "))

    t.left(90)  
    draw_pythagoras_tree(100, t, 30, level)

    t.done()

if __name__ == "__main__":
    main()
