from Question1 import *

vectors = [{'length': 4, 'degree': 75, 'area': 2},
           {'length': 6, 'degree': 30, 'area': 1
            }, {'length': 3, 'degree': 50, 'area': 3}]

Q1 = Question1()


def main():

    Rsize, Rdegree = Q1.solve(vectors)
    print("Toplam Vektörünün Büyüklüğü -->", Rsize,
          "\nR eksen ile yapılan açı -->", Rdegree)


main()
