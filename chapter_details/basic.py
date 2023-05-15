# print("hello");
# a,b = 0,1;
# while (a<100):
#     print(a,end=",");
#     a,b = b,a+b;

# x = int(input("Enter a number : "));
# if (x<0):
#     x = 0;
#     print("The min number is zero");
# elif (x == 0):
#     print("the number is : ",x);
# elif (x == 1):
#     print("the number is : ",x);
# else:
#     print("the number is bigger than 1");

# words = ['cat', 'window', 'defenestrate'];
# for w in words:
#     print(w, len(w));

# list_a = [1, 2, 3, 4, 5];
# list_a.extend([6,7,8,9]);
# print(list_a);

# def calculate(self, s: str) -> int:
#     s.split();

# 简易计算器
# origin_string = "2+3*2 /5";
# deal_string = origin_string.replace(" ", "");
# split_string = [];
# index = 0;
# letter_numbers = [];
# letter_indexs = [];
# result_list = [];
# result = 0;
# for item in deal_string:
#     if item == "+" or item == "-" or item == "*" or item == "/":
#         letter_indexs.append(index);
#         letter_numbers.append(item);
#     split_string.append(item);
#     index += 1;
# print(split_string);
# print(letter_numbers);
# print(letter_indexs);
#
# for count in range(len(letter_indexs)):
#     if deal_string.find("*"):
#         mark = deal_string.find("*");
#         result_multiply = int(deal_string[mark - 1]) * int(deal_string[mark + 1]);
#         deal_string=deal_string.replace(str(result_multiply), deal_string[mark - 1:mark + 2]);
#         print(deal_string);

def calculate(s: str) -> int:
    n = len(s)
    stack = []
    preSign = '+'
    num = 0
    for i in range(n):
        if s[i] != ' ' and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')   # 得到数字
        if i == n - 1 or s[i] in '+-*/':
            if preSign == '+':
                stack.append(num)
            elif preSign == '-':
                stack.append(-num)
            elif preSign == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            preSign = s[i]
            num = 0
    return sum(stack)


print(calculate("3*2+2"));
