print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
class Nguoi(object):
    
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
   
    def getGender(self):
        return "Nữ"

aNam = Nam()
aNu = Nu()

print(aNam.getGender())  
print(aNu.getGender())   
