screen whack_a_mole(c=7, r=5):

    default matrix = [[False for _ in range(c)] for _ in range(r)]
    default score = 0

    text '[score]/30' align (0.05, 0.5)

    grid c r:
        align (0.5, 0.5)
        spacing 20

        for i in range(c * r):

            imagebutton:
                auto 'light_{}_%s'.format('True' if find_element(matrix, i) else "False") # find_element在lights_out游戏中
                action If(
                    find_element(matrix, i),
                    If(
                        score < 30,
                        [IncrementScreenVariable('score'), Function(toggle_element2, matrix, i)],
                        Return()
                    ),
                    NullAction()
                )

    timer renpy.random.randint(1, 2) action Function(mole_appearing, matrix) repeat True