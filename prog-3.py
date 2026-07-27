def str_count(str):
    digit=0
    char=0
    spc=0
    for ch in str:
        if ch.isdigit():
            digit=digit+1
        elif ch.isalpha():
            char=char+1
        else:
            spc=spc+1
    return digit,char,spc
def main():
    str=input("Enter a string")
    digit,char,spc=str_count(str)
    print("Number of digit is ",digit)
    print("Number of char is ",char)
    print("Number of digit is ",spc)

if (__name__=="__main__"):
    main()