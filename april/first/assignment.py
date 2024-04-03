# Ex. 1
a,b = 3, 4
a,b = b,a
print(a, b)
# Output is "4 3"

# Ex. 2
first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
second_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
third_list = [0, 1, 2, 3.5, 4.5, 5.5, "six", "seven", "eight", "nine"]


def sort_mixed_list(mixed_list, reverse=None):
    if not reverse:
        numeric_elements = [x for x in mixed_list if isinstance(x, (int, float))]
        numeric_elements.sort()
        non_numeric_elements = [x for x in mixed_list if not isinstance(x, (int, float))]
        non_numeric_elements.sort()
        sorted_list = numeric_elements + non_numeric_elements
        return sorted_list
    else:
        numeric_elements = [x for x in mixed_list if isinstance(x, (int, float))]
        numeric_elements.sort(reverse=True)
        non_numeric_elements = [x for x in mixed_list if not isinstance(x, (int, float))]
        non_numeric_elements.sort(reverse=True)
        sorted_list = numeric_elements + non_numeric_elements
        return sorted_list


first_list.sort()
print("First list sorted ascending: " + str(first_list))
first_list.sort(reverse=True)
print("First list sorted descending " + str(first_list))

second_list.sort()
print("Second list sorted ascending: " + str(second_list))
second_list.sort(reverse=True)
print("Second list sorted descending " + str(second_list))

third_list = sort_mixed_list(third_list)
print("Third list sorted ascending: " + str(third_list))
third_list = sort_mixed_list(third_list, reverse=True)
print("Third list sorted descending " + str(third_list))

first_list[5] = 6
second_list[5] = "f"
third_list[5] = 6.6

del first_list[2]
del second_list[2]
del third_list[2]

first_list[6] = "f"
second_list[6] = 6
third_list[6] = "g"

print(50*"=")

first_list = sort_mixed_list(first_list)
print("First list after changes sorted ascending: " + str(first_list))
first_list = sort_mixed_list(first_list, reverse=True)
print("First list after changes sorted descending " + str(first_list))

second_list = sort_mixed_list(second_list)
print("Second list after changes sorted ascending: " + str(second_list))
second_list = sort_mixed_list(second_list, reverse=True)
print("Second list after changes sorted descending " + str(second_list))

third_list = sort_mixed_list(third_list)
print("Third list after changes  sorted ascending: " + str(third_list))
third_list = sort_mixed_list(third_list, reverse=True)
print("Third list after changes  sorted descending " + str(third_list))