import math


def loc(num_list):
    return (sum(num_list))/(len(num_list))


def scale(num_list):
    l = loc(num_list)
    variance = sum((x - l) ** 2 for x in num_list) / len(num_list)
    return math.sqrt(variance)


def calc(k, num_list):
    s = scale(num_list)
    l = loc(num_list)
    return (l-(k*s)),(l+(k*s))


def run():
    n = 1
    n_lst = []
    inp = input(f'enter num{n} : ')
    while inp.lower() != 'c':
        try:
            n_lst.append(float(inp))
            n += 1
        except ValueError:
            print('invalid number, try again')

        inp = input(f'enter num{n} : ')

    k = input(f'enter k : ')
    try:
        c = calc(float(k),n_lst) 
        print(f'min : {c[0]}')
        print(f'max : {c[1]}')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run()
