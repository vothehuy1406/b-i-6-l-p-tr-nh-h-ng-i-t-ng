print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
class StringManipulator:
    def __init__(self):
        self.user_string = ""  

    def get_String(self):
        self.user_string = input("Nhập một chuỗi: ")  

    def print_String(self):
        print(self.user_string.upper())  

string_manipulator = StringManipulator()

string_manipulator.get_String()

string_manipulator.print_String()
