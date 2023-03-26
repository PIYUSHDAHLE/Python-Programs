# #Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    li=[]
    N = int(input())
    for i in range(N):
        com, *line = input().split()
        comm = list(map(int, line))
        if com=="insert":
            li.insert(comm[0],comm[1])
        elif com=='remove':
            li.remove(comm[0])
        elif com=='append':
            li.append(comm[0])
        elif com=='sort':
            li.sort()
        elif com=='pop':
            li.pop()
        elif com=='reverse':
            li.reverse()
        elif com=='print':
            print(li)
    i += 1