def calculate_coins(sum):
    if sum < 0:
        return False
    sum *= 100
    coins = [100,50,20,10,5,2,1]
    result = {}
    for coin in coins:
            count = 0
            while sum - coin >= 0:
                    count += 1
                    sum -= coin
            result[coin] = count
    return result
