import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Infinix_Phone():

    def __init__(self) -> None:
        self.infinix_phone = pd.read_csv('data/infinix_phones_202310311513.csv')
        self.infinix_phones = np.array(self.infinix_phone)

    @property
    def infinix_phone_data(self):
        data = []
        for infinix_phone in self.infinix_phones:
            data.append({'id': infinix_phone[0], 'model': infinix_phone[0]})
        return data

    @property
    def infinix_phone_data_dict(self):
        data = {}
        for infinix_phone in self.infinix_phones:
            data[infinix_phone[0]] = infinix_phone[1] 
        return data

    def get_recs(self, kriteria:dict):
        wp = WeightedProduct(self.infinix_phone.to_dict(orient="records"), kriteria)
        return wp.calculate

if __name__ == "__main__":
    from settings import MODEL_SCALE

    data = pd.read_csv('data/infinix_phones_202310311513.csv').to_dict(orient="records")
    for infinix_phone in data:
        print("".join([x for x in MODEL_SCALE.keys() if x.lower() in infinix_phone['model'].lower()]))
