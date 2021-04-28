import torch
import torch.nn as nn
import torch.nn.functional as F

"""
Most competitive neural sequence transduction models have an encoder-decoder structure. 
Here, the encoder maps an input sequence of symbol representations (x1,…,xn) to a sequence of 
continuous representations z=(z1,…,zn). Given z, the decoder then generates an output sequence (y1,…,ym) of symbols one element at a time.
At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.
"""


class EncoderDecoder(nn.Module):
    """
    A standard Encoder-Decoder architecture.
    """
    def __init__(self, encoder, decoder, src_embed, tgt_embed, generator):
        super(EncoderDecoder,self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.src_embed = src_embed
        self.tgt_embed = tgt_embed
        self.generator = generator

    def encode(self, src, src_mask):
        return self.encoder(self.src_embed(src), src_mask)

    def decode(self, memory, src_mask, tgt, tgt_mask):
        return self.decoder(self.tgt_embed(tgt),memory, src_mask, tgt_mask)

    def forward(self, src, tgt, src_mask, tgt_mask):
        return self.decode(self.encode(src,src_mask),src_mask, tgt, tgt_mask)


