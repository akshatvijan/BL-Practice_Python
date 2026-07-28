import re
def check_news(news):
    check_modi=re.search('Modi',news)
    print(f"Presense of 'Modi' {True if (check_modi) else False}")
    total_word=re.findall(r'\b\w+\b',news)
    print(f"Total word length is: {len(total_word)}")
    the_occ=re.findall('the',news)
    print(f"Occurence of word the: {len(the_occ)}")
    check_digit=re.search(r'\d',news)
    print(f"Occurence of digit: {True if check_digit else False}")
    without_article = re.sub(r'\b(a|an|the)\b', '', news, flags=re.IGNORECASE)
    print(without_article)
    without_vowel=re.sub(r'a|e|i|o|u','',news,flags=re.IGNORECASE)
    print(without_vowel)
news_paragraph = "Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi. Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X. “These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,” he posted on X, in a clear indication that govt intends to initiate action. Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed “experts”, as per the X post."
check_news(news_paragraph)