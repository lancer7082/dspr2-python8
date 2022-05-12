"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def bs_predict(number: int = 1) -> int:
    """Guess number using binary search method

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Guesses count
    """

    count = 0

    def bs_predict_interval(number: int = 1, nmin: int = 1, nmax: int = 100):
        """Randomly guess number

        Args:
            number (int, optional): Guessed number. Defaults to 1.
            nmin (int, optional): Min number in interval. Defaults to 1.
            nmax (int, optional): Max number in interval. Defaults to 100.
        """
        
        nonlocal count
                
        count += 1
        
        if nmin == nmax:
            predict_number = nmin
        else:    
            predict_number = nmin + (nmax - nmin) // 2
            
        if number == predict_number:
            return  # Exit if correct number   
        elif number < predict_number:
            bs_predict_interval(number, nmin - 1, predict_number + 1)
        else: 
            bs_predict_interval(number, predict_number - 1, nmax + 1)
                
        return
                             
    bs_predict_interval(number)
    
    return count
    
    
def score_game(predict_method) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_method(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(bs_predict)