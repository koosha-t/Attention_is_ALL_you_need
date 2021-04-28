import torch.nn as nn
import copy

def clones(module, N):
    "produce N identical layers"
    return nn.ModuleList([copy.deepcopy(module)] for _ in range(N))

class Encoder:
    "Core Encoder is a stack of N layers"
    def __init__(self, layer, N):
        super(Encoder,self).__init__()
        self.layers = clones(layer,N)

    def forward(self):
        pass





