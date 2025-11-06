
import torch, argparse, os
from torch.utils.data import DataLoader
from torchvision import transforms
from parking.datasets import BayCropsDataset
from parking.models import mobilenetv3_tiny

def main(args):
    tfm = transforms.Compose([
        transforms.Resize((96, 96)),
        transforms.ToTensor()
    ])
    train_ds = BayCropsDataset(args.root, args.train_list, transform=tfm)
    val_ds   = BayCropsDataset(args.root, args.val_list, transform=tfm)

    train_loader = DataLoader(train_ds, batch_size=64, shuffle=True, num_workers=2)
    val_loader   = DataLoader(val_ds, batch_size=64, shuffle=False, num_workers=2)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = mobilenetv3_tiny().to(device)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    crit = torch.nn.CrossEntropyLoss()

    for epoch in range(10):
        model.train()
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            opt.zero_grad()
            loss = crit(model(x), y)
            loss.backward()
            opt.step()

        # quick val
        model.eval(); correct = n = 0
        with torch.no_grad():
            for x, y in val_loader:
                x, y = x.to(device), y.to(device)
                pred = model(x).argmax(1)
                correct += (pred == y).sum().item(); n += y.numel()
        print(f"Epoch {epoch+1}: val_acc={correct/n:.3f}")
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    torch.save(model.state_dict(), args.out)
    print('Saved:', args.out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--train_list", required=True)
    ap.add_argument("--val_list", required=True)
    ap.add_argument("--out", default="weights/occupancy_mbv3.pth")
    args = ap.parse_args()
    main(args)
