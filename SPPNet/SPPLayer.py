import math
import torch
import torch.nn.functional as F

# 构建SPP层(空间金字塔池化层)
class SPPLayer(torch.nn.Module):
    def __init__(self, num_levels, pool_type='max_pool'):
        super(SPPLayer, self).__init__()

        self.num_levels = num_levels
        self.pool_type = pool_type

    def forward(self, x):
        # feature map经历3个池化层，分别是4*4，2*2，1*1，最终提取21个特征
        num, c, h, w = x.size() # num:样本数量 c:通道数 h:高 w:宽
        for i in range(self.num_levels):
            level = i+1
            kernel_size = (math.ceil(h / level), math.ceil(w / level))
            stride = (math.ceil(h / level), math.ceil(w / level)) # 向下取整
            pooling = (math.floor((kernel_size[0]*level-h+1)/2), math.floor((kernel_size[1]*level-w+1)/2))

            # 选择池化方式
            if self.pool_type == 'max_pool':
                tensor = F.max_pool2d(x, kernel_size=kernel_size, stride=stride, padding=pooling).view(num, -1)
            if self.pool_type == 'avg_pool':
                tensor = F.avg_pool2d(x, kernel_size=kernel_size, stride=stride, padding=pooling).view(num, -1)

            # 将3个池化层拼接
            if (i == 0):
                SPP = tensor.view(num, -1)
            else:
                SPP = torch.cat((SPP, tensor.view(num, -1)), 1)
        return SPP

if __name__ == '__main__':
     X = torch.rand(10,3,256,256)
     net = SPPLayer(num_levels=3,pool_type='max_pool')
     out = net(X)
     print(out.shape)
