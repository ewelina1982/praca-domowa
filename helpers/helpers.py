def find_item_by_name(items, item_name):
    # print("test1"+item_name)
    # # print(items)
    # for i in items:
    #     if item_name in i.name:
    #         print(i.name)
    print(next(i for i in items if item_name in i.name))
    return next((i for i in items if item_name in i.name), None)