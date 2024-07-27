## int() -> 주어진 문자열을 특정 진법으로 해석하여 10진법 정수로 변환
int('1010', 2)  # 2진법 -> 10진법: 결과는 10
int('A', 16)    # 16진법 -> 10진법: 결과는 10
int('ZZZZZ', 36)  # 36진법 -> 10진법: 결과는 60466175

## bin() -> 10진법 정수를 2진법 문자열로 변환
bin(10)  # 결과는 '0b1010'

## oct() -> 10진법 정수를 8진법 문자열로 변환
oct(10)  # 결과는 '0o12'

## hex() -> 10진법 정수를 16진법 문자열로 변환
hex(10)  # 결과는 '0xa'

## Custom
## 10진법을 다른 진법으로 변환하는 함수
def to_base(n, b):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = chars[n % b] + result
        n //= b
    return result or "0"

print(to_base(60466175, 36))  # 결과는 'ZZZZZ'

## 다양한 진법 변환
def convert_base(num, from_base, to_base):
    # Convert from `from_base` to decimal
    decimal_num = int(num, from_base)
    # Convert from decimal to `to_base`
    if to_base == 10:
        return str(decimal_num)
    
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while decimal_num > 0:
        result = chars[decimal_num % to_base] + result
        decimal_num //= to_base
    return result or "0"

print(convert_base("ZZZZZ", 36, 10))  # 36진법 -> 10진법: 결과는 '60466175'
print(convert_base("60466175", 10, 36))  # 10진법 -> 36진법: 결과는 'ZZZZZ'