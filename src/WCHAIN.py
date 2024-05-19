def longest_word_chain(words):
    # Створюємо множину слів для швидкого пошуку
    word_set = set(words)

    # Ініціалізуємо словник для замасковування проміжних результатів
    dp = {}

    # Ініціалізуємо максимальну довжину ланцюжка
    max_chain_length = 1

    # Проходимо по кожному слову
    for word in word_set:
        # Викликаємо рекурсивну функцію для обчислення максимальної довжини ланцюжка, починаючи з поточного слова
        chain_length = recurse(word, word_set, dp)

        # Оновлюємо максимальну довжину ланцюжка
        max_chain_length = max(max_chain_length, chain_length)

    # Повертаємо максимальну довжину ланцюжка
    return max_chain_length


def recurse(word, word_set, dp):
    # Якщо результат для поточного слова вже обчислений, повертаємо його
    if word in dp:
        return dp[word]

    # Ініціалізуємо максимальну довжину ланцюжка для поточного слова
    max_length = 1

    # Розглядаємо всі можливі варіанти видалення однієї літери зі слова
    for i in range(len(word)):
        new_word = word[:i] + word[i + 1:]

        # Якщо нове слово присутнє в множині слів
        if new_word in word_set:
            # Рекурсивно обчислюємо максимальну довжину ланцюжка, починаючи з нового слова
            length = 1 + recurse(new_word, word_set, dp)

            # Оновлюємо максимальну довжину ланцюжка для поточного слова
            max_length = max(max_length, length)

    # Замасковуємо результат для поточного слова
    dp[word] = max_length

    # Повертаємо максимальну довжину ланцюжка для поточного слова
    return max_length


# Читаємо вхідні дані з файлу wchain.in
with open('resources/wchain.in', 'r') as file:
    lines = file.readlines()
    N = int(lines[0])
    words = [line.strip() for line in lines[1:]]

# Знаходимо довжину максимального ланцюжка
result = longest_word_chain(words)

# Записуємо результат у файл wchain.out
with open('resources/wchain.out', 'w') as file:
    file.write(str(result))
