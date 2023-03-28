import turtle

def draw_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    draw_tree(100, t)
    turtle.done()

if __name__ == '__main__':
    main()
