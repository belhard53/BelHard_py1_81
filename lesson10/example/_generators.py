

# def f1():
#     return 1
#     print(1)

# def f2():
#     yield 1
#     # print(123)
#     yield 2
#     yield 3
    
  

# # print(f1())

# b = list(f2())
# print(b)

# a = f2()
# for i in a:
#     print(i*1111)

# a = f2()
# print(next(a))
# print(next(a))
# print(next(a))
# # print(next(a))

# print(next(f2()))

# a = [i for i in range(1_000_000)]
# b = (i for i in range(1_000_000))

# print(a.__sizeof__())
# print(b.__sizeof__())

# print(b.__next__())
# print(b.__next__())
# -------------------------

# def f1(a):
#     i = 0
#     while i<a:
#         res = i*2+2*8/7
#         i += 1
#         yield res

# a = f1(10)

# for i in a:
#     print(i)


# -------------------------
# def f1():
#     for i in range(1, 9):
#         yield i*1111

# a = f1()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# for i in a:
#     print('--', i)

# --------------
# def f1():
#     yield 111
#     yield 222
#     yield 333
    
# def f2():
#     yield 11111
#     yield 22222
#     yield 33333
    
# def f3(a=f1(), b=f2()):        
#     while 1:
#         try:
#             yield next(a)
#             yield next(b)
#         except StopIteration:
#             break

# for item in f3():
#     print(item)
    
# # ------------------------
# def ping():
#     for i in range(2):
#         yield f"PING-{i}"


# def pong():
#     for i in range(2):
#         print(f"PONG-{i}")
#         yield from ping()


# p = pong()
# for i in p:
#     print(i)    
    
# ----------------------------

# def infinity_ping():
#     while ...:
#         yield "PONG"


# for i in infinity_ping():
#     print(i)
    