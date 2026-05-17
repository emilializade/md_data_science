import numpy as np

def score_game(predict_func) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм"""
    count_ls = []
    # фиксируем сид для воспроизводимости
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score

def game_core_v3(number: int = 1) -> int:
    """Угадываем число, используя бинарный поиск"""
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict = (low + high) // 2
        if predict == number:
            break
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1
    return count

if __name__ == "__main__":
    # Вызов функции оценки
    print('Run benchmarking for game_core_v3: ', end='')
