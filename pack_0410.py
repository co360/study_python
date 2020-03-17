from util_test import random_id

def getID():
    d1 = random_id.getId()
    d2 = random_id.getId()
    d3 = random_id.getId()
    print d1,d2,d3

if __name__ == "__main__":
    getID()