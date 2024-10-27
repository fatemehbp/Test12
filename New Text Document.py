class CustomStr:
    def init(self, string):
        self.string = string

    def custom_split(self, *separators):
        parts = [self.string]
        for sep in separators:
            temp = []
            for part in parts:
                temp.extend(part.split(sep))
            parts = temp
        return [p for p in parts if p]

    def remove_duplicate(self):
        seen = set()
        result = []
        for char in self.string:
            if char not in seen:
                seen.add(char)
                result.append(char)
        self.string = ''.join(result)

    def set_char(self, index, new_char):
        if not (0 <= index < len(self.string)):
            raise IndexError("Index is out of bounds")
        self.string = self.string[:index] + new_char + self.string[index + 1:]

    def isfloat(self):
        dot_seen = False
        for idx, char in enumerate(self.string):
            if char == '.':
                if dot_seen or idx == 0 or idx == len(self.string) - 1:
                    return False
                dot_seen = True
            elif not char.isdigit():
                return False
        return dot_seen

    def ispalindrome(self):
        left, right = 0, len(self.string) - 1
        while left < right:
            if self.string[left] != self.string[right]:
                return False
            left += 1
            right -= 1
        return True

    def str(self):
        return self.string

    def repr(self):
        return f"CustomStr('{self.string}')"

# مثال‌ها
a = CustomStr('kamand kargar')
print(a.custom_split(" ", 'a', 'k'))  # ['m', 'nd', 'rg', 'r']

b = CustomStr('kamand')
b.remove_duplicate()
print(b)  # 'kamnd'

c = CustomStr('kamand kargar')
c.set_char(0, 'n')
print(c)  # 'namand kargar'

d = CustomStr('1.2')
print(d.isfloat())  # True

e = CustomStr('racecar')
print(e.ispalindrome())  # True

f = CustomStr('python')
print(f.ispalindrome())  # False