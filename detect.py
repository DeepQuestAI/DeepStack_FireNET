from deepstack_sdk import ServerConfig, Detection
import os

config = ServerConfig("http://localhost:80")
detection = Detection(config, name="firenetv1")

response = detection.detectObject(image=os.path.join("images", "test.png"), output=os.path.join("images", "test_detected.jpg"))

for obj in response:
    print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max,
                                                                                        obj.y_max))
