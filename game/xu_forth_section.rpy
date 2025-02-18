label xu_forth_section:
    scene bg 9
    "（宝青坊内）"
    show boss with dissolve
    axuan talk "老板娘，我想变成妖怪，这样就能跟小白在一起了，你可以帮我吗。"
    boss "少年人我可以帮你。"
    axuan talk "真的吗？"
    boss "少年人，我也年少过轻狂过放纵过。到如今，也留下诸多遗憾。你要知道有一天，你可能会后悔。"

    menu xu_forth_one:
        "那我再考虑考虑。":
            "思考片刻，你还是放弃了变成妖的想法，你害怕村里人的歧视目光，你害怕自己成为人人喊打的老鼠，于是告别了老板娘返回了村子。"
            hide boss with dissolve
            "不知过了多少天，一条白蛇的巨蛇袭击了你的村子，无数村民流离失所，死于非命，你也在这场灾难中丧命。"
            "弥留之际，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了上一次做出选择的时刻。"
            show boss with dissolve
            jump xu_forth_one
        "仙人悔而我不悔！":
            axuan talk "如果不能在一起，我现在就会后悔。"
            boss "好吧，果然少年。天下生意，有来有往，我要的，你给得了吗。"
    axuan talk "你要什么我给什么。"
    boss "好，不过，你得拿你的精气来换。我们为各方妖怪打造法宝所需。就是人之精气。妖怪们的法宝最灵验的，就是用精气炼出来的。这也是我们宝青坊在妖界的成名所在。"
    axuan talk "我得变成妖，我答应你。"
    boss "好，不过你可知道，成了妖怪的后果。你生而为人，享受人世间的诸多太平好处，"
    boss "理所当然，浑浑噩噩。如果成了妖怪，天要杀你，人要杀你，道士要杀你，其他妖怪也要杀你。"
    boss "你被我取了精气成妖，你也只能成为一个最弱最小的妖，无论怎么修炼也不能提升。"
    axuan talk "我都认了，来吧。"
    boss "好，成交，差点忘了，要化人为妖，我还要取一件物什。"
    axuan talk "什么物什。"
    "看到她望向了你的胯下，开始施展法术，你心中顿时升起不祥的预感。"
    axuan talk "这不成啊这！"
    "话音未落，你眼前一黑，失去了知觉。"
    hide boss with dissolve
    show dudou with dissolve
    scene bg 15
    dudou "汪汪！"
    "你被肚兜舔醒了，刚回过神，你连忙朝下看去，身上并未缺少什么零件，你终于放下了紧张的心。"
    axuan talk "还好还在。"
    "你站了起来，肚兜突然朝你身后看去，露出了惊奇的神色，你也回头一看。"
    axuan talk "肚兜，我长尾巴了！我是妖怪了！"
    hide dudou with dissolve
    "你回过神来才发现，原来老板娘将肚兜的尾巴嫁接到了你的身上，你成为了一只狗妖。"
    "喜上眉梢的你跑了起来，这才发现自己似乎有用不完的力气，健步如飞，连忙赶回那处旧寺庙寻找小白。"
    scene bg 16
    "只见此处已经成为了一片废墟，到处都是残垣断壁，火光四起。你担心小白被压在了废墟之下。"

    menu:
        "徒手挖废墟。":
            axuan talk"小白，小白，你在哪？"
            "没想到，你真挖到了幸存者，不过是一个面如骷髅的道士，他已经神志不清，这让你一头雾水，不知道发生了什么。"
            daoshi "别吸了，求求你。"
            jump xu_forth_two
        "一味呼喊。":
            axuan talk "小白，小白，你在哪？"
            "喊了半天，却是无人回应你。"
            jump xu_forth_two

    label xu_forth_two:
        scene bg 17
        "这时你看到不远处的永州城也是火光四起，浓烟飘荡。在寺庙中寻找无果的你决定去城内寻找。"
        baixing "妖怪来了，快逃命啊！"
        axuan talk "小白！小白！"
        "但见一条体型硕大的白蛇在城内横冲直撞，见过小白原形的你认出了她。"
        axuan talk "那么大一条那个是小白吗。"
        show xiaoqing with dissolve
        "小青不知从哪冒了出来，为你解释了眼前的一切。"
        xiaoqing "你还真回来了，不过姐姐她现在已经变成了一条巨蟒。那道士抢了姐姐的珠钗，不知怎么，却反被姐姐吸了功力。"
        axuan talk "怎么会这样？"
        xiaoqing "你竟然变成妖了，小子，萍水相逢，你对我姐姐能有什么深情？你不过是喜欢我姐姐的美貌罢了。如今我姐姐变成了这个吓人模样，你还喜欢她吗？"
        axuan talk "她现在要去哪？"
        xiaoqing "小子，你还不知道吧，国师已经到了你们蛇村。姐姐要去找他算账呢，那个蛇村眼看就要有灭顶之灾了。"
        hide xiaoqing with dissolve
        "听到这里，你意识到大事不好，连忙返回村子，通知村民，当然为了隐藏身份，你特意将尾巴藏进了裤子。"
        scene bg 3
        axuan talk "大家快走，我们村危险，一条巨蟒马上就要来了，赶紧走别管这村子了。"
        show cunminjia with dissolve
        cunminjia "瞎说什么呀你，我们村围墙这么高，怕什么巨蟒。"
        axuan talk "永州城被巨蟒毁了，大家快走吧，赶紧离开。"
        hide cunminjia with dissolve
        show cunminyi with dissolve
        cunminyi "永州是石头城，巨蟒？净瞎说。"
        hide cunminyi with dissolve
        da_shen "阿宣，你终于回来了。"
        axuan talk "大婶您赶紧离开，快。"
        da_shen "那我回去收拾收拾。"

    scene bg 18
    xiaren "洞虚演道，太阴真君。"
    "只见村口一声喊叫，随之而来的是浩浩荡荡的朝廷军队，国师就在军队最前方的车架当中。"
    show guoshi with dissolve
    guoshi "一条巨蟒？但你是一只妖怪，又怎知你不是妖言惑众。"
    "说罢，他施展法术，将你控制在空中，让你的尾巴露了出来。"
    axuan talk "你身为国师，却不能保民平安，净做些祸害人的事。"
    hide guoshi with dissolve
    show cunminbing with dissolve
    cunminbing "(惊呼)他真的是妖怪！"
    hide cunminbing with dissolve
    axuan talk "是，我是妖怪了，但我还是阿宣。我赶回来就是为了让你们快逃，永州城毁了，这也会毁了。大家要听我的赶紧离开这。"
    "大家只是一味的震惊你的妖怪身份，甚至露出害怕与厌恶的神色，对你的警告不屑一顾。"
    show guoshi with dissolve
    guoshi "无能小妖。"
    axuan talk "捕蛇，捕蛇。你为了练功，逼得我们拼着性命到处捕蛇，逼得小白变成了一条巨蟒。"
    hide guoshi with dissolve
    "突然，远处的山谷传来了巨响，你听出了那是小白爬动的声音。"

    menu xu_forth_three:
        "置之不理。":
            show xiaobai_ with dissolve
            "你没有理会那巨响，过了一会，小白来到了村子，仇人见面分外眼红，马上和国师打了起来，你和其他村民被战斗的余波击飞了出去，死伤无数。"
            "弥留之际，你的耳边传来了一道玄妙的声音，那是【生生不息的激荡】，忽然你发现自己回到了上一次做出选择的时刻。"
            hide xiaobai_ with dissolve
            jump xu_forth_three
        "前去拦住小白。":
            show guoshi with dissolve
            axuan talk"她来了，快放开我，我能拦住她。"
            guoshi "也罢，你去吧。"
            hide guoshi with dissolve
    scene bg 19
    "你来到了捕蛇村附近的峡谷，将小白和小青拦了下来。"
    axuan talk "小白，如果你与国师开战的话，村子就会毁了，不知有多少村民会家破人亡，收手吧。"
    axuan talk "小白，你听我说，我把自己变成妖了，我们俩都是妖了。"
    axuan talk "你身形巨大，那又怎么样？天地这么大，容下多少山川湖海。我虽然是个最弱最小的妖，但我会拼尽全力去保护你。如果世间容不下我们，我们就一起去这天地的尽头，八荒四海，总有个容身之所。"
    scene bg 20
    "正当她犹豫不决之际，异变突生，天空中突然升起一道半球形的壁垒，将你们三人困在了里面，黑色的大手从天而降，将你们三个牢牢压在了地上。"
    jump xu_fifth_section

