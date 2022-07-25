try:
    from konlpy.tag import Mecab
except:
    from eunjeon import Mecab

mecab = Mecab()

def get_pos(txt):
    return mecab.pos(txt)

def get_morphs(txt):
    return mecab.morphs(txt)

if __name__ == "__main__":
    txt = "2번 3 회 추경예산안은 고용 사회안전망 강화와 경기 보강을 위해서."
    print(get_pos(txt))

    txt = "나는 코로나 일구에 감염됬었어"
    print(get_pos(txt))

    txt = "나는 이번 유일 사일에 본 시험에서 영점 사점을 받았어"
    print(get_pos(txt))

    txt = "나는 이번 유일 사일에 본 시험에서 영점 사프로를 받았어"
    print(get_pos(txt))