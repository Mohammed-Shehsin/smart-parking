
from torch.utils.data import Dataset
from PIL import Image
import os

class BayCropsDataset(Dataset):
    def __init__(self, root_dir, list_file, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        with open(list_file, 'r', encoding='utf-8') as f:
            self.items = [line.strip().split() for line in f if line.strip()]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        rel, lbl = self.items[idx]
        img = Image.open(os.path.join(self.root_dir, rel)).convert("RGB")
        if self.transform:
            img = self.transform(img)
        return img, int(lbl)
