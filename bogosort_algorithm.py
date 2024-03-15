import random

original_list = [0, 1, 2, 3, 4, 5]
shuffling_list = original_list.copy()
loop = 0
tries = 1
attempts_list = []

def test(original, shuffled, attempts):
    while shuffled != original:
        random.shuffle(shuffled)
        attempts += 1
    return attempts

while loop < 100:
    tries = test(original_list, shuffling_list, tries)
    attempts_list.append(tries)
    loop += 1
    random.shuffle(shuffling_list)
    tries = 0

average = sum(attempts_list) / len(attempts_list)
print('average:', average)
