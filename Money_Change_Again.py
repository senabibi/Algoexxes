def min_coins(money):
    coins = [1, 3, 4]
    minCoins = [0] + [money + 1] * money

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return minCoins[money]

# Convert the input string to an integer
money = int(input(" "))
print(min_coins(money))
