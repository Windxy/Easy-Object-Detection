import torch
import os

from model import SPPNet


def main():
    net = SPPNet().eval()
    model_path = ''
    print('Loading weights into state dict...')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    if model_path!='':
        state_dict = torch.load(model_path, map_location=device)
        net.load_state_dict(state_dict)

    if device=='cuda':
        os.environ["CUDA_VISIBLE_DEVICES"] = '0'
        # net = nn.DataParallel(net)
        # net = net.cuda()

    # data type nchw
    dummy_input = torch.randn(1, 3, 256, 256)
    input_names = ["input"]
    output_names = ["output"]
    torch.onnx.export(net, dummy_input, "sppnet.onnx", verbose=True,
                      input_names=input_names,
                      output_names=output_names
                      )

if __name__ == '__main__':
  main()
