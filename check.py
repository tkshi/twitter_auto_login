# -*- coding: utf-8 -*-

import re
pattern = r"Twitter認証コードは([0-9]*)です"
text = "Twitter認証コードは400053です。 -- Sent using SMS-to-email. Reply to this email to tex..."
repatter = re.compile(pattern)
matchOB = repatter.findall(text)
print(matchOB[0])
if __name__ == '__main__':
    print('pypy')
