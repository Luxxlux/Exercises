# code method replace_char
# the method takes 3 parameters : (str, chr, chr)
# the method will return the given str, but with all the specified first chr,
# replaced by the second

# exemple :
test = "aaaa bbbb cccc"
# result = replace_char(test, ' ', 'X')
# gives us : "aaaaXbbbbXcccc"
#
# the prototype must be :

# --------------------------- Laimis Practice ---------------------------------------------


# def laimis_rep(test: str, x: chr, y: chr):
#     txt = "I like bananas"
#
#     x = txt.replace(" ", "apples")
#
#     print(x)
#     print(test)
#
#
# laimis_rep(test,'x','y')

# --------------------------- End of Laimis Practice --------------------------------------


def replace_char(test: str, x: str, y: str) -> str:
    print(test)
    replaced_test = test.replace(' ','X')
    print(replaced_test)
    return

replace_char(test,'x','y')

