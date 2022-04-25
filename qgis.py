import pandas as pd
import numpy as np

emd_shp = '/Users/kangchangmin/Desktop/intaek/workspace/search_area/EMD_20220324/emd.shp'
li_shp = '/Users/kangchangmin/Desktop/intaek/workspace/search_area/LI_20220324/li.shp'
save_path = '/Users/kangchangmin/Desktop/intaek/workspace/search_area'
cols = ['법정동코드', '중심점_x', '중심점_y']

emd_layer = QgsVectorLayer(emd_shp, "emd_layer", "ogr") # 읍면동 레이어
li_layer = QgsVectorLayer(li_shp, "li_layer", "ogr") # 리 레이어

def ext_csv(layer, filename):
    result = []
    # 폴리곤(읍면동리)마다 동 코드, 중심점 x 좌표, 중심점 y 좌표 구하기
    for feature in layer.getFeatures():
        id = feature.attributes()[0]
        geom = feature.geometry()
        center = geom.centroid()
        x = center.asPoint().x()
        y = center.asPoint().y()
        result.append([id, x, y])
    df = pd.DataFrame(np.array(result), columns=cols)
    df.to_csv(save_path + '/' + filename + '.csv', index=False)
    print(f'{filename} 저장 완료')

ext_csv(emd_layer, '읍면동_중심점')
ext_csv(li_layer, '리_중심점')
