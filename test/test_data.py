#此文件的作用是初始化一些测试集

#协同过滤推荐系统测试集
#初始化时135用户相似，246相似，09相似，78相似
#假设物品0是美剧，1是美国动漫，2美国历史，3是美国动作片，4是日本动漫，5是日本动作片，6日本爱情片，7中国动画片，8中国动作片
test_cf = [
    [0, 1, 0, 1, 0, 0, 0, 1, 0], #0 动漫爱好者
    [1, 1, 1, 1, 0, 0, 0, 0, 0], #1 美国人
    [0, 0, 0, 0, 1, 1, 1, 0, 0], #2 日本人
    [1, 1, 1, 1, 0, 0, 0, 0, 0], #3
    [0, 0, 0, 0, 1, 1, 1, 0, 0], #4
    [1, 1, 1, 1, 0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 1, 1, 1, 0, 0], #6
    [0, 0, 0, 1, 0, 1, 0, 0, 1], #7动作片爱好者
    [0, 0, 0, 1, 0, 1, 0, 0, 1], #8
    [0, 1, 0, 1, 0, 0, 0, 1, 0] #9
    ]