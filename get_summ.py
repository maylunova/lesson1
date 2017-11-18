def get_summ(one, two, delimeter=' '):
    return str(one) + str(delimeter) + str(two)


one = 'hello'.upper()
two = 'world'.upper()
print(get_summ(one, two))
