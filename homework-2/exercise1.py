
num_list = [2, 5, 7, 10, 14, 17, 18, 21, 27, 30]

#Make function
def even_odd(x):
    #Loop function over list
    for i in x:
        #Make conditionals to see if even or odd
        if i % 2 == 0:
            print(str(i) + " even")
        else:
            print(str(i) + " odd")

even_odd(num_list)