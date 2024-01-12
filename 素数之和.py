def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def sum_of_primes_in_range(start, end):
    primes = find_primes_in_range(start, end)
    return sum(primes)

start = int(input("请输入起始数："))
end = int(input("请输入结束数："))
result = sum_of_primes_in_range(start, end)
print(f"{start}到{end}之间的素数和为：{result}")
