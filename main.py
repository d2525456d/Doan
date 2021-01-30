import  folder_op, web_op


def start(url_goc, max_page):
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình
    url_list = [url_goc] #Chứa các đường link sẽ được duyệt
    url_list_const = 10000
    history = [] #Chứa các đường link đã duyệt
    max_page = n #Quy định số lượng trang web được tải về
    count = 0 #Đếm số lượng trang web đã tải về
    folder_op.tao_thu_muc("C:\\")
    data_folder = 'C:\\Crawler'

    #kịch bản các trang web
    while (count < max_page) and (len(url_list) > 0):
        url_new = []
        url_new_const = 500
        url = url_list.pop(0)
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links:
            if web_op.kiem_tra_link(item) == False:
                    item = web_op.chinh_sua_link(url, item)
            if (item not in url_list) and (item not in history) and (item not in url_new) and (item != url):
                if len(url_new)>=url_new_const:
                    continue
                else:
                        url_new.append(item)
        if len(url_list) + len(url_new) <= url_list_const:
            url_list = url_list + url_new
        else:
            check = int(url_list_const - len(url_list))
            array =url_new[:check]
            url_list = url_list + array

        history.append(url)
        count += 1

        data_array = [page, url_new, url, url_new_const]
        name_folder = folder_op.tao_ten_folder_tu_dong(data_folder, url)
        folder_op.luu_file(data_array, name_folder)
        print("Đã cào " + str(count) + " url")

    print("-"*50+"\n Dữ liệu đã cào được lưu tại thư mục: C:\\Crawler\n"+"-"*50)


if __name__ == '__main__':
    url_goc = str(input("Nhập đường dẫn mà bạn muốn cào dữ liệu: "))
    n = int(input("Nhập số lượng url mà bạn muốn cào: "))
    start(url_goc, n)