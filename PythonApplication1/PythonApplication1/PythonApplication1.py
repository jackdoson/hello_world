if 1+2:
    print("hello world!")#输出你好世界
else:
    print("false")
item_one=1
item_two=2
item_three=3
total=item_one+\
      item_two+\
      item_three
print(total)
counter=100
miles=1000.0
name="hello"
print(counter)
print(miles)
print(name)
a,b,c=1,2,"hello"
print(a,b,c)
print(type(a),type(b),type(c))
print(isinstance(a,int))
class a:
    pass
class b(a):
    pass
print(
    isinstance(a(),a),
    type(a())==a,
    isinstance(b(),a),
    type(b())==a
    )