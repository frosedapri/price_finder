with open(r"C:\Users\owen\Desktop\Projet Python\website\read_it.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
print(content)