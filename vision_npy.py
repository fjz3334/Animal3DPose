import numpy as np

# 注意编码方式
pre_train = np.load("./data/mesh_down_sampling_4.npz", allow_pickle=True, encoding="latin1")
# ls = list(range(0,16))
# np.save('./data/sheep/test_sheep.npy',ls)
# pre_train = np.load('./data/test_shape.npy')
print("------type-------")
print(type(pre_train))
print("------shape-------")
# print(pre_train.shape)
print("------data-------")
print(pre_train)
# data = np.load("./data/mesh_down_sampling_4.npz", encoding='latin1', allow_pickle=True)
# A = data['A']
# U = data['U']
# D = data['D']
# print(A,U,D)