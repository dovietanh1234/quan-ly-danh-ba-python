contacts = []

def display_menu():
    """Hiển thị menu chính"""
    print("\n=== QUẢN LÝ DANH BẠ LIÊN HỆ ===")
    print("1. Thêm liên hệ mới")
    print("2. Xem toàn bộ danh bạ")
    print("3. Tìm kiếm liên hệ")
    print("4. Xóa liên hệ")
    print("5. Thoát chương trình")
    print("===============================")
    choice = input("Chọn chức năng (1-5): ")
    return choice

def add_contact():
    """Thêm liên hệ mới"""
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")
    email = input("Nhập email: ")
    new_contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(new_contact)
    print("Liên hệ đã được thêm thành công!")

def view_contacts():
    """Xem toàn bộ danh bạ với định dạng bảng"""
    if not contacts:
        print("Danh bạ trống!")
        return

    print("\n=== DANH BẠ LIÊN HỆ ===")
    print("{:<5} {:<20} {:<15} {:<30}".format("STT", "Tên", "Số điện thoại", "Email"))
    print("-" * 70)
    for i, contact in enumerate(contacts, start=1):
        print("{:<5} {:<20} {:<15} {:<30}".format(i, contact['name'], contact['phone'], contact['email']))
    print("=======================")

def search_contact():
    """Tìm kiếm liên hệ dựa trên từ khóa (tương đồng với tên hoặc số điện thoại)"""
    keyword = input("Nhập từ khóa tìm kiếm (tên hoặc số điện thoại): ").lower()
    found = False
    print("\n=== KẾT QUẢ TÌM KIẾM ===")
    print("{:<5} {:<20} {:<15} {:<30}".format("STT", "Tên", "Số điện thoại", "Email"))
    print("-" * 70)
    for i, contact in enumerate(contacts, start=1):
        if keyword in contact['name'].lower() or keyword in contact['phone'].lower():
            print("{:<5} {:<20} {:<15} {:<30}".format(i, contact['name'], contact['phone'], contact['email']))
            found = True
    if not found:
        print("Không tìm thấy liên hệ nào khớp!")
    print("=======================")

def delete_contact():
    """Xóa liên hệ dựa trên tên"""
    name_to_delete = input("Nhập tên liên hệ cần xóa: ").lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name_to_delete:
            del contacts[i]
            print("Liên hệ đã được xóa!")
            return
    print("Không tìm thấy liên hệ với tên này!")

def main():
    """Chức năng chính: Chạy menu và gọi các hàm"""
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

# Chạy chương trình
if __name__ == "__main__":
    main()