'''
Rabin Karp 알고리즘
    - 비교할 문자열과 패턴을 Hash function을 통해 해시값으로 변환
    - 해시값의 비교를 통해서 문자열이 일치하는지 확인
        - 일치하지 않으면 다음 문자열로 넘어가고
        - 일치한다면 해당 문자열과 패턴의 1:1 매칭을 통해서 최종적으로 일치하는지 확인
        - 해시값이 같지만 다른 문자열인 경우를 대비해서 해시값이 일치하는 경우에는 일대일 매칭으로 일치하는지 확인
    - 무차별 대입 매칭보다 빠르지 않지만 실제로는 복잡도가 O(n+m)
    - 좋은 해싱 기능을 사용하면 매우 효과적일 수 있으며 구현하기 쉽다.
'''

class RabinKarp:
    def __init__(self, pattern):
        self.pattern = pattern
        self.prime = 101  # 임의의 소수 사용
        self.base = 256    # ASCII 문자 수
        self.pat_hash = self._hash(pattern)
        self.pat_len = len(pattern)

    def _hash(self, s):
        """
        문자열 해시 함수
        """
        hash_val = 0
        for char in s:
            hash_val = (hash_val * self.base + ord(char)) % self.prime
        return hash_val

    def search(self, text):
        """
        주어진 텍스트에서 패턴을 검색하고 일치하는 모든 위치를 반환
        """
        text_len = len(text)
        text_hash = self._hash(text[:self.pat_len])

        matches = []
        for i in range(text_len - self.pat_len + 1):
            if text_hash == self.pat_hash and text[i:i+self.pat_len] == self.pattern:
                matches.append(i)
            if i < text_len - self.pat_len:
                # 다음 해시 계산
                text_hash = (self.base * (text_hash - ord(text[i]) * pow(self.base, self.pat_len - 1, self.prime)) + ord(text[i + self.pat_len])) % self.prime
                # 음수 방지
                text_hash += self.prime
                text_hash %= self.prime
        return matches
    
# 사용하기 쉬운 함수 버전
def rabin_karp(s, pattern):
	pattern_hash = hash(pattern)  # 1. 패턴의 hash값을 구한다
	n = len(pattern)

	for i in range(len(s)):
		s_hash = hash(s[i:i+n])     # 2. 문자열의 패턴의 길이만큼 hash값을 구한다.
		if pattern_hash == s_hash:  # 2-2 : 해쉬값이 일치하다면
			if pattern == s[i:i+n]: # 2-2-1 : 패턴과 문자열이 일치한지 확인
				return i

	return -1

# 예제 사용
pattern = "abc"
text = "ababcabcabababdabc"

rk = RabinKarp(pattern)
matches = rk.search(text)
if matches:
    print("패턴이 발견된 위치:", matches)
else:
    print("일치하는 패턴을 찾을 수 없습니다.")
