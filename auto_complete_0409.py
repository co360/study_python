query_log = ['alice', 'any', 'alias', 'bob',
             'bomb', 'bill', 'there', 'their', 'them']

dict = {}
for word in query_log:
    for i in range(1, len(word) + 1):
        key = word[0:i]
        if key not in dict:
            dict[key] = set([])
        dict[key].add(word)
print dict.keys()

while True:
    value = raw_input("\n")
    if value == 'exit':
        break
    else:
        if value in dict:
            print dict[value]
