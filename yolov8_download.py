from ultralytics import YOLO
import os
os.chdir('./model')

# Load a model,Export to onnx with simplify
model = YOLO("yolov8n.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8s.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8m.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8s-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8n-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8m-seg.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8n-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8s-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)

# Load a model,Export to onnx with simplify
model = YOLO("yolov8m-pose.pt")
model.info()
model.export(format='onnx', simplify=True,opset=17)





