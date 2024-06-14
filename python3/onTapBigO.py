###Bài 2: Ôn Tập Big O Xác định BigO
a=1
b=2
while (a<3):        #O(log n)
    while (b<3):    #O(log n)
    a= a*2
    b= b*2

#O(logn)×O(logn)=O((logn)^2) 

###Bài 3: Ôn Tập Big O  
for a in range(0, n):                  # n lần
    for b in range(a, n):              # (n - a) lần cho mỗi giá trị của a
        print("a")                     # n+(n−1)+(n−2)+…+1= [n(n+1)]/2 = O(n^2)


for c in range(0, n):                  # n lần
    for d in range(0, n):              # n lần
        print("a")                     # n * n = n^2   => O(n^2)

#  ====> O(n^2) + O(n^2)= 2[O(n^2)] => O(n^2) 

###Bài 1: Ôn Tập Big O
i = 0             #=> O(1)  --> 1
while (i < n):    #=> O(n) - vòng lặp này sẽ chạy n lần --> n
    i = i + 1     #=> O(n) - câu lệnh này được thực hiện n lần trong vòng lặp --> n

#---> F(n)= 1+2n
#---> O(n)