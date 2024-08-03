def printName(count,N):
    if count > N:
        return 
    else:
        print("GFG",end=" ")
        printName(count+1,N)

def main():
    count = 1
    N = 10
    printName(count,N)

if __name__ == "__main__":
    main()