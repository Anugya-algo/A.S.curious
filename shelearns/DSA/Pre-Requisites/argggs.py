#* unpack
# *args =allow to pass any number of non key arguments ,dont know b4hand ,stores in the form of TUPLE
# **kwargs=pass multiple keyword arguments,extra options to be appended, stores as DICTIONARY

# def price(*args,**kwargs):
#     item_price=p-d(p)/100
#     return(item_price)

# item=['mop','cooker','brush','sponge']
# price_item=dict(mop=550,cooker=1200,brush=30,sponge=40)
# p=price_item['**kwargs']
# discount=dict(mop=12,cooker=15,brush=8,sponge=20)
# d=discount['**kwargs']

def price(*args, **kwargs): 
    result = {}
    for item in args:
        if item in kwargs['prices'] and item in kwargs['discounts']:
            original_price = kwargs['prices'][item]
            discount = kwargs['discounts'][item]
            discounted_price = original_price - (discount * original_price / 100)
            result[item] = discounted_price
        else:
            result[item] = "No data"
    return result


price_item = {'mop': 550, 'cooker': 1200, 'brush': 30, 'sponge': 40}

discount = {'mop': 12, 'cooker': 15, 'brush': 8, 'sponge': 20}

items = ['mop', 'cooker', 'brush', 'sponge']
final_prices = price(*items, prices=price_item, discounts=discount)
print(final_prices)
