# Easy-Object-Detection
简单可扩展的PyTorch目标检测代码

| 名称   | 时间 | 亮点                                                         | paper链接                                                    | code链接                                                     |
| ------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SPPNet | 2014 | 1.**比例池化**：解决了RCNN速度慢的缺点，空间金字塔池化采用比例池化，不关心输入大小，也能够输出固定维度的特征，从而代替全连接层。<br />2.**特征共享**：SPP证明了只需要把原图在神经网络上走一遍，因为有了空间金字塔，不管输入是什么输出大小都是一样的，只需要把最后那层feature map按照比例裁剪，再分别放到池化层输出即可。<br />3.**通用性**：SPP可以改进所有基于CNN的方法 | [paper-SPPNet](https://link.springer.com/content/pdf/10.1007/978-3-319-10578-9_23.pdf) | [code-SPPNet](https://github.com/Windxy/Easy-Object-Detection/blob/main/SPPNet/SPPNet.py) |



## 待完成&完成

### 框架Architecture

- [ ] 🚌 R-CNN（PyTorch+onnx）
- [ ] 🚌 SPPNet（PyTorch+onnx）
- [ ] 🚌 Fast R-CNN（PyTorch+onnx）
- [ ] 🚌 Faster R-CNN（PyTorch+onnx）
- [ ] 🚌 SSD（PyTorch+onnx）
- [ ] 🚌 YOLOv1（PyTorch+onnx）
- [ ] 🚌 YOLOv2（PyTorch+onnx）
- [ ] 🚌 YOLOv3（PyTorch+onnx）
- [ ] 🚌 YOLOv4（PyTorch+onnx）
- [ ] 🚌 YOLOv5（PyTorch+onnx）
- [ ] 🚌 YOLOX（PyTorch+onnx）
- [ ] 🚌 CornerNet（PyTorch+onnx）
- [ ] 🚌 RetinaNet（PyTorch+onnx）
- [ ] 🚌 FCOS（PyTorch+onnx）
- [ ] 🚌 DETR（PyTorch+onnx）
- [ ] 🚌Swin Transformer（PyTorch+onnx）



### 组件Components

#### IoU损失（IoU Loss）

- [ ] 🚲Smooth-L1

- [ ] 🚲IoU

- [ ] 🚲GIoU

- [ ] 🚲DIoU

- [ ] 🚲CIoU

- [ ] 🚲IoUAware

  

#### 非极大值抑制（NMS）

- [ ] 🛹NMS
- [ ] 🛹SoftNMS
- [ ] 🛹MatrixNMS



#### 模块（module）

- [ ] 🚚特征金字塔网络 FPN
- [ ] 🚚空间金字塔池化 SPP
- [ ] 🚚路径聚合网络 PANet
- [ ] 



### 数据增强技巧（Data Augmentation）

- [ ] 🚕Resize
- [ ] 🚕Lighting
- [ ] 🚕Flipping
- [ ] 🚕Expand
- [ ] 🚕Crop
- [ ] 🚕Color Distort
- [ ] 🚕Random Erasing
- [ ] 🚕Mixup
- [ ] 🚕AugmentHSV
- [ ] 🚕Mosaic
- [ ] 🚕Cutmix
- [ ] 🚕Grid Mask
- [ ] 🚕Auto Augment
- [ ] 🚕Random Perspective
