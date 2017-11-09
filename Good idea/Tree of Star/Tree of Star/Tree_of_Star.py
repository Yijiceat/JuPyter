#網路看到的解法
def tree(num):
    for i in range(num):
        print(' '*(num-i-1)+'*'*(i*2+1))

tree(int(input('請輸入Tree Of Star 的層數 : ')))


#自己練習的解法
#def tree(num):
#    for i in range(num):
#       print(' '*(num-i-1)+'*'*(i*2+1))