# -yolo
1.训练ultralytics的一次训练
参考 https://blog.csdn.net/linmoqian/article/details/157656782?spm=1001.2014.3001.5501 这位大神的步骤，对15张奶蛙图片进行打框，
然后根据大神提供的代码，调整自己目标的数量与路径，成功得到相应的图表与best.pt，不过因为训练参数太低（硬件扛不住），所以将训练后的模
型进行预测时，得不到结果，ai识别不了，询问deepseek，得知可能是过拟合。相关图表与训练过程截图在 zip里

2.yolo的实时推理部署
参考deepseek提供的部分方案，我建立了一个demo_camera.py，成功调用了openCV的摄像头




3.接入应用web
依旧是参考deepseek的思路，新建web_app的文件夹，用python fastAPI建立了个后端（main.py）
然后用HTML简单搞了个Web前端（index.html）
不过一开始去浏览器搜的时候网页打不开，所以又问ai，然后加代码解决cors的跨域问题。









