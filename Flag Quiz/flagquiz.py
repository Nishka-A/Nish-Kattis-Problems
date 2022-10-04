# Author: Nishka Awasthi
# It is ok to post my anonymized solution

raw_input() #to get rid of the first line
entries = int(raw_input()) #This is number of lines to be processed

if entries == 1:
    print(raw_input())

else:
    matrix = []
    og_strs = []
    for i in range(entries):
        og_strs.append(raw_input())
        line = og_strs[i].split(", ")
        matrix.append(line)

    # list that contains the number of differences
    compare_lst = [0] * entries
    differences = 0

    #start with first row
    for i in range(len(matrix)):
        # my main row is in matrix[i]
        for j in range(i + 1, len(matrix)):
            # my comparing row is in matrix[j]
            for k in range(len(matrix[0])):
                if matrix[i][k] != matrix[j][k]:
                    # they not same!
                    differences += 1
            if compare_lst[i] < differences:
                compare_lst[i] = differences
            if compare_lst[j] < differences:
                compare_lst[j] = differences
            differences = 0

    min_comp = min(compare_lst)

    # in case there is multiple right answers, print all
    # things with the least amount of "differences"
    for i in range(len(compare_lst)):
        if compare_lst[i] == min_comp:
            print(og_strs[i])
