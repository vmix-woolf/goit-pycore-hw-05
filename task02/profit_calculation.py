import re 
from typing import Callable

def generator_numbers(text: str):
    pattern = re.compile(r'\s\d*\.\d{2}\s')  # get all float numbers
    profits_list = re.findall(pattern, text)
    
    for profit in profits_list:
        yield float(profit.strip())  # rectify each profit number and return it to calling function


def sum_profit(text: str, func: Callable) -> float:
    sum = 0
    for profit_value in func(text):
        sum += profit_value  # summarize sequential profits sent by generator func()
    
    return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як \
    основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
