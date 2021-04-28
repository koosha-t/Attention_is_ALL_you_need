import torch.nn as nn

"""
In Transformer's architecture, a residual connection followed by layer normalization is employed 
around each sub-layer in both encoder and decoder.That is, the output of each sub-layer is LayerNorm(x+Sublayer(x)), 
where Sublayer(x) is the function implemented by the sub-layer itself. 
"""

class LayerNorm(nn.Module):
    def __init__(self):
        pass