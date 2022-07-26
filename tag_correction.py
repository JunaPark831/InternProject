import enum
import pos
import transform_index

# def num_two_correction(sentence: list) -> list:
#     if sentence.replace(" ",'') =='':
#         return pos.get_pos(sentence)
#     sen_pos = pos.get_pos(sentence)
#     newList =[]
#     place = 0
#     for i in range(len(sen_pos)-1):
#         if sen_pos[i]==('이', 'JKS'):
#             if sen_pos[i+1][1]=='NR':
#                 for a in range(place, len(sentence)):
#                     if sentence[a:a+2]=='이'+sen_pos[i+1][0]:
#                        newList.append(('이', 'NR'))
#                        place = a
#                        break
#             else: newList.append(sen_pos[i])
#         else: newList.append(sen_pos[i])
#     newList.append(sen_pos[len(sen_pos)-1])
#     return newList

UNITS = ["일", "이", "삼", "사", "오", "육", "칠", "팔", "구",]


def subject_case_marker22(sentence:str, sentence_pos: list) -> list:
    for pos_ind, pos_key in enumerate(sentence_pos):
        if pos_key[0] in UNITS and pos_key[1] == "JKS" and sentence_pos[pos_ind+1][1] == "NR" and sentence[transform_index.get_txt_ind(sentence, pos_ind)-1] == " ":
            sentence_pos[pos_ind] = (pos_key[0], "NR")
    return sentence_pos

def subject_case_marker(sentence):
    if sentence.replace(" ",'') =='':
        return pos.get_pos(sentence)
    sen_pos = pos.get_pos(sentence)
    newList =[]
    place = 0
    for i in range(len(sen_pos)-1):
        if sen_pos[i]==('이', 'JKS'):
            if sen_pos[i+1][1]=='NR':
                for a in range(place, len(sentence)):
                    if sentence[a:a+2]=='이'+sen_pos[i+1][0]:
                       newList.append(('이', 'NR'))
                       place = a
                       break
            else: newList.append(sen_pos[i])
        else: newList.append(sen_pos[i])
    newList.append(sen_pos[len(sen_pos)-1])
    return newList

def fixing_NR_after_MM(sentence_pos: list) -> list:
    filtered_pos = sentence_pos
    for i in range(len(sentence_pos)-1):
        if sentence_pos[i] != () and sentence_pos[i+1] != ():
            if sentence_pos[i] == ('몇','MM') and sentence_pos[i+1][1]=='NR':
                filtered_pos[i+1] = (filtered_pos[i+1][0],'NONO')
    return filtered_pos

def fixing_NR_after_NNB(sentence_pos):
    filtered_pos = sentence_pos
    for ind in  range(1,len(sentence_pos)):
        if sentence_pos[ind] != () and sentence_pos[ind-1] != ():
            if sentence_pos[ind] == ('쪽','NNB') and sentence_pos[ind-1][1] == 'NNG':
                print("a")
                if sentence_pos[ind-1][0] in UNITS:
                    print("b")
                    filtered_pos[ind-1] = (filtered_pos[ind-1][0],'NR')
    return filtered_pos     
                
        

def apply_tag_correction(sentence: str) -> list:
    sentence_pos = pos.get_pos(sentence)
    sentence_pos = subject_case_marker(sentence)
    sentence_pos = fixing_NR_after_MM(sentence_pos)
    sentence_pos = fixing_NR_after_NNB(sentence_pos)
    return sentence_pos


if __name__ == "__main__":
    txt = "이 사업은 계획이 변경 이천이십 년 사월 십칠일에 나왔다."
    print(apply_tag_correction(txt))
    print(fixing_NR_after_NNB(pos.get_pos("구 쪽에서 십이 조 십이 쪽까지 입니다.")))