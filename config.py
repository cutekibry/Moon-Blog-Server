#!/usr/bin/python3

ojlink_patterns = {
    "AGC": lambda x: "https://atcoder.jp/contests/agc{0}/tasks/agc{0}_{1}".format(x[:-1-(not x[-1].isalpha())], x[-1-(not x[-1].isalpha())]),
    "BZOJ": lambda x: "https://www.lydsy.com/JudgeOnline/problem.php?id=%s" % x,
    "CF": lambda x: "http://codeforces.com/contest/%s/problem/%s" % (x[:-1-(not x[-1].isalpha())], x[-1-(not x[-1].isalpha())]),
    "CFGYM": lambda x: "http://codeforces.com/gym/%s/problem/%s" % (x[:-1-(not x[-1].isalpha())], x[-1-(not x[-1].isalpha())]),
    "HDU": lambda x: "http://acm.hdu.edu.cn/showproblem.php?pid=%s" % x,
    "LOJ": lambda x: "https://loj.ac/problem/%s" % x,
    "LGOJ": lambda x: "https://www.luogu.org/problem/%s" % x,
    "SPOJ": lambda x: "https://www.spoj.com/problems/%s/" % x,
    "UOJ": lambda x: "http://uoj.ac/problem/%s" % x,
    "ZJU": lambda x: "http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=%s" % x,
}

globals = {
    "AUTHOR": "Tsukimaru Oshawott",
    "SITE_NAME": "Tsuki's blog",
    "ARTICLES_PER_PAGE": 50,
}

tags = [
    # Space
    ["", ""],

    # Special
    ["未翻译", "red"],
    ["未完成", "red"],

    ["提交答案", "teal"],
    ["交互题", "teal"],

    # Articles
    ["Moon", "teal"],
    ["空", "black"],
    ["游记", "green"],
    ["算法", "green"],
    ["文章", "green"],
    ["杂项", "green"],
    ["随想", "green"],

    # Sources
    ["AtCoder", "blue"],
    ["BestCoder", "blue"],
    ["BZOJ", "blue"],
    ["Codeforces", "blue"],
    ["HDU", "blue"],
    ["LGOJ", "blue"],
    ["LOJ", "blue"],
    ["Project Euler", "blue"],
    ["SPOJ", "blue"],
    ["USACO", "blue"],
    ["ZJU", "blue"],

    ["2001", "blue"],
    ["2002", "blue"],
    ["2003", "blue"],
    ["2004", "blue"],
    ["2005", "blue"],
    ["2006", "blue"],
    ["2007", "blue"],
    ["2008", "blue"],
    ["2009", "blue"],
    ["2010", "blue"],
    ["2011", "blue"],
    ["2012", "blue"],
    ["2013", "blue"],
    ["2014", "blue"],
    ["2015", "blue"],
    ["2016", "blue"],
    ["2017", "blue"],
    ["2018", "blue"],
    ["2019", "blue"],
    ["2020", "blue"],

    ["AHOI", "blue"],
    ["BJOI", "blue"],
    ["CQOI", "blue"],
    ["HAOI", "blue"],
    ["HEOI", "blue"],
    ["HNOI", "blue"],
    ["JLOI", "blue"],
    ["JSOI", "blue"],
    ["JXOI", "blue"],
    ["SCOI", "blue"],
    ["SDOI", "blue"],
    ["SHOI", "blue"],
    ["SNOI", "blue"],
    ["TJOI", "blue"],
    ["YNOI", "blue"],
    ["ZJOI", "blue"],
    ["联合省选", "blue"],

    ["山东省队集训", "blue"],
    ["雅礼集训", "blue"],
    ["清华集训", "blue"],

    ["集训队互测", "blue"],

    ["美团 CodeM", "blue"],

    ["一本通", "blue"],

    ["NOIP", "blue"],
    ["NOI", "blue"],
    ["WC", "blue"],
    ["CTSC", "blue"],
    ["THUSC", "blue"],
    ["THUPC", "blue"],
    ["THUWC", "blue"],
    ["PKUSC", "blue"],
    ["PKUPC", "blue"],
    ["PKUWC", "blue"],

    ["APIO", "blue"],
    ["CEOI", "blue"],
    ["IOI", "blue"],
    ["JOI", "blue"],
    ["POI", "blue"],
    ["ROI", "blue"],

    ["模板", "blue"],
    ["原创", "blue"],

    # Algorithms
    # ["数据结构", "pink"],
    ["ST 表", "olive"],
    ["队列", "olive"],
    ["单调队列", "olive"],
    ["单调栈", "olive"],
    ["并查集", "olive"],
    ["树状数组", "olive"],
    ["线段树", "olive"],
    ["线段树合并", "olive"],
    ["线段树分治", "olive"],
    ["堆", "olive"],
    ["可并堆", "olive"],
    ["平衡树", "olive"],
    ["字典树", "olive"],
    ["树套树", "olive"],
    ["启发式合并", "olive"],
    ["分块及按大小分类", "olive"],
    ["莫队", "olive"],
    ["树链剖分", "olive"],
    ["欧拉序", "olive"],
    ["离线", "olive"],
    ["可持久化", "olive"],
    ["点分治", "olive"],
    ["线性基", "olive"],
    ["Bitset", "olive"],
    ["差分", "olive"],
    ["虚树", "olive"],
    ["Link-Cut Tree", "olive"],

    # ["图论", "pink"],
    ["最短路", "olive"],
    ["差分约束系统", "olive"],
    ["K 短路", "olive"],
    ["最小生成树", "olive"],
    ["二分图匹配", "olive"],
    ["欧拉回路", "olive"],
    ["缩点", "olive"],
    ["2-SAT", "olive"],
    ["网络流", "olive"],
    ["最大流", "olive"],
    ["费用流", "olive"],
    ["最小割", "olive"],
    ["最小割树", "olive"],
    ["有上下界网络流", "olive"],
    ["哈夫曼编码", "olive"],
    ["矩阵树定理", "olive"],
    ["LGV 定理", "olive"],

    # ["数学", "pink"],
    ["概率与期望", "olive"],
    ["高斯消元", "olive"],
    ["二分", "olive"],
    ["矩阵", "olive"],
    ["多项式", "olive"],
    ["DFT（含 NTT）及 FFT", "olive"],
    ["高维卷积", "olive"],
    ["二项卷积", "olive"],
    ["FWT", "olive"],
    ["位运算", "olive"],
    ["异或", "olive"],
    ["组合计数", "olive"],
    ["生成函数", "olive"],
    ["容斥原理", "olive"],
    ["Min-Max 容斥", "olive"],
    ["博弈论", "olive"],
    ["拉格朗日插值", "olive"],
    ["伯努利数", "olive"],
    ["斯特林数", "olive"],

    # ["数论", "pink"],
    ["原根", "olive"],
    ["莫比乌斯反演", "olive"],
    ["中国剩余定理", "olive"],
    ["Lucas 定理", "olive"],
    ["欧拉函数", "olive"],
    ["杜教筛", "olive"],
    ["洲阁筛", "olive"],
    ["质因数分解", "olive"],

    # ["DP", "pink"],
    ["背包 DP", "olive"],
    ["区间 DP", "olive"],
    ["划分 DP", "olive"],
    ["环形 DP", "olive"],
    ["数位 DP", "olive"],
    ["树形 DP", "olive"],
    ["斜率优化", "olive"],

    # ["字符串", "pink"],
    ["AC 自动机", "olive"],
    ["KMP", "olive"],
    ["Hash", "olive"],
    ["Manacher", "olive"],
    ["回文自动机", "olive"],
    ["回文树", "olive"],

    # ["搜索", "pink"],
    ["DFS", "olive"],
    ["BFS", "olive"],
    ["启发式搜索", "olive"],
    ["深度迭代搜索", "olive"],

    # Others
    ["01 分数规划", "olive"],
    ["分治", "olive"],
    ["CDQ 分治", "olive"],
    ["整体二分", "olive"],
    ["凸优化", "olive"],
    ["贪心", "olive"],
    ["随机化", "olive"],
    ["思维题", "olive"],

    ["数据结构", "pink"],
    ["图论", "pink"],
    ["数学", "pink"],
    ["数论", "pink"],
    ["DP", "pink"],
    ["字符串", "pink"],
    ["搜索", "pink"],
]

sentences = [
    # OIers
    ["人的所作所为，大抵都是因自己的意愿而进行的。那么，也就总该有些时候，要听从自己内心的声音，即使为此要放弃很多，但只要自己觉得有意义，那么，再多牺牲也无所谓。", "AntiLeaf"],

    ["自己选的路，跪着走完吧！", "Bunnycxk"],
    ["时间越来越少了，jw 的题量真的好多，我不得不努力，也不得不迎头赶上。", "Bunnycxk"],
    ["高中的 OI 刚刚开始，希望不要那么快就凋零。兔纸的时间已经不多，请把自己选择的路，好好走下去。", "Bunnycxk"],

    ["<a href=\"https://loj.ac/problem/2142\">相逢问候</a>你全家，<a href=\"https://loj.ac/problem/2145\">分手祝福</a>你祖宗。", "Codesonic"],

    ["惊觉往事历历已经年，机房依旧喧攘间。相觑犹问客从何处来，不见故人泪阑珊。", "<a href=\"https://www.bilibili.com/video/av201769837/\">CommonAnts</a>"],
    ["我自幼便听说了精益求精，追求完美的品质；我同样深谙先行而后言的道理；我拥有广泛的兴趣和幸福的生活。但这三点的结合却注定是一个悲剧。", "<a href=\"https://loj.ac/article/1757\">CommonAnts</a>"],

    ["树的直径有人不会的吗？... 你看那些说不会的一般都是假的。", "czl"],
    ["然后如果这样这样这样这样，那么就有这样。那么，显然！", "czl"],
    ["黄同学，你树链剖分学傻了吧？", "czl"],
    ["和我高一比？... 那要看是什么时候的高一...", "czl"],
    ["我知道你会了，不用说了。", "czl"],

    ["这就是 OIer 的选择。", "hjw"],
    ["呵呵，那只是你的以为。", "hjw"], 
    # ["orz", "hjw"],
    # ["用 hy 定理就好了。", "hjw"],

    # ["你是鬼吧...", "Henry_y"],
    # ["怎么改？你强行改啊...", "Henry_y"],
    # ["这题不是直接取模吗？", "Henry_y"],
    # ["这题我写过啊...", "Henry_y"],

    ["成为很厉害很厉害的人，最重要的，就是要热血，永远也不要让你的血凉下去。", "hzwer"],

    ["历史的车轮仍然在行驶着。我们是车辙前的尘土。", "iotang"],
    ["不过你们快去拿 Au 吧！这样与我竞争的人就会变少。加油啊，还在 OI 世界中存活的家伙。", "iotang"],

    # ["优秀的人，到哪里都是很优秀的。", "kkksc03"],

    ["不知道这样的训练是否有用呢，ZJOI 会告诉我答案吧。", "Memset0"],

    # ["级 150 轻轻松松！", "Tsukimaru"],
    # ["明天开始到期末考结束，我会暂时断网。", "Tsukimaru"],
    ["BZOJ 刷题量没上千，你也好意思在这里说话？", "Tsukimaru"],

    ["啊，好几万老师！", "wjd"],

    ["你都刷那么多题了，快去颓废！", "zcmimi"],
    ["不要 gay 里 gay 气...", "zcmimi"],

    # ["= =", "ZincSabian"],
    ["要么刷题，要么睡觉，你选一个。", "ZincSabian"],
    ["lmh 我真 tm 羡慕你的闲。", "ZincSabian"],
    ["lmh 我和你很熟么？", "ZincSabian"],
    # ["考试加油啊 qwq", "ZincSabian"],
    ["删好友了，再见。", "ZincSabian"],
    ["学了 OI 后悔三年，不学 OI 后悔一辈子。", "ZincSabian"],

    ["无穷的远方，无穷的学长，都与我无关。", "洛克园艺师"],

    ["别慌，WA 的颜色也很好看——但时间永远不会等待你。", "千柒"],

    # Grade 8 Teachers
    # ["积累本儿~", "魏老师"],

    # Grade 9 Teachers
    # ["这个 “良实”，默写的时候别写错。", "赵老师"],
    # ["我这个，可以说是 “二十四孝” 的老师了。", "赵老师"],

    ["不用再给我送茶叶了！", "翁老师"],
    ["考成这样你还好意思说话？", "翁老师"],
    ["你要记住：你是毕业班的同学，你是毕业班的同学，你是毕业班的同学！", "翁老师"],
    ["有些黑暗，只能你自己一个人跨过。", "翁老师"],

    # ["lmh，你作文写得跟兔子尾巴似的。", "程老师"],
    # ["你是全村人的希望啊！", "程老师"],

    ["Q 吸，等于 CM 得儿↘塔↗T↘", "廖老师"],
    ["这个东西都不会写啊？……差劲！", "廖老师"],
    ["臭小子，期末没有 85 分，我寒假给你布置 10 套试卷！", "廖老师"],

    ["啧啧啧... 优秀！优秀的 14 班！", "杨老师"],
    ["你们要记住，你们是连 “王在法下” 都背得出来的同学！", "杨老师"],
    ["这次考试考不好的话，不要担心，让它随风而去吧。", "杨老师"],
    # ["古代埃及，圈一圈。", "杨老师"],

    # ["金刚石当然可以烧，只要有钱就行吧？", "化学老师"],

    # Others
    # ["你们现在非常优秀，我希望你们能够更加优秀。", "李校长"],

    # Litterateurs
    ["无穷的远方，无数的人们，都与我有关。", "鲁迅"],
    ["悟已往之不谏，知来者之可追。实迷途其未远，觉今是而昨非。舟遥遥以轻飏，风飘飘而吹衣。问征夫以前路，恨晨光之熹微。", "陶渊明"],

]

links = [
    ["Online Judges", [
        ["https://loj.ac/", "LibreOJ"],
        ["https://www.luogu.org/", "LGOJ"],
    ]],
]
