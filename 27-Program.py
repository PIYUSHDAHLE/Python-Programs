#set concept
s={1,2,3}
print(s)
s.add(4)
s.add(3) # set not repet the same value
print(s)
s.add(4.5)
s.add(4.1)
s.add(4.0) # int 4 = float 4.0 so its not print
s.add("3")
print(s)
#s.add([1,2,3]) #add list in set = error
s.add((1,)) #add tuple no error
print(s)