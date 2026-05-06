import math
import random


# 1. Basic arithmetic and math functions
def demo_arithmetic_and_math():
    print("\n=== 1. Basic Arithmetic and Math Functions ===")
    a = 10
    b = 3

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor division:", a // b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)

    print("Cos(pi/4):", math.cos(math.pi / 4))
    print("Log(42.89):", math.log(42.89))
    print("Sqrt(256):", math.sqrt(256))
    print("Exp(3):", math.exp(3))


# 2. Newton's law of gravitation
def gravitation_force(m1, m2, r):
    G = 6.674e-11
    return G * m1 * m2 / (r ** 2)


def demo_gravitation():
    print("\n=== 2. Newton's Law of Gravitation ===")

    f1 = gravitation_force(1.989e30, 5.972e24, 149597870000)
    print("Gravitational force between Earth and Sun:", f1, "N")

    f2 = gravitation_force(70, 0.5, 0.75)
    print("Gravitational force between 70 kg and 0.5 kg:", f2, "N")


# 3. Ideal Gas Law
R = 8.31446261815324


def pressure_from_v_t(n, V, T):
    return n * R * T / V


def volume_from_p_t(n, P, T):
    return n * R * T / P


def temperature_from_p_v(n, P, V):
    return (P * V) / (n * R)


def ideal_gas_moles(P, V, T):
    return (P * V) / (R * T)


def demo_ideal_gas():
    print("\n=== 3. Ideal Gas Law ===")
    n = 1

    P = pressure_from_v_t(n, 0.25, 300)
    print("Pressure:", P, "Pa")

    V = volume_from_p_t(n, 500, 321)
    print("Volume:", V, "m^3")

    T = temperature_from_p_v(n, 2.5e3, 1e-5)
    print("Temperature:", T, "K")

    moles = ideal_gas_moles(500, 0.25, 300)
    print("Moles from P, V, T:", moles, "mol")


# 4. Normal distribution PDF
def normal_pdf(mu, sigma, x):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))


def demo_normal_distribution():
    print("\n=== 4. Normal Distribution PDF ===")
    print("y1 =", normal_pdf(0, 1, 0.5))
    print("y2 =", normal_pdf(3, 0.1, -2.8))
    print("y3 =", normal_pdf(-1, 3, -1))


# 5. String operations
def demo_strings():
    print("\n=== 5. String Operations ===")
    name = "Nihat"
    version = 1

    print("Hello " + name)
    print("I am %s%d" % (name, version))
    print("I am {}{}".format(name, version))
    print(f"I am {name}{version}")

    text = " \tHello World\n"
    print("Strip:", text.strip())
    print("Upper:", "python".upper())
    print("Lower:", "PYTHON".lower())
    print("Replace:", "banana".replace("a", "o"))


# 6. Conditional statement
def classify_age(age):
    if age < 24:
        return "Young"
    elif 24 <= age < 60:
        return "Middle-age"
    else:
        return "Senior"


def demo_conditional():
    print("\n=== 6. Conditional Statement ===")
    for age in [18, 35, 70]:
        print(f"Age {age}: {classify_age(age)}")


# 7. Credit card decision tree
def credit_card_decision(age, is_student=False, excellent_credit=False):
    if age < 24:
        if is_student:
            return "APPROVED"
        return "DENIED"
    elif 24 <= age < 60:
        return "APPROVED"
    else:
        if excellent_credit:
            return "APPROVED"
        return "DENIED"


def demo_credit_card():
    print("\n=== 7. Credit Card Decision Tree ===")
    print("Age 20, student=True:", credit_card_decision(20, is_student=True))
    print("Age 20, student=False:", credit_card_decision(20, is_student=False))
    print("Age 40:", credit_card_decision(40))
    print("Age 70, excellent_credit=True:", credit_card_decision(70, excellent_credit=True))
    print("Age 70, excellent_credit=False:", credit_card_decision(70, excellent_credit=False))


# 8. Problem solving flowchart
def troubleshooting(works, broke_it=None, anyone_knows=None, trouble=None, blame=None):
    if works:
        return "DON'T MESS WITH IT!"
    else:
        if broke_it:
            if anyone_knows:
                return "SORRY TO HEAR THAT!"
            return "HIDE IT!"
        else:
            if not trouble:
                return "THROW IT AWAY!"
            else:
                if blame:
                    return "NO PROBLEM!"
                return "SORRY TO HEAR THAT!"


def demo_flowchart():
    print("\n=== 8. Problem Solving Flowchart ===")
    print(troubleshooting(True))
    print(troubleshooting(False, broke_it=True, anyone_knows=False))
    print(troubleshooting(False, broke_it=False, trouble=False))
    print(troubleshooting(False, broke_it=False, trouble=True, blame=True))


# 9. While loop
def find_first_even(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            return numbers[index]
        index += 1
    return None


def demo_while_loop():
    print("\n=== 9. While Loop ===")
    numbers = [5, 7, 9, 11, 14, 17]
    print("First even number:", find_first_even(numbers))


# 10. For loop vowel counter
def count_vowels(word):
    count = 0
    for c in word.casefold():
        if c in "aeiou":
            count += 1
    return count


def demo_vowel_counter():
    print("\n=== 10. For Loop Vowel Counter ===")
    word = "Education"
    print(f"Word: {word}")
    print("Number of vowels:", count_vowels(word))


# 11. Multiples of n from 1 to 100
def multiples_from_1_to_100(n):
    result = []
    for i in range(1, 101):
        if i % n == 0:
            result.append(i)
    return result


def multiples_n(n, a=1, b=10):
    result = []
    for i in range(a, b + 1):
        if i % n == 0:
            result.append(i)
    return result


def demo_multiples():
    print("\n=== 11. Multiples of n from 1 to 100 ===")
    for n in [2, 3, 7, 9]:
        print(f"Multiples of {n}:", multiples_from_1_to_100(n))

    print("multiples_n(4, 1, 12):", multiples_n(4, 1, 12))


# 12. Caesar Cipher
def caesar_cipher(text, shift):
    result = ""

    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            result += ch

    return result


def demo_caesar_cipher():
    print("\n=== 12. Caesar Cipher ===")
    message = "HELLO WORLD"
    shift = 3

    encrypted = caesar_cipher(message, shift)
    decrypted = caesar_cipher(encrypted, -shift)

    print("Original :", message)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)


# 13. Terms of the series and iterative sum
#     sum from n=0 to N of (3 + 2n) / 2^n
def build_series_terms(N):
    terms = []
    for n in range(N + 1):
        term = (3 + 2 * n) / (2 ** n)
        terms.append(term)
    return terms


def iterative_sum(values):
    total = 0
    for v in values:
        total += v
    return total


def series_sum(N):
    return iterative_sum(build_series_terms(N))


def demo_series():
    print("\n=== 13. Terms of the Series and Iterative Sum ===")
    for N in [5, 10, 100]:
        terms = build_series_terms(N)
        total = iterative_sum(terms)
        print(f"\nN = {N}")
        print("Terms:", terms if N <= 10 else "Too many terms to display fully.")
        print("Sum:", total)


# 14. Lists and list operations
def demo_lists():
    print("\n=== 14. List Operations ===")
    L = [3, 4, 5]
    print("Original list:", L)

    L[0] = 7
    print("After L[0] = 7:", L)

    L.append(9)
    print("After append(9):", L)

    L.extend([1, 2])
    print("After extend([1, 2]):", L)

    L.insert(2, "X")
    print("After insert(2, 'X'):", L)

    removed = L.pop()
    print("After pop():", L)
    print("Popped item:", removed)

    if "X" in L:
        L.remove("X")
    print("After remove('X'):", L)

    print("Length:", len(L))
    print("Slice L[1:4]:", L[1:4])


# 15. String split and join
def demo_split_join():
    print("\n=== 15. String Split and Join ===")
    s = "3,4,5,6,7"
    parts = s.split(",")
    print("Split:", parts)

    joined = "<->".join(["TAG", "JOUR", "DAY"])
    print("Join:", joined)


# 16. List comprehensions / iterative built lists
def demo_list_comprehensions():
    print("\n=== 16. List Comprehensions ===")
    L = list(range(5))
    print("list(range(5)):", L)

    pairs = [[i, j] for i in range(2) for j in range(2)]
    print("Pairs:", pairs)

    squares = [i ** 2 for i in range(1, 6)]
    print("Squares:", squares)

    odds = [i for i in range(10) if i % 2 != 0]
    print("Odds:", odds)


# 17. User-defined function examples
def hello():
    print("Hello!")


def greet(name):
    print("Hello, " + name + ". Good morning!")


def dice():
    return random.randint(1, 6)


def absolute_value(num):
    if num >= 0:
        return num
    return -num


def nroot(arg, n=2):
    return arg ** (1 / n)


def demo_functions():
    print("\n=== 17. User-defined Functions ===")
    hello()
    greet("Mickey Mouse")
    print("Dice roll:", dice())
    print("Absolute value of -25:", absolute_value(-25))
    print("Square root of 25:", nroot(25))
    print("Cube root of 8:", nroot(8, 3))


# 18. Scope example
def scope_demo_function():
    x = 10
    print("Value inside function:", x)


def demo_scope():
    print("\n=== 18. Scope Example ===")
    x = 20
    scope_demo_function()
    print("Value outside function:", x)


# Main runner
def main():
    demo_arithmetic_and_math()
    demo_gravitation()
    demo_ideal_gas()
    demo_normal_distribution()
    demo_strings()
    demo_conditional()
    demo_credit_card()
    demo_flowchart()
    demo_while_loop()
    demo_vowel_counter()
    demo_multiples()
    demo_caesar_cipher()
    demo_series()
    demo_lists()
    demo_split_join()
    demo_list_comprehensions()
    demo_functions()
    demo_scope()


if __name__ == "__main__":
    main()
