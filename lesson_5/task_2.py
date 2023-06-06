def considers_the_salary_of_employees(names, bets, awards):
    return {n: b * a for n, b, a in zip(names, bets, awards)}


def convert_awards_to_float(awards):
    return [float(award[:-1]) for award in awards]


def run():
    names = ['Иван', 'Екатерина', 'Марина', 'Станислав']
    bets = [3000, 500, 200, 400]
    awards = ['15.3%', '10.2%', '12.8%', '17.3%']
    
    awards = convert_awards_to_float(awards)
    res = considers_the_salary_of_employees(names, bets, awards)
    print(res)


if __name__ == '__main__':
    run()
