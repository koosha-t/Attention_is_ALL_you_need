import torch
import torch.nn as nn

"""
In Transformer's architecture, a residual connection followed by layer normalization is employed 
around each sub-layer in both encoder and decoder.That is, the output of each sub-layer is LayerNorm(x+Sublayer(x)), 
where Sublayer(x) is the function implemented by the sub-layer itself. 
"""

class LayerNorm(nn.Module):
    " Construct a layernorm module "
    def __init__(self, features, eps=1e-6):
        super(LayerNorm,self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim = True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2



