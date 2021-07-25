import pickle
from pprint import pprint


with open('chances_x.bin', 'rb') as fp:
    pprint(pickle.load(fp))
