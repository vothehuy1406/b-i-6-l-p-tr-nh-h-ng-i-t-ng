print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
class Circle(object):

    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius ** 4 * 3.14

aCircle = Circle(2)

print(aCircle.area())
