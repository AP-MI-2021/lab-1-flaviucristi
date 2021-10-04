'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n<2:
    return False
  else:
    for i in range(2,n//2+1):
      if n%i==0:
        return False
  return True



  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p=1
  for i in lst:
    p=p*i
  return p

  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  d=x
  i=y

  while i>0:
    r=d%i
    d=i
    i=r

  return d

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x!=y:
    if x>y:
      x=x-y
    else:
      y=y-x
  return x
  
  
def main():
  while True:
    print("1. Determinati daca numarul este prim")
    print("2. Calculeaza produsul a n numere")
    print("3. Determina cel mai mare divizor comun prin prima metoda")
    print("4. Determina cel mai mare divizor comun prin a doua metoda")
    print("x. Iesire")

    optiune= input("Dati o optiune: ")

    if optiune == "1":
      n=int(input("Dati numar: "))
      print(is_prime(n))

    elif optiune == "2":
      lst=[]
      n=int(input("Dati numarul de numere: "))
      for i in range(1,n+1):
        lst.append(int(input("Dati numere: ")))
      print(get_product(lst))

    elif optiune=="3":
      x=int(input("Dati primul numar: "))
      y=int(input("Dati al doilea numar"))
      print(get_cmmdc_v1(x,y))

    elif optiune=="4":
      x = int(input("Dati primul numar: "))
      y = int(input("Dati al doilea numar"))
      print(get_cmmdc_v2(x, y))

    elif optiune=="x":
      break

    else:
      print("Optiune gresita! Reincearca")


if __name__ == '__main__':
  main()
