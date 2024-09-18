
import numpy as np

mask_ratio = 2800/1200

cam_1_bound = (np.array([
[   3, 1193],  
[   1,    6],  
[ 783,   46],  
[1060,  129],  
[1901,  325],  
[1844,  400],  
[1826,  482],  
[1564,  591],  
[1480,  620],  
[1470,  652],  
[1355,  696],  
[1304,  685],  
[1019,  800],  
[ 217, 1067],  
[ 154, 1193]
]) * mask_ratio).astype(int)

cam_2_bound = (np.array([
[ 616, 1191],  
[   0,  291],  
[   0,   24],  
[ 218,   21],  
[ 966,   29],  
[1197,   24],  
[1216,   47],  
[1349,   78],  
[1370,   76],  
[1419,   79],  
[1591,  107],  
[1678,  122],  
[1729,  143],  
[1916,  178],  
[1915,  475],  
[1674, 1196]
]) * mask_ratio).astype(int)

cam_3_bound = (np.array([
[ 145, 1190],  
[  53,  520],  
[ 94,  236],  
[ 130,  162],  # [ 151,  200],  
[ 184,  152],  
[ 447,  115],  
[ 458,   96],   
[ 640,   70],  
[ 665,   76],  
[ 872,   36],  
[1912,   99],  
[1915,  419],  
[ 978, 1193]
]) * mask_ratio).astype(int)

cam_4_bound = (np.array([
[1557, 1190],  
[1543, 1003],  
[ 647,  646],  
[ 475,  570],  
[ 429,  579],  
[ 308,  525],  
[ 284,  485],  
[  34,  385],  
[   3,  270],  
[   3,  182],  
[1118,   23],  
[1847,  81],  
[1892, 1173]
]) * mask_ratio).astype(int)

cam_bound_list = [cam_1_bound, 
                  cam_2_bound, 
                  cam_3_bound, 
                  cam_4_bound]