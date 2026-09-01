# def square(x):
#   return x ** 2
# print(square(5))

##Lambda
# square_lambda = lambda x: x ** 2
# print(square_lambda(5))


##map (transform every item)
# nums = [1, 2, 3, 4, 5]
# doubled = list(map(lambda n: n * 2, nums))
# print(doubled)

##filter: Keep only items where the function return True
# evens = list(filter(lambda n: n % 2 == 0, nums))
# print(evens)

##Both (maps filter) are same as comprehension style writing

## sorted() with key=
# words = ["banana", "kiwi", "apple"]
# print(sorted(words))
# print(sorted(words, key=len))
# print(sorted(words, key=len, reverse=True))