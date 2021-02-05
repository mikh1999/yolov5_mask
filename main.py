python3 train.py --img 640 --batch 4 --epochs 50 --data ../dataset/data.yaml --weights yolov5s.pt
python3 train.py --img 640 --batch 6 --epochs 50 --data ../yolov5/dataset/data.yaml --weights ../yolov5/runs/train/exp12/weights/last.pt

python3 detect.py --weights ../yolov5/runs/train/exp7/weights/last.pt --img 640 --conf 0.4 --save-txt --source ../yolov5/data/images

exp15 - best