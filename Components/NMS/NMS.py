import numpy as np

def non_max_suppress(predicts_dict, threshold=0.2):
    '''
    predicts_dict : {"label_A":[[x1,y1,x2,y2,score],[]...],...} 预测得到的标签+位置信息+置信度
    threshold : 抑制阈值，高于该值的框将被除掉（去重原则）
    '''
    for object_name, bbox in predicts_dict.items():
        bbox_array = np.array(bbox, dtype=np.float32)
        x1, y1, x2, y2, scores = bbox_array[:, 0], bbox_array[:, 1],\
        						 bbox_array[:, 2], bbox_array[:, 3], bbox_array[:,4]
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]
        keep = []
        while order.size > 0:
            keep.append(order[0])
            w1 = np.maximum(x1[order[0]],x1[order[1:]]) - np.minimum(x2[order[0]],x2[order[1:]])
            h1 = np.maximum(y1[order[0]],y1[order[1:]]) - np.minimum(y2[order[0]],y2[order[1:]])
            inter = np.maximum(0.0, w1 + 1) * np.maximum(0.0, h1 + 1)   # 获取交集的面积
            union = areas[order[0]] + areas[order[1:]] - inter          # 获取并集的面积
            iou = inter / union                                         # 计算得到IoU
            indexs = np.where(iou <= threshold)[0] + 1	                # 核心，去重得到新的索引
            order = order[indexs]

        bbox = bbox_array[keep]
        predicts_dict[object_name] = bbox.tolist()
        predicts_dict = predicts_dict

    return predicts_dict