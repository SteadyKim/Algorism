def get_stars(n):
    matrix = []
    
    for i in range(len(n) * 3):

        if ( i // (len(n)) ) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)


    return matrix
 
 
star = ["***", "* *", "***"]
n = int(input())
e = 0
while n != 3:
    n = int(n / 3)
    e+= 1
 
for i in range(e):
    star = get_stars(star)
for i in star:
    print(i)