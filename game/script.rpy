# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define me = Character("我",color="#CCCCCC")
define xiaoqing = Character("小青",color="#00FFFF")
define axuan = Character("阿宣",color="#FF0000")
define dudou = Character("肚兜",color="#FFFF00")
define laofuren = Character("老妇人",color="#F5F5F5")
define girl = Character("姑娘",color="#FFFFFF")
define xiaobai = Character("小白",color="#FFFFFF")
define cunmin = Character("村民",color="#E3CF57")
define boss = Character("老板娘",color="#8A2BE2")
define black_man = Character("黑衣人",color="#000000")
define nansheyao = Character("男蛇妖",color="#802A2A")
define guo_shi_di_zi = Character("国师弟子",color = "#9932CC")
define guoshi = Character("国师",color = "#9932CC")
define shifu = Character("师傅",color = "#FFC0CB")
define young_man = Character("年轻人",color = "#FF0000")
define daoshi = Character("道士", color = "#603d30")
define baixing = Character("百姓", color = "#eea08c")
define cunminjia = Character("村民甲", color = "#bdaead")
define cunminyi = Character("村民乙", color = "#ed4845")
define da_shen = Character("大婶", color="#f2b9b2")
define xiaren = Character("下人",color = "#f33b1f")
define cunminbing = Character("村民丙", color = "#bdaeaf")
# 游戏在此开始。


label start:

    scene bg 1 with dissolve
    "2025年1月28日晚，你正在和家人坐在一起看春晚"
    
    "此时电视里正在播放这小品《借伞》，喜欢白蛇传故事的你看的津津有味。"

    "节目结束时你还在回味刚刚的小品情节，你不禁想到，他们的爱情故事真是美好。"

    menu:
        me "要是我也是__就好了。"
        "许仙":
            jump xuxian
        "白素贞":
            jump baisuzhen
    label xuxian:
        scene bg 2 with dissolve
        "正当你沉浸于自己的幻想时，突然一道神秘的光芒闪过，你感到一阵眩晕，随后发现自己置身于一个陌生而古老的世界。"
        
        "与此同时，一段不属于你的记忆涌入了你的脑海："

        scene bg 3
        show axuan with dissolve
        "许宣是一个在山野间自由自在的活泼少年，清俊洒脱且果敢有担当。他生活在晚唐时期的捕蛇村，这是一个因捕蛇可以抵税而兴起的村落。"

        "他出身普通，是村里的捕蛇人，但与一般捕蛇人不同，他害怕捕蛇，更喜欢采摘草药。"

        "请查明朝廷下令捕蛇的真实原因，并解决村子即将面临的危机，方可回到原来的世界。"

        hide axuan with dissolve
        "回过神来你这才发现，你化身成为了阿宣，穿越到了《白蛇》的故事之中，虽然有些猝不及防，但饱览穿越小说的你很快接受了这个设定，甚至还有些跃跃欲试。"

        scene bg 4
        "此时你像往常一样，独自一人来到村外的水域采摘草药。突然，你听到一阵微弱的呻吟声，声音似乎是从水边传来的。"

        menu:
            "顺着声音查看。":
                jump voice
            "不理会声音，专心采药。":
                jump no_voice
        label no_voice:
            "你发现靠近水边的地方草药更加茂盛，不知不觉中你耳边的声音更加清晰了，这下不得不看看发生了什么。"
        label voice:
            show xiaobai at right
            "来到了河边的一块大石头旁，你发现那是一个穿着白色衣裙的女子，她躺在岸边，昏迷不醒，身上还带着一些伤痕。"

            "看到这一幕，你有一些犹豫，决定："
            menu if_save_people:
                "立刻救人":
                    jump save_people
                "装作没看见，继续敬业的采草药":
                    jump not_save
            label save_people:
                scene bg 4-1
                "你将女子抱回了自己的小屋，将她放在床上，用被子轻轻盖住她。然后屋外的草丛中采来一些草药，熬成汤药，小心翼翼地喂给女子喝。不知她什么时候能醒啊，那么她到底是谁呢？"     
                hide xiaobai with dissolve
                jump xu_first_section
            label not_save:
                hide xiaobai with dissolve
                scene bg 4-2
                "你没有理会这个陌生的白衣女子，而是继续专注于找草药，不知不觉中你走到了丛林深处，当你采完了最后一株草药时，你已分不清来时的路。"

                "正当你一筹莫展之际，突然听到身后传来某种东西划过地面而发出的摩擦声，你以为遇到了村里的人，正要开心的问路，没想到一回头是一只人面蛇身的蛇妖，张着大嘴向你袭来，你来不及反应，眼前一黑失去了意识。"
                
                "弥留之际，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了做出选择的前一刻。"
                show xiaobai with dissolve
                
                jump if_save_people

    label baisuzhen:
        scene bg 2 with dissolve
        "正当你沉浸于自己的幻想时，突然一道神秘的光芒闪过，你感到一阵眩晕，随后发现自己置身于一个陌生而古老的世界。"
        
        "与此同时，一段不属于你的记忆涌入了你的脑海："

        show xiaobai with dissolve
        "小白是一只修炼了五百年的白蛇，虽然已经化成了人形，但始终无法修成正果，得道飞仙，你的内心仿佛有处空洞，每次突破都会周天动摇，几乎走火入魔。"
        
        "这一次的突破也是失败了，在妹妹小青的帮助下，你才清醒过来，请找到自己无法突破的原因，了却因果方可回到原来的世界。"
        hide xiaobai with dissolve
        "回过神来你这才发现，你化身成为了小白，穿越到了《白蛇》的故事之中，虽然有些猝不及防，但饱览穿越小说的你很快接受了这个设定，甚至还有些跃跃欲试。"


        show xiaoqing
        "你刚刚经历了一场失败，看见眼前一脸担心的小青，你决定："

        menu tupo_choice:
            "把自己的困惑告诉她":
                jump tell_her
            "闭口不言，不让她担心":
                jump not_tell_her
            "强行突破，大胆冒险":
                jump qiangxing_topo
        
        
        label tell_her:
            xiaoqing "是啊，每次突破都很险，至于你的困惑，你握住这只珠钗，它会告诉你一切。"
            hide xiaoqing with dissolve
            jump bai_first_section
        label not_tell_her:
            xiaoqing "姐姐，你每次突破都这么冒险，看你的样子一定很困惑，你握住这只珠钗，它会告诉你一切。"

            "你握住了小青递过来的宝钗，突然，宝钗上射出一道碧色的光，冲入了你的眉心。"

            hide xiaoqing with dissolve
            "五百年前的记忆顿时涌入了你的脑海，神奇的是，你的身体也随之穿越回了过去。"

            jump bai_first_section
        label qiangxing_topo:
            "你不甘心居于现状，找机会背着小青自己强行突破，结果自然是走火入魔，功力全失，筋脉尽断，几近气绝身亡。"
            
            hide xiaoqing with dissolve
            
            "弥留之际，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了做出选择的前一刻。"

            show xiaoqing
            jump tupo_choice










        
