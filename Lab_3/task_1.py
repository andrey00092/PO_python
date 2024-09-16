# TODO Напишите функцию для поиска индекса товара

def index_search(shop_list, missed_item):
    for idx in range(0, len(shop_list)):
        if shop_list[idx] == missed_item:
            return idx
        if idx == len(shop_list):
            return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_search(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
