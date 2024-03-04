 name1 = "bolaji"
 name3 = "chichi"
 name2 = "dayo"
 print(name1 == name2)
 print(name1 < name2)
 print(ord('B'))
 print("ci" in name3)
 print(f'[{name1:^10}]')


 print(f'{name1}  {name2}  {name3}')
 print(name1 * 5)

 name4 = "  solomon   "
 print(len(name4))
 print(len(name4.strip()))
 print(len(name4))
 print(name4)

 print(name2.capitalize())
 sentence = "welcome to semicolon africa"
 print(sentence.title())
 print(sentence.count("e"))
 print(sentence.rindex("e",5))

# collect alphabete alone#
 name = input("Enter your name: ").strip()
 if name.isalpha():
     print("VALID NAME")
 else:
     print("INVALID NAME")
 #collect name with number#
     name = input("Enter your name: ").strip()
     if name.isalnum():
         print("VALID NAME")
     else:
         print("INVALID NAME")

# #helps you checck what a method is doing#
 print(help(name1.isalnum()))
#dictonary comprention#v
sample = 'goggle.com'
print({k:sample.count(k)for k in sample})

