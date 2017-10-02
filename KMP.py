#this is how you make acronym program
def main ():
    x = input("Enter Names Here :").split("-")
    y = []

    for i in x:
         y.append(i[0])

    print("".join(y).upper())

main()