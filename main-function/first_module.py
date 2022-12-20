
def test():
    print ("first module's name {}".format(__name__))

if __name__ == '__main__':
    test()
else:
    print('first_module Ran from import statement')