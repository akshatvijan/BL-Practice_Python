#regEx Intro
import re
# Regex	Meaning	Equivalent
# \d	Digit	[0-9]
# \D	Non-Digit	[^0-9]
# \s	Whitespace	[ \t\n\r\f\v]
# \S	Non-Whitespace	[^ \t\n\r\f\v]
# \w	Word Character	[a-zA-Z0-9_]
# \W	Non-Word Character	[^a-zA-Z0-9_]

# | Function     | Searches                 | Returns                     | Use Case                              |
# | ------------ | ------------------------ | --------------------------- | ------------------------------------- |
# | `match()`    | Beginning of string only | Match object / `None`       | Check if string starts with a pattern |
# | `search()`   | Entire string            | First Match object / `None` | Find first occurrence                 |
# | `findall()`  | Entire string            | List of all matches         | Get all matched values                |
# | `finditer()` | Entire string            | Iterator of Match objects   | Get matches with index/position       |

# | Method    | Returns                  | Example Output |
# | --------- | ------------------------ | -------------- |
# | `group()` | Matched string           | `"cat"`        |
# | `start()` | Starting index           | `0`            |
# | `end()`   | Ending index (exclusive) | `3`            |
# | `span()`  | `(start, end)` tuple     | `(0, 3)`       |

# str='i,am,studing,python'
# list=str.split(",")
# print(list)

# import re
# quote = "I scream, you scream, we all scream for ice cream."

# #search
# ans1=re.search('scream',quote).group()
# ans2=re.search('scream',quote).end()
# ans3=re.search('scream',quote).start()
# ans4=re.search('scream',quote).span()

# print(ans1)
# print(ans2)
# print(ans3)
# print(ans4)
# all_occurence=re.findall('scream',quote)
# print(all_occurence)
# split_occ=re.split('you',quote)
# print(split_occ)

# #digits
# value='I have 2 apples and 5 oranges and 24 banana'
# matches=re.findall(r'\d',value)
# print(matches)

# text='the year is 2024'
# matches=re.findall(r'\d{2}',text)
# print(matches)

#non digits
# text1="123 main st. francis 123 hello"
# matches=re.findall(r'\D+',text1)
# print(matches)
# text1="123 main st. francis 123 hello"
# matches=re.findall(r'\D{3}',text1)
# print(matches)


# #\s 
# text2="hello world  "
# matches=re.findall(r'\s{2}',text2)
# print(matches)

# #\S
# text2="hello world  "
# matches=re.findall(r'\S+',text2)
# print(matches)

#\w
text="zbc123_ 123"
matches=re.findall(r'\w+',text)
print(matches)


text="zbc1 23_ , 123"
matches=re.findall(r'\W+',text)
print(matches)

