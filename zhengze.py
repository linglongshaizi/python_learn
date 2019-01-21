import re

#match 和 search 的使用
source = 'Young Frankenstein'
m = re.match('You',source)
if m:
    print(m.group())

n = re.match('Frank',source)

if n:
    print(n.group())  #match 只能检测以模式串座位开头的源字符串

p = re.search('Frank',source)

if p:
    print('this is search result:',p.group())   #使用search可以匹配任何位置   this is search result: Frank

q = re.match('.*Frank',source)

if q:
    print(q.group())    #使用.*匹配，.代表任意单一字符(一个字符)，*代表任意一个它之前的字符，.*代表任意多个字符；Young Frank
#findall的使用

mm = re.findall('n',source)
print(mm,len(mm))   #findall 找出字串中所有的n，返回一个列表，使用len()查看列表长度；['n', 'n', 'n', 'n'] 4

nn = re.findall('n.',source)
print(nn)   #使用.找出所有n+后面一个字符；['ng', 'nk', 'ns']，最后一个n没有被匹配，使用？说明n后面的字符可选

qq = re.findall('n.?',source)
print(qq)   #使用？说明n后面的字符可选  ['ng', 'nk', 'ns', 'n']

source_two = 'apple Fank'

qq = re.findall('.?a',source_two)

print(qq)  #同理 如果想找前面一个字符则使用'.?'

#split()使用

m = re.split('n',source)
print(m)    #使用split进行分割，Young Frankenstein 被分割['You', 'g Fra', 'ke', 'stei', '']组成的列表

#sub()使用

m = re.sub('a','?',source)
print(m)    #吧字串中的所有a都替换成？，返回字符串 Young Fr?nkenstein

import string
printable = string.printable
print(len(printable))
print('前50个:',printable[0:50],'后50个:',printable[50:])
print('所有的数字是：',re.findall('\d',printable),'所有的数字和字母是：',re.findall('\w',printable))     #\d 匹配数字字符，\w匹配字母或者数字字符
