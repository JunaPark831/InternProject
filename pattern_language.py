import re
import convert 
from typing import Dict


#NR처리할 부분의 group이름은 항상 change로!!
REGEX_NUMBERS = [
    '([가-힣|0-9]+)\s*점\s*[가-힣|0-9]+\s*[프로|점|퍼센트|그람|킬로]',
    '[가-힣|0-9]+\s*점\s*([가-힣|0-9]+)\s*[프로|점|퍼센트|그람|킬로]',
    '제([가-힣]+)\s*[항|조|목|차관|조항|항목|관|회|차]',
    
]
REGEX_NUMBERS_BEFORE = [
    '[가-힣|0-9]+\s*월\s*([가-힣|0-9]+[일]*)\s*(일+)',
    '[가-힣|0-9]+\s*년\s*([가-힣|0-9]+[일]*)\s*(일+)'
]
REGEX_TEXT_CORRECTIONS: Dict[str, str] = {
    '[0-9\s](\s*[점]\s+)[0-9]': ".",
    # ('[0-9]([\.\s]+)[0-9]',"."),
}

def apply_regular_expression(sentence: str) -> str:
    for regex_num in REGEX_NUMBERS:
        # regexp = re.compile(regex_num)
        re_iter = re.finditer(regex_num, sentence)
        for s in re_iter:
            sentence = sentence[:s.start()] + sentence[s.start():s.end()].replace(s.group(1), convert.get_number(s.group(1))) + sentence[s.end():]

    for regex_text in REGEX_TEXT_CORRECTIONS:
        # regexp= re.compile(regex_text)

        re_iter_text = re.finditer(regex_text, sentence)
        for s in re_iter_text:
            sentence = sentence[:s.start()] + sentence[s.start():s.end()].replace(s.group(1), REGEX_TEXT_CORRECTIONS[regex_text]) + sentence[s.end():]

        # if regexp.search(sentence):
        #     correction_in_sentnece = regexp.findall(sentence)
        #     for inst in correction_in_sentnece:
        #         sentence = sentence.replace(inst,regex_text[1])
    return sentence
def apply_before(sentence):
    for regex_num in REGEX_NUMBERS_BEFORE:
        # regexp = re.compile(regex_num)
        re_iter = re.finditer(regex_num, sentence)
        for s in re_iter:
            sentence = sentence[:s.start()] + sentence[s.start():s.end()].replace(s.group(1), convert.get_number(s.group(1))) + sentence[s.end():]
    return sentence

if __name__ == "__main__":
    print(apply_regular_expression('제육 조 제이십사 항을 참고바랍니다.'))
    print(apply_regular_expression("나는 이번 유 월 사일에 본 시험에서 9점 4점을 받았어."))
    print(apply_regular_expression("나는 이번 유월 사일에 본 시험에서 영점 사프로를 받았어."))
    None
