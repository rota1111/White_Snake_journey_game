# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character('希尔薇娅',color="#c8ffc8")
define m = Character('我',color="#c8c8ff")
# 游戏在此开始。

label start:
    s "嗨！今天的课怎么样？"

    m "挺好的……"

    "我当然不会承认，上课的时候内容只是左耳进右耳出。"

    s "你现在要回家了吗？要不要跟我一起走？"

    m "当然！"
    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "您已创建一个新的 Ren'Py 游戏。"

    e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
