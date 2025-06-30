#1
import threading
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_range(start, end, result):
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)

if __name__ == "__main__":
    start = int(input("Boshlanish: "))
    end = int(input("Tugash: "))
    n_threads = int(input("Iplar soni: "))

    threads = []
    results = [[] for _ in range(n_threads)]

    length = (end - start + 1) // n_threads
    for i in range(n_threads):
        s = start + i * length
        e = s + length - 1
        if i == n_threads - 1:
            e = end
        t = threading.Thread(target=check_range, args=(s, e, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes = []
    for sublist in results:
        primes.extend(sublist)
    primes.sort()

    print("Tub sonlar:", primes)
#2
import threading
from collections import Counter

def count_words(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        counter.update(local_counter)

if __name__ == "__main__":
    filename = input("Fayl nomini kiriting: ")
    num_threads = int(input("Nechta ip ishlatsin? "))

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads

    threads = []
    global_counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i != num_threads - 1 else total_lines
        t = threading.Thread(target=count_words, args=(lines[start:end], global_counter))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("So'zlar soni:")
    for word, count in global_counter.most_common():
        print(f"{word}: {count}")
