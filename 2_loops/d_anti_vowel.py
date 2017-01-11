def anti_vowel(text):
    s = ""
    i = 0
    while i < len(text):
      if not text[i] in "aeiouAEIOU":
        s += text[i]
      i += 1
    return s
