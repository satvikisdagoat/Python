ori_num = int(input("Enter a number:"))
vidya_num = ori_num
rev_num = 0
while ori_num != 0:
    digit = ori_num % 10
    rev_num = rev_num * 10 + digit
    ori_num //=10

print("the rev number is:", rev_num)   

if rev_num == vidya_num:
    print("the number is palindrome")
else:
    print("the number is not a palindrome")   
