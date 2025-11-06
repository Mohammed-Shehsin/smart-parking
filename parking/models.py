
import torch
import torch.nn as nn
from torchvision import models

def mobilenetv3_tiny(num_classes: int = 2):
    m = models.mobilenet_v3_small(weights=None)
    m.classifier[-1] = nn.Linear(m.classifier[-1].in_features, num_classes)
    return m
