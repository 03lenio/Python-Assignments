with open("primes.txt", "w") as primes_file:
    for i in range(1000):
        for j in range(2, (i // 2) + 1):
            if (i % j) == 0:
                break
        else:
            primes_file.write(str(i))

