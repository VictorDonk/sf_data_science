import numpy as np
def random_predict(number:int=1) -> int:
    count = 0
    min = 0
    max = 100
    while True:
          predict_number = round((min+max)/2)
          count += 1
          if number == predict_number:
              break
          elif number > predict_number:
               min = predict_number
          elif number < predict_number:
               max = predict_number
    return(count)
print(f'Количество попыток: {random_predict()}')
def score_game(random_predict) -> int:
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
score_game(random_predict)