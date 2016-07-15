# W1D3 Wednesday Palindrome - NORMAL

def main():
    print("\n"*50)
    print("\nPlease enter something:  ",end='')
    entry = input().lower()

    if entry > "":
        if is_palindrome(entry):
            print("\n********************\nThis is a Palindrome\n********************\n")
        else:
            print("\n********************\nSorry, no Palindrome\n********************\n")


def is_palindrome(entry):
    entry_stripped = entry.replace(' ','')
    p_len = len(entry_stripped)
    middle = int(p_len / 2)
    each_letter = list(entry_stripped)

    front_half = entry_stripped[:middle]

    if p_len%2 == 0:
        back_half = entry_stripped[middle:]
    else:
        back_half = entry_stripped[middle+1:]



    #back_half = back_half[::-1]        --------------
    #bk_half_list = list(back_half)     SUPER EASY WAY

    #if front_half == back_half:               |
    #    is_a_pal = True
    #else:                                     |
    #    is_a_pal = False               ______________


    fr_half_list = list(front_half)
    back_half = back_half[::-1]
    bk_half_list = list(back_half)

    x = 0
    for each in fr_half_list:
        theletter = bk_half_list[x]
        if each != theletter:
            is_a_pal = False
            return is_a_pal
        else:
            x += 1
    is_a_pal = True
    return is_a_pal


if __name__ == __main__
main()
