def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

def init(data):
    labels = 'first', 'middle', 'last'
    for label in labels:
        data[label] = {}

MyNames={}
init(MyNames)
store(MyNames, 'wang hao')
store(MyNames, 'wang qiang')
store(MyNames, 'zhang bao')
print lookup(MyNames, 'first', 'zhang')


# def hello(parameter_list):
    # 'this is a hello'
    # print parameter_list
# print hello.__doc__
# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'arnold', 'bob']

# print [(g,b) for g in girls for b in boys if g[0] == b[0]]
# tmpObj={}
# tmpObj.pop
# [tmpObj.setdefault(b[0], []).append(b) for b in boys]
# print [(g,''.join(tmpObj[g[0]])) for g in girls if g[0] in tmpObj]

# print [x*x for x in range(10) if not x%3 ]
# print [(x,y) for x in range(3) for y in range(3)]

# a=[1,2,3,4]


# b=['a', 'b', 'c','d']

# for x,y in zip(a, b):
#     print x, y

# for index, string in enumerate(b):
#     print index, string