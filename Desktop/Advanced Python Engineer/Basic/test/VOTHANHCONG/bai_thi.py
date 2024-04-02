from libs.xu_ly_du_lieu import *

file_input = 'files/hoc_sinh.csv'
file_output = 'files/ket_qua.csv'
lstHS = doc_file_csv(file_input) 
#Em đọc file hoc_sinh.csv ra lstHS trước sau đó tính toán trên biến lstHS rồi tính toán điểm tb và xếp loại,
# sau đó lưu vào ket_qua.csv

print('CHƯƠNG TRÌNH QUẢN LÝ HỌC SINH')
while True:
    print('1: Thêm học sinh\n2: Danh sách học sinh\n3: Tra cứu học sinh\n4: Xóa học sinh\n5: Tính điểm trung bình và xếp loại\n6: Lưu kết quả')
    option = int(input('Chọn chức năng cần thực hiện: '))
    if option == 1:
        them_hoc_sinh(lstHS)
    elif option == 2:
        ds_hoc_sinh(lstHS)
    elif option == 3:
        masohs = input('Cho biết Mã HS: ')
        hs = tra_cuu_hs(lstHS, masohs)
        if hs == None:
            print('Không tìm thấy')
        else:
            in_hs(hs)
    elif option == 4:
        masohs = input('Cho biết Mã HS: ')
        result = xoa_hs(lstHS, masohs)
        if result == 1:
            print('Đã xóa')
        else:
            print('Xóa không thành công')
    elif option == 5:
        diemtrungbinh = tinh_dtb_xep_loai(lstHS)
    elif option == 6:
        result = luu_dshs_to_file(file_output, lstHS)
        if result == 1:
            print('Đã lưu')
    else:
        break
    
    chon = input('Ban co muon tiep tuc khong: ')
    if chon != '1':
        break