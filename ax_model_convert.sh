#!/bin/bash

# ログファイルの設定
LOG_FILE="build_$(date +%Y%m%d_%H%M%S).log"
exec 1> >(tee -a "$LOG_FILE")
exec 2> >(tee -a "$LOG_FILE" >&2)

echo "Build process started at $(date)"

# モデルビルド関数
build_model() {
    local input=$1
    local output=$2
    local config=$3
    
    echo "Building model: $input"
    pulsar2 build --input "$input" --output_dir output --config "$config" --target_hardware AX620E
    if [ $? -eq 0 ]; then
        cp output/compiled.axmodel "$output"
        echo "Successfully built and copied to $output"
    else
        echo "Error building model $input" >&2
        return 1
    fi
}

# YOLO検出モデル
build_model "model/yolov8m-cut.onnx" "model/yolov8m.axmodel" "config/yolov8_config.json"
build_model "model/yolov8n-cut.onnx" "model/yolov8n.axmodel" "config/yolov8_config.json"
build_model "model/yolov8s-cut.onnx" "model/yolov8s.axmodel" "config/yolov8_config.json"

build_model "model/yolov8m-pose-cut.onnx" "model/yolov8m-pose.axmodel" "config/yolov8_pose_config.json"
build_model "model/yolov8n-pose-cut.onnx" "model/yolov8n-pose.axmodel" "config/yolov8_pose_config.json"
build_model "model/yolov8s-pose-cut.onnx" "model/yolov8s-pose.axmodel" "config/yolov8_pose_config.json"

build_model "model/yolov8m-seg-cut.onnx" "model/yolov8m-seg.axmodel" "config/yolov8_seg_config.json"
build_model "model/yolov8n-seg-cut.onnx" "model/yolov8n-seg.axmodel" "config/yolov8_seg_config.json"
build_model "model/yolov8s-seg-cut.onnx" "model/yolov8s-seg.axmodel" "config/yolov8_seg_config.json"



echo "Build process completed at $(date)"