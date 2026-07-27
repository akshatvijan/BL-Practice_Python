def remove_digit(text):
    ans=""
    for ch in text:
        if not ch.isdigit():
            ans=ans+ch
    print(ans)

text=input("Enter a string")
remove_digit(text)