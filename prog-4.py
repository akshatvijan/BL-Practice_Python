def str_count(str):
    digit=sum(1 for ch in str if ch.isdigit())
    char=sum(1 for ch in str if ch.isalpha())
    spc=len(str)-digit-char
    return digit,char,spc
   
def main():
    str=input("Enter a string")
    digit,char,spc=str_count(str)
    print("Number of digit is ",digit)
    print("Number of char is ",char)
    print("Number of digit is ",spc)

if (__name__=="__main__"):
    main()