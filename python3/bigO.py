#***BÀI TẬP 1: Xác định Big O notation
i = 0             #=> O(1)  --> 1
while (i < n):    #=> O(n) - vòng lặp này sẽ chạy n lần --> n
    i = i + 1     #=> O(n) - câu lệnh này được thực hiện n lần trong vòng lặp --> n

#---> F(n)= 1+2n
#---> O(n)


#***BÀI TẬP 2: Xác định Big O notation
i = 0               #=> O(1)  --> 1
while (i < n):      #=> O(n) - vòng lặp này sẽ chạy n/100 lần --> n/100
    i = i + 100     #=> O(n) - câu lệnh này được thực hiện n/100 lần trong vòng lặp --> n/100

#---> F(n)= 1+2n/100
#---> O(n)


#***BÀI TẬP 3: Xác định Big O notation
while (i < n):          # O(n) do i tăng lên 100 mỗi lần, nên chạy n/100 lần
    while (a < n):      # O(n^2) cho vòng lặp này
        while (b < n):  # O(n) cho vòng lặp này
            b = b + 1
        a = a + 1
    while (c < n):      # O(n) cho vòng lặp này
        c = c + 1
    i = i + 100                     


#---> F(n)= O(n)*O(n^2)             #(2n/100 + 4n^2/100 + 2n^3/100)
#---> O(n^3)






