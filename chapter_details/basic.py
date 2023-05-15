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

list_a = [1, 2, 3, 4, 5];
list_a.extend([6,7,8,9]);
print(list_a);