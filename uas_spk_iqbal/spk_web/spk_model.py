from settings import MODEL_SCALE, PROCESSOR_SCALE

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7
        self.raw_weight = {
            'model': 6,
            'ram': 5,
            'processor': 4,
            'storage': 1,
            'battery': 3,
            'price': 7,
            'screen_size': 2
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]]
                temp2 = {v: k for k, v in setWeight.items()}[item[1]]
                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': infinix_phone['id'],
            'model': MODEL_SCALE["".join([x for x in MODEL_SCALE.keys() if x.lower() in infinix_phone['model'].lower()])],
            'ram': infinix_phone['ram'],
            'processor': PROCESSOR_SCALE["".join([x for x in PROCESSOR_SCALE.keys() if x.lower() in infinix_phone['processor'].lower()])],
            'storage': infinix_phone['storage'],
            'battery': infinix_phone['battery'],
            'price': infinix_phone['price'],
            'screen_size': infinix_phone['screen_size']
        } for infinix_phone in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        model = [] # max
        ram = [] # max
        processor = [] # max
        storage = [] # max
        battery = [] # max
        price = [] # min
        screen_size = [] # max

        for data in self.data:
            model.append(data['model'])
            ram.append(data['ram'])
            processor.append(data['processor'])
            storage.append(data['storage'])
            battery.append(data['battery'])
            price.append(data['price'])
            screen_size.append(data['screen_size'])

        max_model = max(model)
        max_ram = max(ram)
        max_processor = max(processor)
        max_storage = max(storage)
        max_battery = max(battery)
        min_price = min(price)
        max_screen_size = max(screen_size)

        return [{
            'id': data['id'],
            'model': data['model']/max_model, # benefit
            'ram': data['ram']/max_ram, # benefit
            'processor': data['processor']/max_processor, # benefit
            'storage': data['storage']/max_storage, # benefit
            'battery': data['processor']/max_battery, # benefit
            'price': min_price/data['price'], # cost
            'screen_size': data['screen_size']/max_screen_size # benefit
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)

    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['model'] ** weight['model'] *
                row['ram'] ** weight['ram'] *
                row['processor'] ** weight['processor'] *
                row['storage'] ** weight['storage'] *
                row['battery'] ** weight['battery'] *
                row['price'] ** (-weight['price']) *
                row['screen_size'] ** weight['screen_size']
                , 2
            )

            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))
