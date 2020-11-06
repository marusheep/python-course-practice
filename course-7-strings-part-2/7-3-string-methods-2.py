# rjust() and ljust()

print("hello world".rjust(15))
print("hello world".ljust(15) + "space checking")

#.center()

print("hellp world".center(10,":"))

#.trip() / .rstrip() / .lstrip()

print("111 I have an excited trip!11111")
print("111 I have an excited trip!11111".strip("1"))
print("111 I have an excited trip!11111".rstrip("1"))
print("111 I have an excited trip!11111".lstrip("1"))

#.replace()

print("good morning".replace("morning","afternoon"))