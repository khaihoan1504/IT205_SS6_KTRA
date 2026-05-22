qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:
    print('1. Xem báo cáo tồn kho')
    print('2. Nhập kho')
    print('3. Xuất kho')
    print('4. Cảnh báo hàng tồn kho thấp')
    print('5. Thoát chương trình')
    
    choice = int(input('Nhập lựa chọn: '))
    print()
    
    match choice:
        case 1:
            print('Laptop: ', end='')
            if qty_laptop > 0:
                for i in range(qty_laptop):
                    print('*', end='')
                print()
            else:
                print('0')
            
            print('Phone: ', end='')
            if qty_phone > 0:
                for i in range(qty_phone):
                    print('*', end='')
                print()
            else:
                print('0')
                
            print('Tablet: ', end='')
            if qty_tablet > 0:
                for i in range(qty_tablet):
                    print('*', end='')
                print()
            else:
                print('0')
            print()
        case 2:
            while True:
                print('1-Laptop, 2-Phone, 3-Tablet')
                choice_2 = int(input('Nhập lựa chọn: '))
                
                if not(1 <= choice_2 <= 3):
                    print('Sai lựa chọn, vui lòng nhập lại!')
                    continue
                
                while True:
                    qty = int(input('Nhập số lượng nhập kho: '))
                    if qty > 0:
                        break
                    else: 
                        print('Số lượng không hợp lệ, vui lòng nhập lại!')
                    
                match choice_2:
                    case 1:
                        qty_laptop += qty
                        break
                    case 2:
                        qty_phone += qty
                        break
                    case 3:
                        qty_tablet += qty
                        break
            print()
        case 3:
            while True:
                print('1-Laptop, 2-Phone, 3-Tablet')
                choice_2 = int(input('Nhập lựa chọn: '))
                
                if not(1 <= choice_2 <= 3):
                    print('Sai lựa chọn, vui lòng nhập lại!')
                    continue
                
                
                match choice_2:
                    case 1:
                        while True:
                            qty = int(input('Nhập số lượng nhập kho: '))
                            if qty > qty_laptop:
                                print('Số lượng xuất kho lớn hơn số lượng tồn kho!')
                                continue
                            elif qty > 0:
                                qty_laptop -= qty
                                break
                            else:
                                print('Không nhập số âm!')
                    case 2:
                        while True:
                            qty = int(input('Nhập số lượng nhập kho: '))
                            if qty > qty_phone:
                                print('Số lượng xuất kho lớn hơn số lượng tồn kho!')
                                continue
                            elif qty > 0:
                                qty_phone -= qty
                                break
                            else:
                                print('Không nhập số âm!')
                    case 3:
                        while True:
                            qty = int(input('Nhập số lượng nhập kho: '))
                            if qty > qty_tablet:
                                print('Số lượng xuất kho lớn hơn số lượng tồn kho!')
                                continue
                            elif qty > 0:
                                qty_tablet -= qty
                                break
                            else:
                                print('Không nhập số âm!')
                break
            print()
        case 4:
            if qty_laptop < 10:
                print(f'[Cảnh báo] Mặt hàng laptop sắp hết (chỉ còn {qty_laptop})')
            if qty_phone < 10:
                print(f'[Cảnh báo] Mặt hàng laptop sắp hết (chỉ còn {qty_phone})')
            if qty_tablet < 10:
                print(f'[Cảnh báo] Mặt hàng laptop sắp hết (chỉ còn {qty_tablet})')
            print()
        case 5:
            print('Thoát chương trình!')    
            break
        case 0:
            print('Thoát chương trình!')    
            break
                    
            