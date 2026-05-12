# UNet CamVid Semantic Segmentation

This repository is a cleaned semantic segmentation project for the CamVid dataset using a UNet model in PyTorch.

It keeps the training, evaluation, data-loading, and metric code from the local project, while removing the large CamVid dataset and trained checkpoints that are not suitable for a regular GitHub repository.

## Included

- `train.py`: training script
- `test.py`: prediction script for single images or directories
- `datasets/CamVid_dataloader11.py`: CamVid dataloader and color map helpers
- `model/`: UNet model definition
- `metric/`: segmentation metric implementation
- `sample_predictions/`: a few example prediction outputs
- `figures/`: screenshot from local training usage

## Not Included

The original local project contained assets that are not stored in this GitHub copy:

- full `CamVid/` dataset
- local `checkpoint/unet_best.pth`
- full local test dataset under `datasets/test`
- all generated prediction outputs

## Install

```bash
pip install -r requirements.txt
```

## Expected Dataset Layout

```text
CamVid/
├── train/
├── train_labels/
├── val/
└── val_labels/
```

## Train

```bash
python train.py --data_root ./CamVid --epochs 50 --batch_size 8
```

## Predict

Predict a directory:

```bash
python test.py --image_dir ./datasets/test --checkpoint ./checkpoint/unet_best.pth --overlay
```

Predict a single image:

```bash
python test.py --image_dir ./some_image.png --checkpoint ./checkpoint/unet_best.pth --overlay
```

## Notes

- `test.py` saves colorized masks and optional overlay images.
- You need to provide your own dataset and checkpoint locally to reproduce results.
- This repository is intended as a clean code snapshot of the project rather than a full experiment backup.
