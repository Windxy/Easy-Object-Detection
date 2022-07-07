import math

# 引入了最小闭包区域的对角线距离
def DIoU(box1,box2):
    # box:[top,left,bottom,right]
    inter_h = min(box1[2],box2[2]) - max(box1[0],box2[0])
    inter_w = min(box1[3],box2[3]) - max(box1[1],box2[1])
    center1 = ((box1[1]+box1[3])/2,(box1[0]+box1[2])/2)
    center2 = ((box2[1]+box2[3])/2,(box2[0]+box2[2])/2)

    inter = 0 if inter_h < 0 or inter_w < 0 else inter_h*inter_w
    union = (box1[3]-box1[1])*(box1[2]-box1[0]) + (box2[3]-box2[1])*(box2[2]-box2[0]) - inter
    iou = inter / union

    distance = math.sqrt((center1[0]-center2[0])*(center1[0]-center2[0]) + (center1[1]-center2[1])*(center1[1]-center2[1]))
    min_x,min_y,max_x,max_y = min(box1[1],box2[1]),min(box1[0],box2[0]),max(box1[3],box2[3]),max(box1[2],box2[2])
    c = math.sqrt((min_x-max_x)*(min_x-max_x) + (min_y-max_y)*(min_y-max_y))

    distance_radio = distance / (1e-7 + c)
    diou = iou - distance_radio
    return diou