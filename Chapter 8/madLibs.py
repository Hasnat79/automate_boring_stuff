import re
text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

def madlibs(text):
    fields=re.findall(r'ADJECTIVE|VERB|NOUN|ADVERB',text)
    for i in fields:
        reg = re.compile(r'{}'.format(i))
        inp=input("Enter %s %s:\n"%("an" if i[0] in 'AEIOU' else "a",i.lower()))
        text = reg.sub(inp,text,1)
    print(text)
madlibs(text)