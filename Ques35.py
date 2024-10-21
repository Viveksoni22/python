class ReverseString:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

rs = ReverseString()
print(rs.reverse_words('hello .py'))