'''
- 대표적인 문자열 매칭 알고리즘
- 우리가 브라우저에서 ctrl+f를 통해 찾고자하는 문자열을 검색하는 행위와 비슷한 동작을 한다.
- kmp 알고리즘의 핵심은 패턴의 접두사와 접미사 개념을 적극 활용하여 '반복되는 연산을 얼만큼 건너뛸 수 있는 지'에 대해 집중한다는 것이다.
- 패턴 내에 존재하는 접두사와 접미사가 '일치' 한다면 접미사를 접두사로 다시 바라봄으로써 문자열 탐색을 이어서 진행할 수 있기 때문이다.
- 
'''

def compute_lps(pattern):
    """
    패턴 문자열에 대한 Longest Prefix Suffix(LPS)를 계산하는 함수
    """
    lps = [0] * len(pattern)
    length = 0  # 이전 인덱스까지의 일치하는 접두사와 접미사의 길이

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    KMP 알고리즘을 사용하여 패턴 문자열을 찾는 함수
    """
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)

    i, j = 0, 0  # 텍스트 및 패턴 문자열에서의 인덱스

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                print("패턴이 텍스트에서 발견된 인덱스:", i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
