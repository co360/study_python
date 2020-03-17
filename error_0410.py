try:
    a=[]
    print a[1]
except ZeroDivisionError as identifier:
    print "zero", identifier
except Exception as e:
    print e
finally:
    print "Done"
print 'hello'