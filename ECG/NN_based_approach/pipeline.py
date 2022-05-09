from ECG.NN_based_approach.Networks.ConvNet1 import ConvNet1
from ECG.NN_based_approach.Networks.ConvNet import ConvNet
from ECG.NN_based_approach.NNType import NNType
import numpy as np
import torch

def process_recording(signal: np.ndarray, net_type: NNType, model_dir: str) -> np.double:
    device = torch.device('cpu')

    if net_type == NNType.Conv:
        net = ConvNet(n_classes=1)
    else:
        assert False, "Key 'net_type' must be one of NNType enum"

    model_path = model_dir + net_type.value + '_model.pt'
    print("Load model at", model_path)
    net.load_state_dict(torch.load(model_path, map_location=device))
    net.eval()

    x_val = torch.from_numpy(signal).float().reshape(1,1,12,5000)
    pred = net.forward(x_val.to(torch.device('cpu')))
    return pred.cpu().detach().item()

