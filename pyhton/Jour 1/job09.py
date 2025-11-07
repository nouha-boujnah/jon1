nom="mascara"
prix_unitaire= 42
quantité_stock= 30
print ("nom:",nom )
print("prix_unitaire:",prix_unitaire)
print ("quantité_stock:", prix_unitaire)
print(f"{nom}for{prix_unitaire} is a portal for {quantité_stock}.")

vente= int(input("combien de prduit veut tu achter ?"))
nouveau_stock= (quantité_stock - vente)
print (nouveau_stock)
inflattion= prix_unitaire * 1.10
print (inflattion)









