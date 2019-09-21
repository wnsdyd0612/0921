#최유승 씨의 주민등록번호는 020612_3XXXX17이다. 최유승 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

pin = "020612-3XXXX17"

yyyymmdd = pin[:6] #처음부터 6자리

num = pin[7:] #끝부터 7자리

print(yyyymmdd)  

print(num)       