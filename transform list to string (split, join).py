# print("hello world!")
# transform list "[1,2,3]" to string "123"
nums = [1,2,3]
print('type(nums):',type(nums))

tmp = str(nums)
print(tmp)

tmp = tmp[1:-1]
print(tmp)

tmp = tmp.split(',')
print(tmp)

S = ''
tmp = S.join(tmp)
print(tmp)


