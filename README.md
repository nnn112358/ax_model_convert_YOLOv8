# ax_model_convert_YOLOv8


### 目的
[axera-tech](https://github.com/AXERA-TECH/ax-samples/)のサンプルプログラムの内、
yolov8のプログラムの実行に必要なモデルの変換を行う。
ソースコードは、ax620e/ax_yolov8_steps.cc、ax_yolov8_pose_steps.cc、ax_yolov8_seg_steps.ccに対応する。

https://github.com/AXERA-TECH/ax-samples/

### Dockerの起動

Dockerに、Pulsar2のイメージをロード。

```
sudo docker load -i ax_pulsar2_3.2_patch1_temp_vlm.tar.gz
```

### ultralyticsのインストール

```
$ pip install ultralytics
```


### モデル変換の実施

以下のPythonプログラムを実行。

```
$ python yolov8_download.py
$ python yolov8_cut-onnx.py
$ python yolov8_pose_cut-onnx.py
$ python yolov8_seg_cut-onnx.py
```

dockerでpulsar2を起動してスクリプトを実行。
```
$ sudo docker run -it --net host --rm -v $PWD:/data pulsar2:temp-58aa62e4
$ ./ax_model_convert.sh
```

axmodelを生成
```
# ls model/*axmodel
model/yolov10n.axmodel  model/yolov10s.axmodel  model/yolov9s.axmodel  model/yolov9t.axmodel
```

もしくは、pulsar2 buildを実行
```
pulsar2 build --input model/yolov8n-cut.onnx --output_dir output --config config/yolov8-config.json --target_hardware AX620E
cp output/compiled.axmodel model/yolov8n.axmodel
```

### M5Stack Module-LLMでの実行

 Module-LLMにコピーして、実行。
 
```
./ax_yolov8 -i m52.jpg -m yolov8s.axmodel
./ax_yolov8_pose -i m52.jpg -m yolov8s-pose.axmodel
./ax_yolov8_seg -i m52.jpg -m yolov8s-seg.axmodel
```

