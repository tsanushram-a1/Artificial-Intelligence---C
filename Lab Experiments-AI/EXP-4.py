from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for p in permutations(range(10), len(letters)):
    values = dict(zip(letters, p))

    # First letters cannot be zero
    if values[word1[0]] == 0 or values[word2[0]] == 0 or values[result[0]] == 0:
        continue

    num1 = int("".join(str(values[c]) for c in word1))
    num2 = int("".join(str(values[c]) for c in word2))
    num3 = int("".join(str(values[c]) for c in result))

    if num1 + num2 == num3:
        print("Solution:")
        print(word1, "=", num1)
        print(word2, "=", num2)
        print(result, "=", num3)
        break
