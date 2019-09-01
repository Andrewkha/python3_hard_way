class Test:

    ls = []

    def change_ls(self, num):
        self.ls.append(num)


a = Test()
a.change_ls(10)

print(a.ls)

b = Test()

print(b.ls)

phrase = 'Hello this is the phrase'
print(phrase[:])