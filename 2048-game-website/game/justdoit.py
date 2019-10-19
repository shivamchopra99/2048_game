import line to: from  /usr/local/lib/python3.4/dist-packages/watson_developer_cloud import VisualRecognitionV3 as VisualRecognition

visual_recognition = VisualRecognition(
    api_key='"7a85ea3ccce43d03daea662cb7b6b7236aeb4dd0"')

import json
from os.path import join, dirname
from os import environ

print(json.dumps(visual_recognition.detect_faces(images_url=https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg), indent=2))