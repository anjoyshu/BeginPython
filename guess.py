import random
min = int(input('請輸入猜數字的範圍(起): '))
max = int(input('請輸入猜數字的範圍(迄): '))
answer = random.randint(min,max)
print(answer)
guess = int(input('猜數字= '))
while answer != guess:
  if guess < answer:
    min = guess
    print('太小了, 再一次:(', min, '~', max, ')')
    guess = int(input())
  elif guess > answer:
    max = guess
    print('太大了, 再一次:(', min, '~', max, ')')
    guess = int(input())

print('賓果!')