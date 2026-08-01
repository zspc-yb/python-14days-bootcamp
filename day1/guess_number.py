import random

target = random.randint(1, 100)
guess_count = 0

while True:
    print("Guess a number between 1 and 100:")
    guess = int(input("你的猜测是: "))
    guess_count += 1

    if guess < target:
        print("太小了！")
    elif guess > target:
        print("太大了！")
    else:
        print(f"恭喜你，猜对了！你用了{guess_count}次猜中了{target}。")
        break