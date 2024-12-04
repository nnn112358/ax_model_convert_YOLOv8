import onnx
import os

def extract_onnx_model(input_path, output_path):
   
   input_names = ["images"]
   output_names = [
       "/model.22/Concat_output_0",
       "/model.22/Concat_1_output_0", 
       "/model.22/Concat_2_output_0"
   ]

   onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolov8n.onnx", "yolov8n-cut.onnx")
extract_onnx_model("yolov8s.onnx", "yolov8s-cut.onnx")
extract_onnx_model("yolov8m.onnx", "yolov8m-cut.onnx")


