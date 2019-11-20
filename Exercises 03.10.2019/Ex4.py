dct_products = {'apple': 5, 'banana': 4, 'orange': 6,
                'milk': 20, 'bread': 10, 'chicken': 50, 'meat': 70}
money = 40


def possibility(dct_shop, pay):  # назвение не очень удачное, но ок
    for key in dct_products:  # нетнетнет, подумай что не так
        if dct_shop[key] <= pay:
            print(key)


possibility(dct_products, money)

dct2 = {'a': 10, 'b': 20, 'c': 50}
possibility(dct2, 30)  # на этой строке программа вообще падает. Так не должно быть

# 3/10 (не решено)
