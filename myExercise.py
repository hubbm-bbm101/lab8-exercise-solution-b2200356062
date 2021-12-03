import sys
f =  open(sys.argv[1])
username = [x for x in sys.argv[2].split(",")]
print(username)
d = {}
for line in f:
    (key, val) = line.rstrip().split(":")
    d[key] = val.split(" ")
for name in username:
    try:        
        print("Name:",name+",","University:",*d[name])
    except KeyError:
        print("No record of '{}' was found!".format(name))
f.close()