# UNet CamVid Semantic Segmentation

## Overview

This repository is a cleaned semantic-segmentation project for the CamVid dataset using a UNet model in PyTorch.

## Tech Stack

- Python
- PyTorch
- UNet

## Project Structure

- `train.py`: training script
- `test.py`: prediction script for single images or directories
- `datasets/CamVid_dataloader11.py`: CamVid dataloader and color-map helpers
- `model/`: UNet model definition
- `metric/`: segmentation metric implementation
- `sample_predictions/`: example prediction outputs
- `figures/`: screenshots from local training usage

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Train:

```bash
python train.py --data_root ./CamVid --epochs 50 --batch_size 8
```

Predict:

```bash
python test.py --image_dir ./datasets/test --checkpoint ./checkpoint/unet_best.pth --overlay
```

## Notes

- The full CamVid dataset and trained checkpoints are intentionally excluded.
- This repository is a clean code snapshot rather than a full experiment backup.
