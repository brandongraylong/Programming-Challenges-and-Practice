# Problem Statement:
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Problem URL:
# https://leetcode.com/problems/coin-change/


def coin_change(coins: list, amount: int) -> int:
    coins = sorted(coins)[::-1]
    coin_arr_len = len(coins)
    coin_curr_idx = 0
    coin_curr_amt = 0
    num_coins = 0

    while(True):
        if coin_curr_amt + coins[coin_curr_idx] <= amount:
            coin_curr_amt += coins[coin_curr_idx]
            num_coins += 1
        else:
            coin_curr_idx += 1
            if coin_curr_idx == coin_arr_len:
                return -1
        if coin_curr_amt == amount:
            return num_coins

def main():
    coins = [15, 25, 1]
    amount = 60
    print(coin_change(coins, amount))

if __name__ == '__main__':
    main()
