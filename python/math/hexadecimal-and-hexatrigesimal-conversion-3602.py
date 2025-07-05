class Solution:
    def concatHex36(self, n: int) -> str:
        hex_val = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        trig_val = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"
        }
        squared = n * n

        def convert(n, hex_val, base):
            hex_place = 0
            for i in range(0, 10):
                if pow(base, i) > n:
                    hex_place = i-1
                    break
            hex_num = ""
            for i in range(hex_place, -1, -1):
                curr_val = n // (pow(base, i))
                n -= curr_val * pow(base, i)
                if curr_val in hex_val:
                    hex_num += hex_val[curr_val]
                else:
                    hex_num += str(curr_val)
            return hex_num

        return convert(squared, hex_val, 16) + convert(pow(n, 3), trig_val, 36)

        
# Better solution
class Solution:
    def concatHex36(self, n: int) -> str:
        # Square and cube of n
        n2 = n * n
        n3 = n * n * n
    
        # Convert to hexadecimal (base 16), uppercase
        hex_part = format(n2, 'X')
    
        # Convert to hexatrigesimal (base 36), uppercase
        base36_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        base36_part = ''
        
        num = n3
        while num > 0:
            base36_part = base36_chars[num % 36] + base36_part
            num //= 36
    
        return hex_part + base36_part