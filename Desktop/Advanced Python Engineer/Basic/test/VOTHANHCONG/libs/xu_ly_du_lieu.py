import csv

def check_mahs(lstHS, mahs_nhap):
    for hs in lstHS:
        if hs.get('mahs')==mahs_nhap:
            return True
    return False

def them_hoc_sinh(lstHS):
    while True:
        print('Nhập thông tin học sinh: ')
        mahs = ''
        while True:
            mahs = input('Mã học sinh: ')
            if check_mahs(lstHS, mahs):
                print('=== Mã học sinh đã tồn tại ===\n')
            else:
                break
        hoten = input('Họ tên học sinh: ')
        diemmon1 = input('Điểm môn 1: ')
        diemmon2 = input('Điểm môn 2: ')
        diemmon3 = input('Điểm môn 3: ')
        
        hs = {'mahs':mahs, 'hoten':hoten, 'diemmon1':diemmon1, 'diemmon2':diemmon2, 'diemmon3':diemmon3}
        lstHS.append(hs)
        n = input('Tiếp tục nhập? (1 để tiếp tục): ')
        if n != '1':
            break
    return

def tra_cuu_hs(lstHS, mahs_tracuu):
    for hs in lstHS:
        if hs['mahs']==mahs_tracuu:
            return hs
    return

def tinh_dtb_xep_loai(lstHS):
    for hs in lstHS:
        diem1, diem2, diem3 = map(float, [hs['diemmon1'], hs['diemmon2'], hs['diemmon3']])
        diem_trung_binh = (diem1 + diem2 + diem3) / 3
        if 0 < diem_trung_binh < 5:
            xep_loai = 'Kém'
        elif 5 <= diem_trung_binh < 6.5:
            xep_loai = 'Trung Bình'
        elif 6.5 <= diem_trung_binh < 8:
            xep_loai = 'Khá'
        elif 8 <= diem_trung_binh < 9:
            xep_loai = 'Giỏi'
        else:
            xep_loai = 'Xuất sắc'
        hs['trungbinh'] = round(diem_trung_binh, 2)
        hs['xeploai'] = xep_loai
    print('{:8}{:25}{:15}{:15}{:15}{:25}{:15}'.format('Ma HS','Ho ten','Mon 1','Mon 2','Mon 3','Diem trung binh','Xep loai'))
    for hs in lstHS:
        print('{:8}{:25}{:15}{:15}{:15}{:25}{:15}'.format(hs['mahs'],hs['hoten'],hs['diemmon1'],hs['diemmon2'],hs['diemmon3'],hs['trungbinh'],hs['xeploai']))
    return

def ds_hoc_sinh(lstHS):
    print('{:8}{:25}{:15}{:15}{:15}'.format('Ma HS','Ho ten','Mon 1','Mon 2','Mon 3'))
    for hs in lstHS:
        print('{:8}{:25}{:15}{:15}{:15}'.format(hs['mahs'],hs['hoten'],hs['diemmon1'],hs['diemmon2'],hs['diemmon3']))
    return

def in_hs(hs):
    print('{:8}{:25}{:15}{:15}{:15}'.format('Ma HS','Ho ten','Mon 1','Mon 2','Mon 3'))
    print('{:8}{:25}{:15}{:15}{:15}'.format(hs['mahs'],hs['hoten'],hs['diemmon1'],hs['diemmon2'],hs['diemmon3']))
    return
    
def luu_dshs_to_file(file_output, lstHS):
    lstLuu=[]
    lstLuu.append(['masv', 'hoten', 'diemmon1', 'diemmon2', 'diemmon3', 'trungbinh', 'xeploai'])
    for hs in lstHS:
        row = [hs['mahs'], hs['hoten'], hs['diemmon1'], hs['diemmon2'], hs['diemmon3'], hs['trungbinh'], hs['xeploai']]
        lstLuu.append(row)
    with open(file_output, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(lstLuu)
    return 1

def xoa_hs(lstHS, mahs_xoa):
    for i in range(len(lstHS)):
        if lstHS[i]['mahs'] == mahs_xoa:
            del(lstHS[i])
            return 1
    return 0

def doc_file_csv(file_input):
    with open(file_input, 'r', encoding='utf-8') as f:
        lstHS = []
        for hs in csv.reader(f):
            if hs[0] == 'Mã HS':
                continue
            hs = {'mahs':hs[0], 'hoten':hs[1], 'diemmon1':hs[2], 'diemmon2':hs[3], 'diemmon3':hs[4]}
            lstHS.append(hs)
    return lstHS