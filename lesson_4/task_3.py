WEALTH_TAX = 0.10
PERSENT_PULL = 0.015
BONUS = 0.03
MULTIPLICITY_OF_BILLS = 50

balance = 0


def accrual_of_percent_all_operations(func):
    """Начисления за каждую n операцию"""
    def wrapper(*args, **kwargs):
        
        bills = func(*args, **kwargs)
        if bills != balance:
            wrapper.operation += 1
        if not wrapper.operation % 3 and wrapper.operation != 0:
            bills = bills + bills * BONUS
            
        if bills > 5_000_000:
            bills = bills - bills * .10

        return bills
        
    wrapper.operation = 0
    return wrapper


@accrual_of_percent_all_operations
def pull(balance, cash):
    """Снимает денежные средства"""
    money = balance - cash - cash * PERSENT_PULL
    return money if not cash % 50 and cash <= balance and 30 <= cash <= 600 else balance


@accrual_of_percent_all_operations
def push(balance, cash):
    """Кладем денежные средства"""
    return balance + cash if not cash % 50 else balance


def select_an_operation(item):
    """Выбираает операцию c деньгами поступления/расход"""
    global balance
    match item:
        case 1:
            cash = int(input('Введите сумму которую хотите получить: '))
            balance = pull(balance, cash)
            print(balance)
        case 2:
            cash = int(input('Введите сумму которую хотите положить: '))
            balance = push(balance, cash)
            print(balance)


def run():
    """Запускает банкомат"""
    operation = True
    while operation:
        operation = int(input('Введите команду:\n1. снять;\n2. положить;\n0. выйти.\n'))
        if operation == 0:
            continue
        
        select_an_operation(operation)
    

def main():
    run()


if __name__ == '__main__':
    main()
  