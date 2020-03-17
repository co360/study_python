stu_list = []
while True:
    cmd = raw_input('add,search,cal,exit\n')
    if cmd == 'exit':
        break
    elif cmd == 'add':
        stu_str = raw_input("alice,chinese,match\n")
        stu_info = stu_str.strip().split(',')
        if len(stu_info) != 3:
            print "format error"
            continue
        stu_name = stu_info[0]
        chinese_score = float(stu_info[1])
        match_score = float(stu_info[2])
        stu_list.append([stu_name,chinese_score,match_score])
        print stu_list
    elif cmd == 'search':
        stu_name = raw_input("alice\n")
        for i in range(len(stu_list)):
            if stu_name == stu_list[i][0]:
                print stu_list[i]
    elif cmd == 'cal':
        chinese_sum = 0
        match_sum = 0
        stu_count = len(stu_list)
        for i in range(stu_count):
            chinese_sum += stu_list[i][1]
            match_sum += stu_list[i][2]
        print chinese_sum/stu_count, match_sum/stu_count
    else:
        print 'cmd not realise'