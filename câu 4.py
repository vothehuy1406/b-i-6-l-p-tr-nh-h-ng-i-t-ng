print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
class RomanToInt:
    
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def __init__(self, roman):
        self.roman = roman

    def convert(self):
        total = 0
        prev_value = 0

        for char in reversed(self.roman):
            current_value = self.roman_map[char]
            
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

roman_numeral = "XLII"
converter = RomanToInt(roman_numeral)
print(f"Số La Mã {roman_numeral} chuyển thành số nguyên là: {converter.convert()
