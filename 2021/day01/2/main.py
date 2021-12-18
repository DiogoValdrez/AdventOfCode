import sys

def main(filename):
    count = 0
    pr = sys.maxsize
    with open(filename, "r") as f:
        var1,var2,var3 = f.readline(),f.readline(),f.readline()
        while var1 != "" and var2 != "" and var3 != "":
            r = eval(var1) + eval(var2) + eval(var3)
            var1,var2,var3 = var2,var3,f.readline()
            if r > pr :
                count += 1
            pr = r
        print(count)
if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
    