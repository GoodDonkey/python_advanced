# my_script.py

# python3 my_script.py result.txt
# python3 my_script.py -o result.txt -l DEBUG -c ...

import sys

# positional argument 0 은 보통 지금 파일 이름.
print(sys.argv[0])

# positional argument 1 부터는 실행할 때 넣어주는 argument 들
# argument를 주지 않으면 오류가 IndexError 발생
print(sys.argv[1])

# 모든 argument를 list에 담아준다.
print(sys.argv)
print(type(sys.argv))
