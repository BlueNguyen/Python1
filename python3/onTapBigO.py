###Bài 2: Xác định BigO
a=1
b=2
while (a<3):        #O(log n)
    while (b<3):    #O(log n)
    a= a*2
    b= b*2

#O(logn)×O(logn)=O((logn)^2) 

###Bài 3: Big O notation 
for a in range(0, n):                  # n lần
    for b in range(a, n):              # (n - a) lần cho mỗi giá trị của a
        print("a")                     # n+(n−1)+(n−2)+…+1= [n(n+1)]/2 = O(n^2)


for c in range(0, n):                  # n lần
    for d in range(0, n):              # n lần
        print("a")                     # n * n = n^2   => O(n^2)

#  ====> O(n^2) + O(n^2)= 2[O(n^2)] => O(n^2) 