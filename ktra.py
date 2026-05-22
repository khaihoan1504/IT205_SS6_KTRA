# Câu 1:
stock_quantity = int(input('Số lượng tồn kho: '))
if stock_quantity >= 50:
    print('Tình trạng: Hàng đầy kho')
elif 10 <= stock_quantity and stock_quantity < 50:
    print('Tình trạng: Mức an toàn')
elif stock_quantity < 10:
    print('Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm')
    
# Câu 2:
total_faulty_products = 0
while True:
    inp = int(input('Nhập số lượng hàng lỗi của từng quầy: '))
    if inp == -1:
        print(f'Tổng số hàng lỗi thu hồi trong ngày là: {total_faulty_products}')
        print('Thoát chương trình!')
        break
    else:
        total_faulty_products += inp
        
#Câu 3
ton_kho = 100
while True:
    inp = int(input('Số lượng muốn xuất: '))
    if inp < 0:
        print('Không được nhập số âm, vui lòng nhập lại!')
        continue
    elif inp > ton_kho:
        print('Kho không đủ hàng, vui lòng nhập lại!')
        continue
    else:
        ton_kho -= inp
        print('Xuất kho thành công!')
        print(f'Tồn kho còn lại: [{ton_kho}]')
        break