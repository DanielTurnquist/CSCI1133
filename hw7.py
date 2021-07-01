def encrypt(message, encoding):
# ==========================================
# Purpose: encodes a message using an arbitrary Baconian cipher and returns it
# Input Parameter(s): -message: the message to be encoded (string)
#                     -encoding: the series of groups of 5 characters representing the cipher (no divison of character groupings) (string)
# Return Value(s): the message, encoded according to the specified encoding (string)
# ==========================================
    low_case_message = message.lower()
    alpha_message = ''
    for char in low_case_message:
        if char.isalpha():
            alpha_message += char
    encoding_list = []
    for i in range(130)[4::5]:
        encoding_list += [encoding[i - 4 : i + 1]]
    unicode_message = []
    for char in alpha_message:
        unicode_message += [ord(char)]
    encoded_message = ''
    for num in unicode_message:
        encoded_message += encoding_list[num - ord('a')]
    return encoded_message

def decrypt(message, encoding):
# ==========================================
# Purpose: decodes a message using an arbitrary Baconian cipher and returns it
# Input Parameter(s): -message: the message to be decoded (string)
#                     -encoding: the series of groups of 5 characters representing the cipher (no divison of character groupings) (string)
# Return Value(s): the message, decoded according to the specified encoding (string)
# ==========================================
    encoding_list = []
    for i in range(130)[4::5]:
        encoding_list += [encoding[i - 4: i + 1]]
    message_list = []
    for i in range(len(message))[4::5]:
        message_list += [message[i - 4: i + 1]]
    decoded_message = ''
    for i in range(len(message_list)):
        for j in range(len(encoding_list)):
            if message_list[i] == encoding_list[j]:
                decoded_message += chr(ord('a') + j)
    return decoded_message

def longest_common(first, second):
# ==========================================
# Purpose: finds the longest common sequence in two strands of DNA and returns it
# Input Parameter(s): -first: the first DNA sequence (string)
#                     -second: the second DNA sequence (string)
# Return Value(s): the longest common sequence (string)
# ==========================================
    first_list = []
    for i in range(len(first)):
        for j in range(len(first)):
            sub = first[i:j+1]
            if sub not in first_list:
                first_list += [sub]
    top_len = 0
    long_com = ''
    for seq in first_list:
        if seq in second and len(seq) > top_len:
            long_com = seq
            top_len = len(seq)
    return long_com

def helper_vowel_index(word):
# ==========================================
# Purpose: finds the index of the first vowel of a word and returns it (or zero if there are no vowels)
# Input Parameter(s): -word: the word to be inspected (string)
# Return Value(s): either 0 or the index of the first vowel (integer)
# ==========================================
    for i, ch in enumerate(word):
        if ch in 'aeiou':
            return i
    return 0

def helper_word_translator(word):
# ==========================================
# Purpose: translates and returns a word according to the rules of Pig Latin
# Input Parameter(s): -word: word to be translated (string)
# Return Value(s): the word translated into Pig Latin (string)
# ==========================================
    vowels = False
    for ch in word:
        if ch in 'aeiou':
            vowels = True
    vowel = helper_vowel_index(word)
    translation = ''
    for ch in word[vowel::]:
        translation += ch
    for ch in word[:vowel:]:
        translation += ch
    if vowel == 0 and vowels:
        return translation + 'way'
    else:
        return translation + 'ay'

def helper_punc_caps(word):
# ==========================================
# Purpose: temporarily removes capitalization and punctuation from a word to make translation easier, and translates the word
# Input Parameter(s): -word: the word to be acted upon (string)
# Return Value(s): the translated word with punctuation and capitalization (string)
# ==========================================
    upper = False
    punc = ''
    for i,ch in enumerate(word):
        if ch.isupper():
            upper = True
        if ch in ',.?!':
            punc = ch
    low_nopunc = ''
    for ch in word:
        if ch.isalpha():
            low_nopunc += ch.lower()
    low_nopunc_trans = helper_word_translator(low_nopunc)
    if upper:
        return low_nopunc_trans[0].upper() + low_nopunc_trans[1::] + punc
    else:
        return low_nopunc_trans + punc

def igpay(phrase):
# ==========================================
# Purpose: translates a phrase into Pig Latin and returns it
# Input Parameter(s): -phrase: a phrase with letters and punctuation (string)
# Return Value(s): the phrase translated into Pig Latin (string)
# ==========================================
    orig_list = phrase.split()
    translated_list = []
    for word in orig_list:
        translated_list += [helper_punc_caps(word)]
    return ' '.join(translated_list)













