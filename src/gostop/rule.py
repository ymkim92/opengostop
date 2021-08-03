# 총통: 같은 카드를 4장 모두 가지고 있을 경우 7점을 내고 스톱을 하거나, 고를 하고 계속 진행할 수 있음
#   - 시작시 바닥에 같은 카드 4장이 깔릴 경우 선이 4장을 모두 가져감.

def check_4cards(a_card_list):
    cnt = 0
    hash_list = [0]*12
    ret = []
    for x, y in a_card_list:
        hash_list[x] += 1
        if hash_list[x] == 4:
            ret.append(x)

    return ret

def decide_go_stop(user):
    pass