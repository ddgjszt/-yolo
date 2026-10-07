from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO
import shutil
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 加载模型 (确保 best.pt 放在同目录下，或者修改成绝对路径)
MODEL_PATH = "best.pt"
model = YOLO(MODEL_PATH) 

@app.post("/detect/")
async def detect_image(file: UploadFile = File(...)):
    # 1. 保存前端上传的图片
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # 2. 用 YOLO 进行推理
    results = model(file_location)
    
    # 3. 解析结果 (提取框、坐标、类别、置信度)
    detections = []
    for box in results[0].boxes:
        detections.append({
            "class": results[0].names[int(box.cls)],
            "confidence": float(box.conf),
            "bbox": [float(x) for x in box.xyxy[0]] # 左上右下坐标
        })
    
    # 4. 清理临时文件
    os.remove(file_location)
    
    # 5. 返回 JSON 数据给前端
    return JSONResponse(content={"filename": file.filename, "detections": detections})

# 运行方式: uvicorn main:app --reload