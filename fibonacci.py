def fibonacci_sequence(terms):

    if terms == 0:
        return 0
    if terms == 1:
        return 1
    
    first_term = fibonacci_sequence(terms - 1)
    second_term = fibonacci_sequence(terms - 2)

    next_term = first_term + second_term
    return next_term

def main():
    terms = input('Which term would you like to display in the sequence? ')
    print fibonacci_sequence(terms)

main()
