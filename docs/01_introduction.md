# 01 — Introduction

## Goal

Develop an AI model capable of automatically detecting car number plates from images by drawing bounding boxes around the plate region.

## Motivation

Automatic license plate detection is a core module for modern Intelligent Transportation Systems, including:

- Toll & parking automation

- Highway traffic monitoring

- Police enforcement systems

- Smart city surveillance

- ANPR (Automatic Number Plate Recognition)

- Manual monitoring is slow, costly, and error-prone.

An AI-based detector enables:

- Real-time vehicle analysis

- Automation at scale

- Consistent accuracy

- Integration with OCR for full ANPR pipelines

## Input Data

The system takes RGB images of vehicles.
Each image is annotated with a bounding box around the license plate using YOLO format:

``class x_center y_center width height``


All coordinates are normalized (0–1).

## AI Domain & Task Type

Domain: Artificial Intelligence → Computer Vision

Subfield: Object Detection

Model Type: Convolutional Neural Network (CNN)

Technique: Single-class detection (“plate”)

Task: Bounding box regression + object classification
