#create a function that prints the first 150 prime numbers
def print_primes():
    #create a list of the first 150 prime numbers
    primes = []
    i = 2
    while len(primes) < 150:
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1

    #print the list of prime numbers
    print(primes)


'''
    q: What is the purpose of machine learning?
    a: To make predictions based on data

    q: What is the purpose of a machine learning model?
    a: To make predictions based on data

    q: What is the purpose of a machine learning algorithm?
    a: To make predictions based on data


'''