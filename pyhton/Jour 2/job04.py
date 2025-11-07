N = int(input("Entrez un nombre entier supérieur à 0 : "))
for i in range(1, N+1):
    print(f"Table de multiplication de {i}")
    for j in range(1,10):
        print(f"{j}*{i}={j*i}")
        


