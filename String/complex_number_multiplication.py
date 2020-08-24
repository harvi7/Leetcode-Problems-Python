class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def decode(s):
            temp_str = s.split('+')
            return int(temp_str[0]), int(temp_str[1].replace('i', ''))
        a_real, a_img = decode(a)
        b_real, b_img = decode(b) 
        return str(a_real * b_real - a_img * b_img) + '+' + str(a_real * b_img + a_img * b_real) + 'i'