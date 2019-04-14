def edit_distance(str1, str2, i, j):   
    if str1[i-1] == str2[j-1]:
        return edit_distance(str1, str2, i-1, j-1)

    if i == 0:
        return j

    if j == 0:
        return i

    return 1 + min(edit_distance(str1, str2, i-1, j), edit_distance(str1, str2, i-1, j-1), edit_distance(str1, str2, i, j-1))
            

def main():
    str1 = 'abcdef'
    str2 = 'azced'
    print(edit_distance(str1, str2, len(str1), len(str2)))
    
main()
