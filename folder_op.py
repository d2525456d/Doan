#Các thư viện cần dùng
import os

#Các hàm cần thiết
#Hàm tạo thư mục mẹ để chứa thư mục con chứa các dữ liệu đã cào
def tao_thu_muc(path):
    os.chdir(path)
    check = os.listdir(path)
    if 'Crawler' not in check:
        os.mkdir('Crawler')
    path = 'C:\\Crawler\\'
    os.chdir(path)

#Hàm tạo tên folder tự động
def tao_ten_folder_tu_dong(path, url):
    os.chdir(path)
    count = len(os.listdir(path)) + 1
    name_folder = "Link_đã_cào_thứ_" + str(count)
    os.mkdir(name_folder)
    return name_folder

#hàm dùng để lưu file
def luu_file(data, name_folder):
    path = "C:\\Crawler\\"
    os.chdir(path + str(name_folder))
    content_1 = "Đây là file chứa code HTML vừa cào được"
    content_2 = "\n------------------------------------------\n\n"
    content_3 = str(data[0])
    list_tao_file_1 = [content_1, content_2, content_3]
    file = open("1 - File_HTML.txt", "w+", encoding="utf-8")
    for item in list_tao_file_1:
        file.write(item)
    file.close()
    line_url_1 = "Đây là những url khác được tìm thấy trong url này"
    line_url_2 = "\n------------------------------------------\n\n"
    line_url_3 = ""
    line_url_4 = data[1]
    max_url = data[3]
    if len(line_url_4) == max_url:
        line_url_3 = "Đã tìm thấy nhiều hơn " + str(max_url) + " url mới:\n"
    else:
        line_url_3 = "Đã tìm thấy " + str(len(line_url_4)) + " url mới:\n"
    list_tao_file_2 = [line_url_1, line_url_2, line_url_3]
    file = open("2 - Những url khác được tìm thấy.txt", "w+", encoding="utf-8")
    for item in list_tao_file_2:
        file.write(item)
    for item in range(len(line_url_4)):
        add_url = str(item + 1) + " - " + str(line_url_4[item]) + "\n"
        file.write(str(add_url))
    file.close()