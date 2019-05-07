
for i in range(1,11):
   print('\
   <crowd-bounding-box \n \
         src=\'${image_url' + str(i) + '}\' \n \
         labels="[\'Left Image\', \'Right Image\']" \n \
         header="Draw bounding boxes to annotate the edges of left and right images" \n \
         name="annotatedResult"> \n \n \
         <short-instructions>Draw bounding boxes to annotate the edges of left and right images.</br> \n \
          <h2 style="color:green;">Examples</h2> \n \
          <h3 style="color:red;">  Red boxes are bad</h3> \n \
          <h3 style="color:#FF9F00">  Yellow boxes are good</h3> \n \
          <hr> \n \
          - Do <b>include</b> artifacts - tapes, scratches, light leaks, etc. \n \
          <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example1.png" \n \
            style="max-width:100%"/><hr></br> \n \
          - <b>Only</b> include contents of image. \n \
          <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example2.png" \n \
            style="max-width:100%"/><hr></br> \n \
          - <b>Avoid</b> blurred areas. \n \
          <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example3.png" \n \
            style="max-width:100%"/></br> \n \
          <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example4.png" \n \
            style="max-width:100%"/><hr></br> \n \
         </short-instructions> \n \n \
         <!-- Use the full-instructions section for more detailed instructions that the \n \
               Worker can open while working on the task. Including more detailed \n \
               instructions and additional examples of good and bad answers here can \n \
               help get good results. You can include any HTML here. --> \n \
         <full-instructions header="Bounding Box Instructions"> \n \
             <p>Use the bounding box tool to draw boxes to annotate the edges of both left and right images:</p> \n \n \
                <li>Annotate the full view of <b>left</b> and <b>right</b> image.</li> \n \
                <li>Do <b>include</b> "artifact" such as tapes, scratches, light leaks, etc.  \n \
                    overlap with the contents of images. You may use the left/right image to judge \n \
                    whether the dubious part is the image content or not.</li> \n \
                <li>Make sure the box includes <b>only</b> contents of images. If you are unsure of \n \
                    whether this is the content of the image, please leave out</li> \n \
                <li><b>Exclude</b> blurred boundaries of the images, \n \
                  they\'re not considered as a part of the images.</li> \n \
                <li>Avoid curved edges, <b>only</b> include contents of the image.</li> \n \
                <li>If the image goes off the screen, label up to the edge of the image.</li> \n \n \
                <h2 style="color:green;">Examples</h2> \n \
                  <h3 style="color:red;">  Red boxes are bad</h3> \n \
                  <h3 style="color:#FF9F00">  Yellow boxes are good</h3> \n \
                  <hr> \n \
                  - Do <b>include</b> artifacts - tapes, scratches, light leaks, etc. \n \
                  <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example1.png" \n \
                    style="max-width:100%"/><hr></br> \n \
                  - <b>Only</b> include contents of image. \n \
                  <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example2.png" \n \
                    style="max-width:100%"/><hr></br> \n \
                  - <b>Avoid</b> blurred areas. \n \
                  <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example3.png" \n \
                    style="max-width:100%"/></br> \n \
                  <img src="https://s3-us-west-2.amazonaws.com/slowglass-testamk/examples/example4.png" \n \
                    style="max-width:100%"/><hr></br> \n \
             </ol> \n \
         </full-instructions> \n \
     </crowd-bounding-box>')
