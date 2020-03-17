# stack
elem_list = []
def top(elem):
    elem_list.append(elem)

def read(elem):
    return elem_list[-1]

def size():
    return len(elem_list)

def pop():
    if size():
        return elem_list.pop()