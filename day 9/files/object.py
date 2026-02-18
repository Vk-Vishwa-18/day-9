#file = open("test.txt", "w")
#file.write("hello vk\n")
#file.write("python")
#file.close()

#file = open("test.txt", "a")
#file.write("\nhello vk")
#file.close()

with open ("test.txt", "r") as file:
    data = file.read()
    print(data)
    