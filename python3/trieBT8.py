# Mảng products
products = ["cat", "banana", "obama", "batman", "car", "cow", "alibaba"]

# Duyệt qua mảng và in ra chỉ số của phần tử bắt đầu bằng "ba"
for i in range(len(products)):
    if products[i][:2] == "ba":
        print(f'Phần tử "{products[i]}" có chỉ số {i}')



