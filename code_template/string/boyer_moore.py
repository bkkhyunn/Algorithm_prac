'''
- Boyer Moore 알고리즘은 KMP알고리즘과 달리 오른쪽에서 왼쪽으로 비교 검사하며, 효과적으로 패턴문자열을 이동할수 있는 방법을 제시한다.
- 실제로 가장 많이 사용되고 있는 문자열 검색 알고리즘이 바로 Boyer Moore 알고리즘이다. 최고의 성능을 발휘 가능 O(n/m) 하기 때문이다.
- 파이썬의 문자열 함수 중 find(), MYSQL 의 LIKE, Postgresql 의 LIKE 또한 boyer moore 알고리즘으로 구현되어 있다.

- 보이어-무어 알고리즘은 오른쪽 끝 문자와 비교하여 점프를 진행하므로, 빠르게 검색 효율 높일 수 있다.
'''

def make_bad_match_table(pattern):
    """
    불일치 테이블 생성 함수

    Args:
    - pattern (str): 패턴 문자열

    Returns:
    - dict: 불일치 테이블
    """
    table = {}
    pattern_length = len(pattern)
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - i - 1
    table[pattern[-1]] = pattern_length  # 마지막 문자는 패턴 길이만큼 이동
    return table

def boyer_moore(text, pattern):
    """
    보이어-무어 알고리즘을 사용하여 주어진 텍스트에서 패턴을 검색하는 함수

    Args:
    - text (str): 검색할 텍스트 문자열
    - pattern (str): 검색할 패턴 문자열

    Returns:
    - int: 패턴이 발견된 인덱스 (찾지 못한 경우 -1 반환)
    """
    bad_match_table = make_bad_match_table(pattern)
    text_length = len(text)
    pattern_length = len(pattern)
    i = pattern_length - 1  # 텍스트 인덱스
    j = pattern_length - 1  # 패턴 인덱스

    while i < text_length:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # 일치하는 패턴의 시작 인덱스 반환
            else:
                i -= 1
                j -= 1
        else:
            # 불일치 시 패턴을 옮길 거리를 계산하여 최대값만큼 이동
            if text[i] in bad_match_table:
                max_shift = max(1, bad_match_table[text[i]])
            else:
                max_shift = pattern_length
            i += max_shift
            j = pattern_length - 1  # 패턴을 다시 오른쪽 끝에서부터 비교

    return -1  # 일치하는 패턴이 없을 경우

# 테스트
text = "ABAAABCD"
pattern = "ABC"
result = boyer_moore(text, pattern)
if result != -1:
    print("일치하는 패턴이 발견. 인덱스:", result)
else:
    print("일치하는 패턴을 찾을 수 없습니다.")
