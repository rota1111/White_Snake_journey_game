label xu_second_section:
    scene bg 6
    "永州城附近，两岸连山，碧水潺潺。你们二人正乘着小船前往永州。"
    axuan talk "离永州已经不远了，还在想自己的来历？想不起自己的来历，是挺头疼的。"
    axuan talk "不过呢，很多事记得不如忘了好。人生无常，苦多乐少。既然如此，多记住些美好的时候就好了。"
    play music music3
    "（啊啊啊~啊啊啊啊~船夫哼起了经典的千年等一回的曲调）"
    stop music 
    menu:
        "大叔闭嘴。":
            axuan talk "大叔，我喜欢清净一点。"
            jump xu_second_one
        "我行我唱。":
            axuan talk "大叔，你唱的调子也太老了吧，都什么朝代了，我来唱吧。"
            "说完，他跳上了桅杆，唱起歌来~"
            play music music4
            show xiaobai_ with dissolve
            "小白不语，只是一味的偷笑，你也一头雾水，不知道是好听还是不好听。"
            hide xiaobai_ with dissolve
            stop music
            jump xu_second_one
    label xu_second_one:
        scene bg 7
        "突然，天色转暗，风气浪涌，水流湍急。在你们面前有一叶小舟，挡在你们的必经之路上。正当你们靠近时，小舟上的船夫突然现出蛇妖的原形，身形巨大无比，毒牙寒光凌凌，向你们扑来。"
        show nansheyao with dissolve
        nansheyao "你果然和人在一起，我取你性命。"
    
    "看他向小白扑去，你决定："
    menu:
        "挡在小白身前。":
            "即使你知道自己无法挡住蛇妖的攻击，你仍然奋不顾身的挡在了小白身前。"
            jump xu_second_two
        "躲在小白身后。":
            "你知道小白会法术，因此躲在她的身后让你很有安全感，即使这样很不道德。"
            jump xu_second_two
        "躲在船夫身后。":
            "你躲在了船夫的身后，船夫一脸震惊的看着你，欲言又止，他只是带着你连忙躲在船舱内。"
            jump xu_second_two
    label xu_second_two:
        hide nansheyao with dissolve
        show xiaobai_ with dissolve
        "危急之时，只见小白化身成了一条白蛇，用锋利的尾巴一扫，将来势汹汹的蛇妖斩落水下，成功逃过一劫。但是由于她用力过猛，法力失控，昏了过去。"
        "你看到昏倒的小白，决定将她带到附近的寺庙中修养。"
        hide xiaobai_ with dissolve

    scene bg 8
    "你背着她来到了这座废弃的寺庙，你发现她的身体越来越冷，面色通红。"
    menu label_xu_second_three:
        "升起火堆。":
            "你升起了一堆火，但仍然没有缓解小白的症状，白霜从她的身体蔓延到了四周的地面上。"
            jump label_xu_second_four

        "远离小白。":
            "你从小就怕冷，不愿靠近小白，只好让她自生自灭。不出意外的话就要出意外了。"
            "恍惚之间，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了做出选择的前一刻。"
            jump label_xu_second_three

    menu label_xu_second_four:
        "用身体为她取暖。":
            "你决定抱住她，尝试用自己的体温缓解她的寒冷，不知不觉中你也睡了过去。"
            jump after_label_xu_second_four
        "远离小白。":
            "你从小就怕冷，不愿靠近小白，只好让她自生自灭。不出意外的话就要出意外了。恍惚之间，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了做出选择的前一刻。"
            jump label_xu_second_four

    label after_label_xu_second_four:
        "你耐心的解释抱着你的缘由。"
    
    axuan talk "在你昏过去之后，法力外泄，身上冷的像冰块一样，于是我将身体当作暖炉，你才醒过来了的。"
    show xiaobai_ with dissolve
    xiaobai "你看到我的尾巴了吧，我是个妖怪。"
    menu:
        "妖精受死。":
            xiaobai "（疑惑）哈？"
            axuan talk "没有没有，我只是活跃一下气氛。"
            axuan talk "是就是呗，人间多的是长了两只脚的恶人，长了条尾巴又怎么样，你不是恶人，就算是妖，你也是个好妖。"
            jump xu_second_three
        "是就是呗。":
            axuan talk "是就是呗，人间多的是长了两只脚的恶人，长了条尾巴又怎么样，你不是恶人，就算是妖，你也是个好妖。"
            jump xu_second_three
    label xu_second_three:
        "你看到小白的眼中露出了不一样的神采，看你的眼神又温柔了几分。"
        hide xiaobai_ with dissolve
        scene bg 9
        "你们继续踏上了前往宝青坊的旅程，经过一番寻找，你们终于来到了宝青坊门前。"
        show boss with dissolve
        "刚进门，便看见了宝青坊的老板娘迎了过来，只见她只见她身姿婀娜，面容姣好，却带着一丝神秘莫测的气息。她穿着一袭青色长裙，裙摆上绣着精致的花纹，随着她的动作轻轻摇曳。"
        "她的眼眸深邃，仿佛能洞察人心，嘴角挂着一抹似有若无的微笑，让人捉摸不透她的真实想法。"

    boss "呦，来客人了。姑娘又来敝坊，是法宝有问题？倒是这位公子面生的很。"
    menu:
        "没有，我们只是随便逛逛。":
            boss "哦？真的吗，那敢问公子想要哪种法宝，本坊有各种各样的宝贝，从灵珠到仙草，从法宝到神器，应有尽有。不过，每一件都有它的代价。"
            "她转身，目光在你们身上扫过，仿佛在评估你们的价值。你微微皱眉，虽然不明真相，但直觉告诉你，这里的每一件东西都不是轻易能得到的。"
            hide boss with dissolve
            show xiaobai_ with dissolve
            "小白则显得有些紧张，她紧紧握住你的手，低声说道："
            xiaobai "阿宣，我们得小心，这里的一切看起来都很不寻常。"
            hide xiaobai_ with dissolve
            show boss with dissolve
            "老板娘似乎察觉到了小白的紧张，她轻笑一声，继续说道："
            boss "比如姑娘头上这件‘忘忧玉钗’，它能够吸取他人法力为己所用，但代价是……"
            "她故意停顿了一下，眼神中闪过一丝狡黠，"
            boss "它会取走使用者的记忆，使用的越多，记忆丧失的也越多。"
            hide boss with dissolve
            jump xu_second_four
        "对，我们想知道这法宝的来历。":
            boss "比如姑娘头上这件‘忘忧玉钗’，它能够吸取他人法力为己所用，但代价是……"
            "她故意停顿了一下，眼神中闪过一丝狡黠，"
            boss "它会取走使用者的记忆，使用的越多，记忆丧失的也越多。"
            axuan talk "我说呢，我遇到她的时候，她就失去了记忆。记忆消失，还要法力干什么。"
            boss "天之道，有所得，必有所失。这种移花接木，改变乾坤之事，我十分感兴趣。"
            boss "而且这只玉钗最初的主人并不是你，而是另有其人。"
            hide boss with dissolve
            show xiaobai_ with dissolve
            xiaobai "那关于原主人，你能帮我们找到一些线索吗？"
            hide xiaobai_ with dissolve
            show boss with dissolve
            boss "当然这片蛇鳞就是原主人之物。"
            hide boss with dissolve
            show xiaobai_ with dissolve
            "小白拿起了这片蛇鳞，细细感受了一下它，过了许久，她终于回过神来，却一言不发。"
            hide xiaobai_ with dissolve
            jump xu_second_four
    label xu_second_four:
        scene bg 10
        "你与阿宣走出了宝青坊，没过多久，迎面走来一个身披斗篷的黑衣人。"
        show black_man with dissolve
        black_man "捕蛇人？"
        "话音未落，黑衣人向你冲过来，你知道来者不善，决定："

    menu xu_second_five:
        "保护小白，伺机而动。":
            "只见黑衣人下手狠毒，将你一掌打飞数米，随后重重落在地上，你昏迷不醒，生死未卜。"
            hide black_man with dissolve
            "弥留之际，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了做出选择的前一刻。"
            show black_man with dissolve
            jump xu_second_five
        "保护自己，马上开溜。":
            "小白与黑衣人对了一掌，掌风鼓动，周围的空气仿佛都被震得微微颤抖，四周的树叶被强劲的掌风扫落，纷纷扬扬地飘散开来。她们二人势均力敌，谁也无法在这一击中占据上风。你感到一股强大的力量从他们掌心传来。"
            jump after_xu_second_five
    label after_xu_second_five:
        hide black_man with dissolve
        show xiaoqing with dissolve
        "就在这时，黑衣人突然摘下了兜帽，露出了本来的面目。小白愣了一下，随后惊讶地喊道"
        xiaobai "小青？！"
        "小青的脸在月光下显得格外冷峻，她的眼神中带着一丝复杂的情绪，既有愤怒，也有无奈。她冷冷地看着她，语气中带着一丝责备。"
        xiaoqing "小白，你到底在做什么？师傅派我来带你回去，没想到你竟然和捕蛇人混在一起，还和我动手！"
        hide xiaoqing with dissolve
        show xiaobai_ with dissolve
        xiaobai "小青，我不是叛徒。阿宣不是普通的捕蛇人。他救了我，照顾我，甚至愿意为我放弃一切。"
        hide xiaobai_ with dissolve
        show xiaoqing with dissolve
        xiaoqing "国师修炼的太阴真功，和我们蛇族同出一脉，他吸取我们的魂魄精华修炼他的功力，师傅恨透了国师，恨透了人，师傅说，人心险恶，只要是人就险恶！"

    menu:
        "你个妖精，不由分说就袭击我，你才险恶呢！":
            xiaoqing "你！"
            jump xu_second_six
        "表示理解。":
            axuan talk "原来国师修炼的是这么邪门的功法，我真的不知道他是这样的。"
            "你这才得知朝廷下令捕蛇的原因。"
            xiaoqing "假惺惺，你一个捕蛇人，帮凶，帮凶就该死！我杀了你这个捕蛇人。"
            jump xu_second_six
    label xu_second_six:
        "说罢，小青又冲了过来，准备杀掉你。"
        "由于小青这次攻击用了全力，突然地面塌陷，你和小白掉入了一个地宫当中，你们连忙在入口彻底封死之前躲了进去，暂时逃脱了小青的追击。"
        hide xiaoqing with dissolve
        jump xu_third_section
