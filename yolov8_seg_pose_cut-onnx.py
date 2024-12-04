import onnx
import os

def extract_onnx_model(input_path, output_path):
   
   input_names = ["images"]
   output_names = [
       "/model.22/Concat_1_output_0",
       "/model.22/Concat_2_output_0", 
       "/model.22/Concat_3_output_0",
       "/model.22/cv4.0/cv4.0.2/Conv_output_0",
       "/model.22/cv4.1/cv4.1.2/Conv_output_0",
       "/model.22/cv4.2/cv4.2.2/Conv_output_0"
   ]

   onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolov8n-pose.onnx", "yolov8n-pose-cut.onnx")
extract_onnx_model("yolov8s-pose.onnx", "yolov8s-pose-cut.onnx")
extract_onnx_model("yolov8m-pose.onnx", "yolov8m-pose-cut.onnx")
extract_onnx_model("yolov8n-seg.onnx", "yolov8n-seg-cut.onnx")
extract_onnx_model("yolov8s-seg.onnx", "yolov8s-seg-cut.onnx")
extract_onnx_model("yolov8m-seg.onnx", "yolov8m-seg-cut.onnx")
