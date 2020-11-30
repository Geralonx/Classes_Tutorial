# For Loop um die Quadrate der Zahlen 0-9 zu erzeugen
for_loop_list = []
for i in range(10):
    for_loop_list.append(i*i)

# List-Comprehension um die Quadrahte der Zahlen 0-9 zu erzeugen.
list_comp_list = [i*i for i in range(10)]

print("For-Loop-Result:\t", for_loop_list)
print("List-Comp-Result:\t", list_comp_list)


# List Comprehension mit einer Bedingung, welche nur die geraden Zahlen erfasst.
new_list = [i*i for i in range(10) if i%2 == 0]
print(new_list)