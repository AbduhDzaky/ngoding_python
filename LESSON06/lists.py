users = ['Dzaky', 'Aping', 'Nada']

data = ['Dzaky', 20, True]

emptylist = []

print("Dzaky" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Nada')) # untuk mengetahui ada di index berapa

print(users[0:2]) # untuk melihat list dari index yang dipilih
print(users[1:]) # untuk melihat list dari index yang dipilih
print(users[-3:-1]) # untuk melihat list dari index yang dipilih

print(len(data)) # mengetahui ada berapa data dalam list

users.append("Elsa") #menambahkan kedalam list
print(users)

users += ['Jason'] # cara lain untuk menambahkan kedalam list
print(users)

users.extend(['Robert', 'Jimmy']) # cara lain untuk menambahkan kedalam list
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ['Edie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob') # untuk menghapus data yang ada dalam list
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data # ini akan menghapus dari list data dan akan memunculkan error
data.clear() # akan menghapus tapi tidak memunculkan error
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower) # untuk mengurutkan berdasarkan alfaber tetapi mengutamakan yang kapital terlebih dahulu
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse() # untuk mengurutkan dari list paling akhir jadi istilahnya di balik
print(nums)

nums.sort(reverse=True) # mengurutkan dari angka yang terbesar, kalau di ganti False jadinya dari yang terkecil
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

