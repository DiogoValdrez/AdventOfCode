import sys

def main(filename):
    count = 0
    f = open(filename, "r")
    prev = 1000
    for var in f:
        var = eval(var)
        if(var > prev):
            count+=1
        prev = var
    print(count)
if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))