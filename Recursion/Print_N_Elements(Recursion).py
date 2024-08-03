def fun(count,N):
    if count > N:
        return
    else:
        print(count,end=" ")
        fun(count+1,N)


def main():
    count = 1
    N = 10
    fun(count,N)

if __name__ == "__main__":
    main()