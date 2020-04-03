def func1():
    animals = {'bird', 'dog', 'cat', 'rat'}
    animals.add('tiger')
    animals.remove('bird')
    for i in animals:
        print(len(i))
    #     print(type(i))
        # print(i)
    x = 23
    # func2(x)
    print(func2(x))

def func2(x):
    result = x + 2
    return result
    

def main(): 
    func1()     

if __name__ == "__main__":
    main()