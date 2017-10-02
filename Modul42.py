#this is how you make module
def main():
    x = 42 #modulo
    y = []

    for i in range(0,10):
        z = int(input("Enter Any Number Here :"))
        f = int(z%x)
        y.append(f)

    j = len(set(y))
    print("Total Distinct Value =",j)

main()