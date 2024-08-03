def printElements(i,N):
    if i > 10:
        return
    printElements(i+1,N)
    print(i,end=" ")

def main():
    i = 1
    N = 10
    printElements(i,N)

if __name__ == "__main__":
    main()