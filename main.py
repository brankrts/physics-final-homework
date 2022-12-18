from Question1 import *
from Question2 import *
from Question3 import *


Q1 = Question1()
Q2 = Question2()
Q3 = Question3()


def main():

    # Soru 1 :
    vectors = [{'length': 4, 'degree': 75, 'area': 2},
               {'length': 6, 'degree': 30, 'area': 1
                }, {'length': 3, 'degree': 50, 'area': 3}]

    Rsize, Rdegree = Q1.solve(vectors)
    print("Toplam Vektörünün Büyüklüğü -->", Rsize,
          "\nR eksen ile yapılan açı -->", Rdegree)
    # Soru 2 :
    isGoal = Q2.isGoal()
    if(isGoal):
        print("Gol olmuştur")
    else:
        print("Gol değildir")

    # Soru 3 :

    a = Q3.findTfirst()
    b = Q3.findTend()

    print("A şıkkının cevabı : -> T =", a, "N")
    print("B şıkkının cevabı : -> T =", b, "N")


main()
