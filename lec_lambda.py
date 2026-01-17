import numpy as np
trig_list = [np.cos, np.sin, np.tan]

a_list = [lambda a: arg for arg in trig_list]
print(trig_list[0](1))
