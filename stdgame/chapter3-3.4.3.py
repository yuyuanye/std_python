import random
import itertools

class player(object):
    def __init__(self, poker, bet_on):
        super(player, self).__init__()
        self.poker = poker
        self.bet_on = bet_on
    def sum_value(self):
        L = []
        for i in self.poker:
            if i[:-1] in ['10', 'J','Q','K']:
                num = 10
            elif i[0] == 'A':
                num = 1
            else:
                num = int(i[0])
        L.append(num)
        return L
    def poker_point(self):
        lst = self.sum_value()
        maxn = 0
        for j in itertools.combinations(lst,3):
            if sum(j) %10 == 0:
                k = sum(lst) % 10
                if k ==0:
                    return 10
                if k > maxn:
                    maxn = k
        return maxn
    def sorted_index(self):
        L = []
        for i in self.poker:
            index = poker_list().index(i)
            L.append(index)
        return max(L)
    def level_rate(self):
        point = self.poker_point()
        if point == 10:
            self.bet_on *=3
        elif 7 <= point < 10:
            self.bet_on *=2
        elif point <7:
            self.bet_on *= 1
        return self.bet_on
def poker_list():
    color = ['♦','♣','♠','♥']
    num_poker = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    sum_poker = [i + j for i in num_poker for j in color]
    return sum_poker

def main():
    print('游戏开始')
    value = int(input('请输入玩家的初始欢乐豆：'))
    i = 1
    while True:
        print('第 %s 局游戏开始！' % i)
        bet_on = int(input('请玩家输入赌注：'))
        if bet_on < 0:
            print('游戏结束')
            print('您剩下的欢乐豆为：',value)
            return
        else:
            L = poker_list()
            random.shuffle(L)
            hostpoker = L[:5]
            host_value = player(hostpoker, bet_on)
            host_sumpoint = host_value.poker_point()
            print('庄家的牌是：',hostpoker)
            print('庄家的点数是：',host_sumpoint)
            poker = L[5:10]
            player_value = player(poker, bet_on)
            play_sumpoint = player_value.poker_point()
            print('玩家的牌是：', poker)
            print('玩家的点数是：', play_sumpoint)
            if play_sumpoint == host_sumpoint:
                if player_value.sorted_index() > host_value.sorted_index():
                    print('这把您赢了')
                    value += player_value.level_rate()
                else:
                    print('这把您输了')
                    value -= host_value.level_rate()
            elif play_sumpoint > host_sumpoint:
                print('这把您赢了')
                value += player_value.level_rate()
            else:
                print('这把您输了')
                value -= host_value.level_rate()
            if value > 0:
                print('您的赌注还剩下：',value)
                print('游戏继续\n')
            else:
                print('您已经输光了欢乐豆，游戏结束')
                return
        i +=1
def test_func():
    t = poker_list()
    for i in poker_list():
        print(poker_list().index(i))

    random.shuffle(t)
    hostpoker = t[:5]
    print(hostpoker)
    L = []
    for i in hostpoker:
        print(i[:-1])
        if i[:-1] in ['10', 'J', 'Q', 'K']:
            num = 10
        elif i[0] == 'A':
            num = 1
        else:
            num = int(i[0])
    L.append(num)
    print(L)
if __name__ == '__main__':
    #main()
    test_func()


