def IoU(box1,box2):
    # box:[top,left,bottom,right]
    # 交集框的左上角坐标 =  max(A的左上角坐标，B的左上角坐标)
    # 交集框的左上角坐标 =  min(A的左上角坐标，B的左上角坐标)
    inter_h = min(box1[2],box2[2])-max(box1[0],box2[0])  # 交集框的高
    inter_w = min(box1[3],box2[3])-max(box1[1],box2[1])  # 交集框的宽
    inter = 0 if inter_h<0 or inter_w <0 else inter_h*inter_w  # 当A和B没有交集的时候，h和w的值小于0
    union = (box1[3]-box1[1])*(box1[2]-box1[0]) + (box2[3]-box2[1])*(box2[2]-box2[0]) - inter # 并集框
    iou = inter / union # iou=交集/并集
    return iou
