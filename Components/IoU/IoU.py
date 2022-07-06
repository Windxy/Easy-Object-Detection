def IoU(box1,box2):
    # box:[top,left,bottom,right]
    inter_h = min(box1[2],box2[2])-max(box1[0],box2[0])
    inter_w = min(box1[3],box2[3])-max(box1[1],box2[1])
    inter = 0 if inter_h<0 or inter_w <0 else inter_h*inter_w
    union = (box1[3]-box1[1])*(box1[2]-box1[0]) + (box2[3]-box2[1])*(box2[2]-box2[0]) - inter
    iou = inter / union
    return iou