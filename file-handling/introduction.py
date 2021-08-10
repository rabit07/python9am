# handle =open ('record.txt', 'w')
# handle.write('we are learning file-handling...')
# handle.close()

# fs=open('record.txt','r')
#
# print(fs.readline())
# print(fs.readlines())
# print(fs.read())

file = open('record.txt', 'a')
num = int(input("Enter username:"))

file.write(f"{num}")
file.write('\n')

file.close()
