screen lights_rule():
    fixed:
        text "熄灭所有亮起石块" xalign 0.5 yalign 0.5

screen lights_out(c=4, r=4):

    default matrix = [[True for _ in range(c)] for _ in range(r)]

    grid c r:
        align (0.5, 0.5)
        spacing 20

        for i in range(c * r):
            imagebutton:
                auto 'light_{}_%s'.format('True' if find_element(matrix, i) else "False")
                action Function(toggle_elements, matrix, i)