# W1D3 Wednesday Palindrome - NORMAL

import re


def main():
    print("\nPlease enter something:  ",end='')
    entry = input().lower()
    print(entry)


    if entry > "":
        if prep(entry):
            print("you a P")
        else:
            print("ain't")


# def is_palindrome(fr_half_list, bk_half_list, is_a_pal):
#     x = 0
#     for each in fr_half_list:
#         theletter = bk_half_list[x]
#         #print(theletter)
#         if each != theletter:
#             is_a_pal = False
#             #print("########## false ##########")
#             return is_a_pal
#         else:
#             x += 1
#     is_a_pal = True
#     return is_a_pal


def is_palindrome(fr_half_list, bk_half_list, is_a_pal, pal_len):
    if pal_len < 0:
        return
    if fr_half_list[pal_len - 1] != bk_half_list[pal_len - 1]:
        is_a_pal = False
        return is_a_pal
    is_palindrome(fr_half_list, bk_half_list, is_a_pal, pal_len - 1)
    is_a_pal = True
    return is_a_pal


def prep(entry):
    entry_stripped = entry.replace(' ','')
    entry_stripped = re.sub('[^a-z0-9]','',entry_stripped)
    p_len = len(entry_stripped)

    if p_len == 1:
        is_a_pal = True             # 1-Letter Palindrome
        return is_a_pal

    middle = int(p_len / 2)
    #print(entry_stripped)
    each_letter = list(entry_stripped)

    front_half = entry_stripped[:middle]

    if p_len%2 == 0:
        back_half = entry_stripped[middle:]
    else:
        print(middle)
        back_half = entry_stripped[middle+1:]

    fr_half_list = list(front_half)
    back_half = back_half[::-1]     #easy way
    bk_half_list = list(back_half)
    print(fr_half_list,bk_half_list,"******")

    is_a_pal = False
    pal_len = middle
    is_a_pal = is_palindrome(fr_half_list, bk_half_list, is_a_pal,pal_len)
    print(is_a_pal)
    return is_a_pal


    # if front_half == back_half:     #easy way
    #     is_a_pal = True             #easy way
    # else:                           #easy way
    #     is_a_pal = False            #easy way


    #print(front_half)
    #print(back_half)



    #good_chars = list(range(chr(97),chr(122)))

#    good_chars = list('abcdefghijklmnopqrstuvwxyz')
#    print(good_chars)

#    entry.strip(' ')
   # print(each_letter)
   # for each in each_letter:
   #     if each not in good_chars:
   #         print(each)

main()
