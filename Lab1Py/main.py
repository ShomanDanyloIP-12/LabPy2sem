from func import*

print("Enter name of file: ")
name = new_var()
get_input(name)
print('Entered text:\n')
output(name)
lst = get_list(name)
name1, name2 = new_name_file2()
par_or_nep(lst, len(lst), name1, name2)
output2(name1, name2)
print("Enter the amount of sorted lines in ne: ")
k = new_var()
list_nep = get_list(name2)
sort(list_nep, int(k), name2)
output(name2)

