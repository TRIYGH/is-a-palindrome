# W1D3 Wednesday Palindrome - NORMAL

def main():
    print("\nPlease enter something:  ",end='')
    entry = input().lower()
    print(entry)


    if entry > "":
        if is_palindrome(entry):
            print("you a P")
        else:
            print("ain't")


def is_palindrome(entry):
    entry_stripped = entry.replace(' ','')
    p_len = len(entry_stripped)
    middle = int(p_len / 2)
    print(entry_stripped)                   #######
    each_letter = list(entry_stripped)

    front_half = entry_stripped[:middle]
#    print(p_len%2)
    if p_len%2 == 0:
        back_half = entry_stripped[middle:]
    else:
        print(middle)
        back_half = entry_stripped[middle+1:]

    #fr_half_list = list(front_half)
    back_half = back_half[::-1]
    #bk_half_list = list(back_half)
    #print(fr_half_list,bk_half_list,"******")

    if front_half == back_half:
        is_a_pal = True
    else:
        is_a_pal = False


    # x = 0
    # for each in fr_half_list:
    #     if each != bk_half_list[x]:
    #         is_a_pal = False
    #         break
    #     else:
    #         is_a_pal = True
    #
    return is_a_pal

    #print(front_half)
    #print(back_half)



    #good_chars = list(range(chr(97),chr(122)))

#    good_chars = list('abcdefghijklmnopqrstuvwxyz')
#    print(good_chars)

#    entry.strip(' ')
#    print(each_letter)
#    for each in each_letter:
#        if each not in good_chars:
#            print(each)

main()
