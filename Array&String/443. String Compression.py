# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75


# chars = ["a","a","b","b","c","c","c"]
# out = []
# i = 0

# while i <= len(chars)-1: 
#     out.append(chars[i])

#     count = 1
#     while i+1 <= len(chars)-1 and chars[i] == chars[i+1]:
#         count += 1
#         i += 1
    
#     if count >= 10: 
#         for digit in str(count):
#             out.append(digit)
#     elif count != 1:
#         out.append(str(count))
    
#     i += 1

# chars = out

# print(chars)
# print(out)
#return len(out)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
i = 0

while i <= len(chars) - 1:
    count = 1
    j = 1

    while i+j <= len(chars) - 1 and chars[i] == chars[i+j]:
        count += 1
        j += 1

    if count == 1: 
        i += 1
    elif count < 10:
        chars[i+1] = str(count)
        del chars[i+2:i+j]
        i += 2
    else: # More or equal to 10
        dts = list(str(count))
        print(chars)
        print(dts)
        chars[i+1:i+len(dts)] = dts
        del chars[i+len(dts)+1:i+j+1]
        i += len(dts) + 1

print(chars)