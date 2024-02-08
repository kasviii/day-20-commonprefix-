def longest_common_prefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

# Taking user input
input_strings = input("Enter strings separated by spaces: ").split()

# Calling the function and printing the result
print("Longest common prefix:", longest_common_prefix(input_strings))
