def diff_inverse_modulo(point1, point2, modulo):
    EC_lambda = 0
    
    for i in range(modulo):
        if ((point2[0] - point1[0]) * i) % modulo == (point2[1] - point1[1]) % modulo:
            return i

def same_inverse_modulo(point1, point2, modulo, A):
    EC_lambda = 0
    
    for i in range(modulo):
        if ((2 * point1[1]) * i) % modulo == ((3 * (point1[0])**2) + A) % modulo:
            return i

def EC_addition(point1, point2, modulo, A, diff_lambda, same_lambda):
    point3 = [0, 0]
    
    if point1 != point2:
        point3[0] += (diff_lambda**2 - point1[0] - point2[0]) % modulo
        point3[1] += (diff_lambda * (point1[0] - point3[0]) - point1[1]) % modulo
        print point3
    else:
        point3[0] += (same_lambda**2 - point1[0] - point2[0]) % modulo
        point3[1] += (same_lambda * (point1[0] - point3[0]) - point1[1]) % modulo
        print point3

def main():
    point1 = []
    point2 = []
    point1 += input('What is the coordinate of P? ')
    point2 += input('What is the coordinate of Q? ')
    A = input('What is the value of A? ')
    modulo = input('What is the modulo value? ')
    multiply = input('How many times do you want to iterate? ')

    for i in range(multiply - 1):
        diff_lambda = diff_inverse_modulo(point1, point2, modulo)
        same_lambda = same_inverse_modulo(point1, point2, modulo, A)
        point_update = EC_addition(point1, point2, modulo, A, diff_lambda, same_lambda)
        point1 = point_update

        print point1

main()
