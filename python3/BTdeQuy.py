def extract_ids(data):
    result = []

    def recurse(items):     #Hàm đệ quy
        for item in items:
            result.append({"id": item["id"]})        # Thêm một từ điển chứa id của phần tử đó vào result
            if "value" in item and item["value"]:    # Nếu phần tử có khóa "value" và giá trị của nó không rỗng, 
                recurse(item["value"])               # Gọi đệ quy trên danh sách value

    recurse(data)
    return result

# Dữ liệu mẫu
lstDemo = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [
                    {
                        "id": 3,
                        "value": [
                            {
                                "id": 4,
                                "value": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": 5,
        "value": []
    }
]

# Gọi hàm và in kết quả
result = extract_ids(lstDemo)
print(result)
