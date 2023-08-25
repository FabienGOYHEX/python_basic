a = [1, 2, 'hello', True, 5, ['a', 2]]

#a[1] = 3
# => [1, 3, 'hello', True, 5, ['a', 2]]

#b = list("hello")
# DECOMPACTAGE

variable1, variable2, varaible3, *listedureste = a
# => 1 2 hello [True, 5, ['a', 2]]
