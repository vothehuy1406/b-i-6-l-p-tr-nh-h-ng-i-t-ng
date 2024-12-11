print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
class HinhChunhat(object):
    
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def area(self):
        return self.dai * self.rong

hinhChunhat = HinhChunhat(7, 4)

print(hinhChunhat.area())
