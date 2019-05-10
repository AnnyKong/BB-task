import boto3
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import HTMLQuestion
from boto.mturk.layoutparam import LayoutParameter
from boto.mturk.layoutparam import LayoutParameters
import json

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import requests
from io import BytesIO
from PIL import Image
import xmltodict

# Create your connection to MTurk
mtc = boto3.client(
    'mturk',
    endpoint_url='https://mturk-requester.us-east-1.amazonaws.com',
    region_name='us-east-1',
    aws_access_key_id='AKIAJVKSLIGGO7BBVHIQ',
    aws_secret_access_key='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',
)

# This is the value you received when you created the HIT
# You can also retrieve HIT IDs by calling GetReviewableHITs
# and SearchHITs. See the links to read more about these APIs.
assignment_id = "39PAAFCODNNBRCN2M31R7R24ASXTV3"
result = mtc.get_assignment(AssignmentId=assignment_id)
assignment = result['Assignment']
worker_id = xmltodict.parse(assignment['WorkerId'])
print(str(assignment['Answer']))
xml_doc = assignment['Answer']
for answer in xml_doc['QuestionFormAnswers']['Answer']:
	worker_answer = str(answer['FreeText'])
	print(str(worker_answer))

# Load the image from the HIT
response = requests.get('https://s3-us-west-2.amazonaws.com/slowglass-testamk/comp100/04729.jpg')
img = Image.open(BytesIO(response.content))
im = np.array(img, dtype=np.uint8)

# Create figure, axes, and display the image
fig,ax = plt.subplots(1)
ax.imshow(im)

# Draw the bounding box
for answer in worker_answer:
    rect = patches.Rectangle((answer['left'],answer['top']),answer['width'],answer['height'],linewidth=1,edgecolor='#32cd32',facecolor='none')
    ax.add_patch(rect)

# Show the bounding box
plt.show()
