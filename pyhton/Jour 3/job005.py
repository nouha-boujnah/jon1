for number in range (2,1001):
    est_premier=True
    for i in range (2,number):
        if number % i == 0:
            est_premier=False
            break
    if est_premier:
        print(number)

    
