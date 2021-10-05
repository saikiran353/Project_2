import re
import time

# pattern = '(\d{3})-(\d{3}-\d{4})'
# mob = re.compile(pattern)
# result =mob.search('saikiran 832-808-4302 saikiran999@gmail.com')
# print(result.group(2))

# hero = re.compile(r'sai|kiran|murali')
# result = hero.search('there was a hero with name murali')
# print(result.group())

# mat = re.compile(r'(sai){1,2}')
# result = mat.search('saisaisaisai is a saisai')
# print(result.group())

# opt = re.compile(r'bat(wo)?man')
# result = opt.search('advanture of batwoman')
# print(result.group())

# opt2 = re.compile(r'bat(wo)*man')  # match 0 or more
# result = opt2.search('kian is batwowowowoman')
# print(result.group())

# opt2 = re.compile(r'bat(wo)+man')  # match 0 or more
# result = opt2.search('kian is batwowowowoman')
# result2 = opt2.search('kiran is not batman') == None
# print(result2)
# print(result.group())
#
mt= re.compile(r'S')
# result = mt.match('Saikiran is a saikiran with Sai and kiran')
# print(result.group())
#
# mt2= re.compile(r'kiran')
# result5 = mt2.fullmatch('kiran  kiran')
# print(result5)
#
# result2 = mt.search('is a with Saikiran and Siran', 23, 24)
# print(result2.group())
#
# result3 = mt.findall('saikiran is a saikiran with sai and kiran')
# print(result3)

# pattern = re.compile(r'\b\w{8}\b')
# result = pattern.findall('saikiran has a kiransai which is saikiran')
# print(result)
#
# result2 = pattern.finditer('saikiran has a kiransai which is saikiran')
# print(result2)
# for match in result2:
#     print(match.group())

# sb = re.compile('sai')
# result = sb.sub('~*', 'saikiran has saikiran')
# print(re.sub('sai', '~*', 'Saikiran', flags=re.IGNORECASE))
# print(result)
# print(re.sub('sai', '~*', 'saikiran has saikiran',count=1, flags=re.IGNORECASE))
# print(re.sub(r'\sand\s', '&', 'saikiran and saikiran'))
#
# print(re.subn('sai', '~*', 'saikiran has saikiran musaihfbu jdggysaidhb'))
# print(re.escape('saikiran has saikiran which may has the kiran aswell but need to add sai'))

# mt = re.compile('(?P<username>\w+)@(?P<git>\w+).(?P<role>\w+)')
# res = mt.search('sai@saikiran353.python_dev')
# print(res.groupdict())





 # res = (re.match('(?P<username>\w+)@(?P<mail>\w+).(?P<origin>\w+)', 'saikiran353@gmail.com'))
 # print(res.groupdict())

# with open('make.csv', 'w')as file:
#     file.write('saikiran999@gmail.com\n')
#     file.write('muralimohan33@gmail.in\n')

# with open('make.csv', 'r') as file:
#     lines = file.readlines()
#     print(lines)
#     for obj in lines:
#         res = (re.match('(?P<username>\w+)@(?P<mail>\w+).(?P<origin>\w+)', obj))
#         print(res.start())
#         print(res.groupdict())
#         print(res.end())
#         print(res.span())

import re

password = "Sa2@yg"
len(password)
flag = 0
while True:
    if len(password) >= 6 and len(password) <= 12:
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password):
                if re.search("[0-9]", password):
                    if re.search("[_@$]", password):
                        print('valid')
                        break
    else:
        print('not valid')
        break

def isValidURL(str):

    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,200}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)
    if (str == None):
        return False
    if (re.search(p, str)):
        return True
    else:
        return False

url = "https://www.google.com"

if (isValidURL(url) == True):
    print("Yes")
else:
    print("No")

def removeDuplicateWords(input):
    regex = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)

print(removeDuplicateWords('sai saikiran sai kiran'))

regex = r'\b[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

check('sriramulasaikiran22@gmail.com')
def matching(string):
    pattern = re.compile('Mr.|Ms.|Dr.|Er.')
    res = re.search(pattern, string)
    return res.group()
print(matching('Mr.saikiran'))

