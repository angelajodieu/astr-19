#code for jounral 1, session 3

#f function, returns x cubed + 8
def f(x):
    return x**3 + 8

#main function
def main():
    x = 9
    result = f(x)
    #print result of the function
    print(result)
    #prints YAY! if result is greater than 27
    if result > 27:
        print("YAY!")

if __name__=="__main__":
    main()
