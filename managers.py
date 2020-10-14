from drivers import JSONDriver


class ProducersManager(JSONDriver):
    def __init__(self, path: str = 'producers.json'):
        super().__init__(path)

    def add_producer(self, producer: dict):
        producers_dict = self.load_data()
        names = [i['name'] for i in producers_dict['producers']]
        if producer['name'] not in names:
            producers_dict['producers'].append(producer)
            print(f'Добавлен продюсер {producer}')
        else:
            print('Продюсер уже есть!')
        self.save_data(producers_dict)

    def del_producer(self, name: str):
        producers_dict = self.load_data()
        for i, producer in enumerate(producers_dict['producers']):
            if producer['name'] == name:
                print(f'Удален продюсер {producers_dict["producers"].pop(i)}')
                self.save_data(producers_dict)
                return None
        print('Такого продюсера нету!')

    def get_producer(self, name: str):
        producers_dict = self.load_data()
        for i, producer in enumerate(producers_dict['producers']):
            if producer['name'] == name:
                return producer
        return 'Такой продюсер не найден!'


class CategoriesManager(JSONDriver):
    def __init__(self, path: str = 'producers.json'):
        super().__init__(path)

    def add_product(self, product: dict):
        products_dict = self.load_data()
        names = [i['name'] for i in products_dict['products']]
        if product['name'] not in names:
            products_dict['products'].append(product)
            print(f'Добавлен продукт {product}')
        else:
            print('Продукт уже есть!')
        self.save_data(products_dict)

    def del_product(self, name: str):
        products_dict = self.load_data()
        for i, product in enumerate(products_dict['products']):
            if product['name'] == name:
                print(f'Удален продукт {products_dict["products"].pop(i)}')
                self.save_data(products_dict)
                return None
        print('Такого продукта нету!')

    def get_product(self, name: str):
        products_dict = self.load_data()
        for i, product in enumerate(products_dict['products']):
            if product['name'] == name:
                return product
        return 'Такой продукт не найден!'


class DataManager(ProducersManager, CategoriesManager):
    def __init__(self, path='producers.json'):
        ProducersManager.__init__(self, path=path)
