# 01 — Introduction

## Goal
The objective of this project is to develop an intelligent system capable of **automatically detecting vehicle license plates** from RGB images using modern deep-learning–based object detection techniques. The system highlights the plate region using bounding boxes and forms the core component of an extended ANPR (Automatic Number Plate Recognition) pipeline.

In its enhanced form, the project also integrates an **OCR-based text extraction step**, enabling the system not only to detect plates but also to **read and interpret their alphanumeric content**.

## Motivation
License plate detection plays a central role in modern transportation and safety infrastructure:

- Smart parking systems and toll automation  
- Highway traffic monitoring  
- Police enforcement and vehicle search  
- Smart city surveillance  
- Entry/exit automation for residential or industrial zones  

Traditional manual monitoring is slow, expensive, and prone to human error. An automated system enables:

- High-speed and reliable plate localization  
- Scalability across thousands of daily vehicles  
- Integration with OCR for complete ANPR pipelines  
- Real-time decision-making and enforcement  

By leveraging YOLOv8 for plate detection and OCR for text interpretation, the project demonstrates how AI can automate key traffic-management tasks.

## Input Data
The model processes **RGB images** containing cars. Each training image includes YOLO-format annotations:

`` class x_center y_center width height ``



Values are normalized between 0 and 1.  
In the enhanced pipeline, the detected plate region becomes the input for OCR, enabling full number-plate reading.

## AI Domain & Task Type

**Domain:** Artificial Intelligence → Computer Vision  
**Subfield:** Object Detection & OCR  
**Model Type:** Convolutional Neural Networks (YOLOv8) + OCR (EasyOCR)  
**Tasks:**  
- Bounding box regression  
- Object classification  
- Text extraction (OCR)
