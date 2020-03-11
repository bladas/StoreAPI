from apps.product.models import Product, Category
import json
from decimal import Decimal


def create(json, Product, Category):
    with open('citrus.json', 'r') as json_file:
        data = json.load(json_file)

        for elem in data:
            # print(elem.get('name'))
            # print(elem.get('category'))
            # print(elem.get('undercategory'))
            price = elem.get('price').split(' ')
            urlimg = 'citrus/' + elem.get('img')
            try:
                true_price = price[0]+price[1]

            except:
                true_price = int(price[0])


            # print(true_price)
            # print(urlimg)
            try:
                print("start")
                category = Category.objects.get(name=elem.get('category'))
                print("Category"+str(category))

                print("2 step next")
                try:
                    print("2 step try")
                    ucategory = Category.objects.get(name=elem.get('undercategory'), parent=category)
                    print("Ucategory"+str(ucategory))
                    new_product = Product.objects.create(name=elem.get('name'), category=ucategory,
                                                            price=float(true_price),photo=urlimg)
                    new_product.save()
                except:
                    print("2 step except")
                    print(elem.get('undercategory'))
                    print(category)
                    new_uc = Category.objects.create(name=elem.get('undercategory'), parent=category)
                    new_uc.save()
                    print("except 2.1")
                    new_product = Product.objects.create(name=elem.get('name'), category=new_uc,
                                                         price=float(true_price),photo=urlimg)
                    new_product.save()
                    print("2 step product ready")

            except:
                print("1 step except")
                new_category = Category.objects.create(name=elem.get('category'))
                new_category.save()
                # try:
                new_uc = Category.objects.create(parent=new_category,name = elem.get('undercategory'))
                new_uc.save()
            #     except:
            #         new_uc = UnderCategory.objects.create(title=elem.get('undercategory'), category=new_category)
            #         new_uc.save()
                new_product = Product.objects.create(name=elem.get('name'), category=new_uc,price=float(true_price),photo=urlimg)
                new_product.save()
                print("1 step product exist")

create(json,Product,Category)

# print(create())
# create(json, Category, UnderCategory, Product)
# , Category, UnderCategory, Product
