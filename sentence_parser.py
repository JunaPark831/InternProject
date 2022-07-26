"""
STT 
"""

#from ast import pattern
from lib2to3.pytree import convert
import string
import sys

from phone_number import phone_number_exception 
sys.path.append("./")

import new_language
import into_digit
import pattern_language
import tag_correction
import month_exception
import text_to_list
import pos
import convert
import transform_index
import bad_words
import phone_number
import text_to_list
import into_digit

def exceptionNR(nr_list):
    copy = nr_list
    list_nr_but_no = text_to_list.TextIntoList("exception_nr.txt")
    #list_nr_but_no = ['조','억','만','하나','둘','셋','넷','다섯','여섯','일곱','여덟','아홉','열']
    for ind, each_nr in enumerate(nr_list):
        if each_nr != ():
            for exception in list_nr_but_no:
                if each_nr[0] == exception:
                    null_info = ()
                    copy[ind] = null_info
    return copy
'''
def BringNumber(sentence: str) -> list:
    """문장에서 NR숫자들을 element로 가지는 list를 반환"""

    sentence_pos = tag_correction.apply_tag_correction(sentence)
    #print(sentence_pos)
    sentence_pos = exceptionNR(sentence_pos)
    #print(sentence_pos)
    numbers = []
    number = ""

    for ind, key in enumerate(sentence_pos):
        if key != ():
            if key[1] == "NR":
                txt_ind = transform_index.get_txt_ind(sentence, ind)
                if  sentence[txt_ind-1] == " " and number != "":
                    numbers.append(number)
                    number = ""
                number += key[0]
                if ind-1 < len(sentence_pos):
                    if ind+1 == len(sentence_pos) or sentence_pos[ind+1][1] != "NR":
                        numbers.append(number)
                        number = ""
    return numbers
'''
#BringNumber에서 NR앞에 오는것이 NR이고 그 사이에 띄워쓰기가 있으면 새로 분리하게끔

def BringNumber(sentence):
    #list1 = tn.checkTwo(sentence)
    #list1 = pos.get_pos(sentence)
    list1 = tag_correction.apply_tag_correction(sentence)
    f = []
    for a in list1:
        if a[1] != 'NR':
            b=()
            f.append(b)
        else:
            f.append(a)
    f = exceptionNR(f)
    string_list = []
    str = ''
    NR_index_in_sentence = 0
    for ind, a in enumerate(f):
        b = ()
        if a != b:
            if f[ind-1] != b:
                txt_ind = transform_index.get_text_ind(sentence, ind)
                txt_ind2 = transform_index.get_text_ind(sentence, ind-1)
                if txt_ind2 == None:
                    difference = 1
                else:   difference = txt_ind - txt_ind2 
                if difference != 1:
                    string_list.append((str,transform_index.get_text_ind(sentence, NR_index_in_sentence)))
                    str=f[ind][0]
                    NR_index_in_sentence = ind
                else:
                    if str == '':
                        NR_index_in_sentence = ind
                    str += a[0]
            else:
                if str =='':
                    NR_index_in_sentence = ind
                str += a[0]
        else:
            if str != '':
                string_list.append((str,transform_index.get_text_ind(sentence, NR_index_in_sentence)))
                str = ''
        if f[ind] != b and ind ==len(f)-1:
            string_list.append((str,transform_index.get_text_ind(sentence, NR_index_in_sentence)))
    print(string_list)
    return string_list



'''
def PutNumber(sentence: str) -> str:
    """문장input에 digit대입한 문장output return"""

    numbers = bad_words.remove_bad_words(BringNumber(sentence))
    if not any(number in sentence for number in numbers):
        return sentence
    for number in numbers:
        for ind, sentence_char in enumerate(sentence):
            if sentence_char != number[0]:
                continue
            pos_ind = transform_index.get_pos_ind(sentence, ind)
            sentence_pos = tag_correction.apply_tag_correction(sentence)
            if sentence[ind:min(len(sentence),ind+len(number))] == number and sentence_pos[pos_ind][1] == "NR":
                sentence = sentence[:ind] + into_digit.ToDigit(number) + sentence[min(len(sentence),ind+len(number)):]
                break
    return sentence
'''
'''
def standing_alone(sentence):
    sentence_pos = pos.get_pos(sentence)
    sentence_pos = exceptionNR(sentence_pos)
    print(sentence_pos)
    for i in range(1,len(sentence_pos)-1):
        if sentence_pos[i] == ():
            continue
        if sentence_pos[i-1] !=():
            if sentence_pos[i-1][1] != 'NR':
                continue
        if sentence_pos[i+1] !=():
            if sentence_pos[i+1][1] != 'NR':
                continue
        where = transform_index.get_text_ind(sentence, i)
        sentence = sentence[:where]+into_digit.ToDigit(sentence_pos[i][0])+sentence[where+1:]
        return sentence
    return sentence
'''
'''
#기존 PutNumber
def PutNumber(sentence):
    #numList = tn.checkTwo(sentence)
    numList = BringNumber(sentence)

    #print(numList)
    copy = ''
    new = ''
    #string일부 가져오는법 [a:b] a에서 b-1위치까지 가져온다.
    #a is an index value
    for num in numList:
        ind_in_sentence = len(copy)
        while ind_in_sentence <= len(sentence)-1:
            if sentence[ind_in_sentence] != num[0]:
                new += sentence[ind_in_sentence]
                ind_in_sentence +=1
            else:
                if sentence[ind_in_sentence:ind_in_sentence+len(num)] == num:
                    new += into_digit.ToDigit(num)
                    copy = sentence[0:ind_in_sentence+len(num)]
                    ind_in_sentence = len(sentence)
                else:
                    new += sentence[ind_in_sentence]
                    ind_in_sentence +=1
    return new +sentence[len(copy):]
'''
def PutNumber(sentence):
    #numList = tn.checkTwo(sentence)
    numList = BringNumber(sentence)
    result =''
    ind_in_sentence = 0
    for num in numList:
        result += sentence[ind_in_sentence:num[1]] + into_digit.ToDigit(num[0])
        ind_in_sentence = num[1] + len(num[0])
    return result + sentence[ind_in_sentence:]


def main(sentence: str) -> str:
    """worker function"""
    #sentence = phone_number.phone_number_exception(sentence)
    sentence = new_language.apply_dictionary(sentence)
    # print('1:',sentence)
    sentence = pattern_language.apply_before(sentence)
    sentence = PutNumber(sentence)
    # print('2:',sentence)
    sentence = month_exception.get_month_exception(sentence)
    # print('3:',sentence)
    sentence = pattern_language.apply_regular_expression(sentence)
    sentence = new_language.apply_dictionary(sentence)
    # print('4:',sentence)
    return sentence
'''
print(main("나는 이번 유월 사일에 본 시험에서 영점 사프로를 받았어."))
print(main("나는 이번 시월 사일에 본 시험에서 영점 사점을 받았어."))
print(main("이번 삼 회 추경예산안은 고용 사회안전망 강화와 경기 보강을 위해서."))
print(main("성원이 되었으므로 제삼백칠십구 회 국회임시회 제일 차 문화체육관광위원회를 개의하겠습니다."))
print(main("나는 지금 오십만육천원을 가지고 있어"))
print(main("나는 이에서 시금치 이개가 나왔어"))
print(main("삼 사 오 칠 구 십삼. 삼천칠백만원을 소비하셨습니다."))
print(main("요번 팔월에 나는 코로나일구에 걸렸었어"))
print(main("이 개년 동안 백범 김구 선생님께서는 백제유물을 탐방하셨다."))
print(main("나는 이월에 이월할거야"))
print(main("의사일정 제이 항과 문화체육관광부 및 문화재청 소관 이천이십 년도 제삼 회 추가경정예산안 의사일정 제삼 항 이천이십 년도 문화예술진흥기금운용 계획 변경안 의사일정 제사 항 이천이십 년도 영화발전기금운용 계획 변경안 의사일정 제오 항 이천이십 년도 관광진흥개발기금운용 계획 변경안"))
print(main("내 무게는 이십삼오십스물"))
print(main('내 전화번호는 공일공 이이이이 일일일일입니다. 니 전화번호는 뭐니?'))
print(main('오 오 칠 칠 팔 구십삼 사십 팔 나는 삼삼오오이야'))
'''

#print(main("백범김구선생님이 만드셨다. 제일 문재는 오만한 태도에서 오는 것이다. 일본인만 김재은을 좋아한다."))

#print(PutNumber("우리 제일 법안심사 소위원회는 지난 사월 이십팔 일 총 팔십한 건의 법률안을 심사하여 한 건은 수정안으로 채택하고 스물일곱 건은 통합 조정하여 두 건의 대안으로 제안하기로 의결하였습니다."))
#print(BringNumber("우리 제일 법안심사 소위원회는 지난 사월 이십팔 일 총 팔십한 건의 법률안을 심사하여 한 건은 수정안으로 채택하고 스물일곱 건은 통합 조정하여 두 건의 대안으로 제안하기로 의결하였습니다."))
#print(BringNumber("오 구 오 구. 안녕하세요 저는 삼백만입니다. 이 칠 구 십삼"))



#print(BringNumber("나는 이에서 시금치 이개가 나왔어"))
#print(pos.get_pos("나는 이번 시월 사일에 본 시험에서 영점 사점을 받았어."))
#print(transform_index.get_text_ind("오천육백. 기증 문화재를 약 천여 점 기증받았습니다.",4))

#print(main("지난 일월 이십이 일 국가공무원법 제삼십일 조의 이에 따라 대통령이 제출하고 일월 이십오 일 국회법 제육십오 조의 이에 따라 우리 위원회에 회부된 문화체육관광부 장관 후보자에 대한 인사청문회를 실시하기 위한 것입니다."))
'''
print(main("구 쪽에서 십이 조 십이 쪽까지입니다."))
print(pos.get_pos("김주열 열사 한분이 헌사해 주셨습니다."))
print(main("이천십구 년 이십일 일 퍼센트보다 무려 세 배 가까이 늘어난 수치입니다."))
print(main("너가 뭐라고 이팔백팔 뭐라하든 내가 쉽게 바뀔거 같아? 오백만 번을 더 해도 너는 일도 나한테 안먹힐거야"))
print(into_digit.ToDigit("이팔팔"))
'''

#print(main("지식과 사람을 연결하는 도서관을 위해 코로나 일구로부터 안전하고 편리하게 이용할 수 있는 서비스 환경을 구축하고 일일구에 신고해야 되는거 아냐??"))
#print(main("국립중앙도서관은 장애인도서관은 이천이십 년 유월 사 일 자로 문화체육관광부장관 소속 소관의 일 차 소속 기관으로 승격된 새내기 조직입니다."))
'''
import re
regex_num ='월\s*(가-힣0-9+)\s*일'
regex_num ='([가-힣|0-9]+)\s*월\s*[가-힣|0-9|일]+\s*일'
regex_num = '[가-힣|0-9]+\s*월\s*([가-힣|0-9]+[일]*)\s*일'
sentence = "나는 오월 칠일이 생일이다."
re_iter = re.finditer(regex_num, sentence)
for s in re_iter:
    print(s.group(1))
    print(s.start())
    print(s.end())
    sentence = sentence[:s.start()] + sentence[s.start():s.end()].replace(s.group(1), convert.get_number(s.group(1))) + sentence[s.end():]
print(sentence)
'''

#print(main("다음은 팔 쪽입니다."))
print(pos.get_pos("삼 인당 지원금을 연 십 만 원으로 인상하고 수혜 인원을 백구십칠만 명으로 증대함으로써 저소득층의 문화 향유 여건이 개선되도록 노력하고 있습니다 또한 코로나 십구 상황에서의 이용 활성화를 위하여 자동 재충전 제도의 도입 온라인 가맹점의 발굴 모바일 앱 출시 등을 비대면 서비스로 그~ 추진해 나가고 있습니다."))