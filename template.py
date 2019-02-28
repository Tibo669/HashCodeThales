
class Whatever:
    
    def __init__(self):
        self.var = 0

    def __str__(self):
        return var
    
    def __repr__(self):
        return var

if len(sys.argv) < 2:
    print("Missing file: hashcode2k19.py data.txt")
    sys.exit()

with(open(sys.argv[1])) as file:
    fileread = file.read()