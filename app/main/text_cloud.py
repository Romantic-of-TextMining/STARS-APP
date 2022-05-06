import json
from PIL import Image
from io import BytesIO
import os

#for generate textcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class AddTextCloud:
    def __init__(self, path):      
        self.input = {"path": path}     
 
    def generate_textcloud(self):
        words = self.input["words"]
        seg_list = " ".join(words)

        x, y = np.ogrid[:1500, :1500]

        mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
        mask = 255 * mask.astype(int)

        back_image = ""
        #import imageio
        # back_image = imageio.imread('/ukraine.jpg') # Background image

        wc = WordCloud(
            width=1500,
            height=1500,
            background_color='white',               #   Background Color
            max_words=200,                    #   Max words
        #    mask=back_image,                       #   Background Image
            max_font_size=None,                   #   Font size
        #    font_path="/content/drive/MyDrive/Colab Notebooks/GenJyuuGothic-Bold.ttf",             #   Display font
            random_state=30,                    #   Random color
            prefer_horizontal=0.9)                #   Ratio

        wc.generate(seg_list)
        print(wc)
        #plt.figure( figsize=(5,5), facecolor='k') # Output plot size
        #plt.axis("off")
        #plt.tight_layout(pad=0)
        #plt.imshow(wc, interpolation="bilinear")

        # Save it to a temporary buffer.
        #buf = BytesIO()
        #fig.savefig(buf, format="png")
        # Embed the result in the html output.
        #self.msg["data"] = base64.b64encode(buf.getbuffer()).decode("ascii")

        #plt.savefig('static/result/text_cloud.png')
        dirname = os.path.dirname(__file__)
        result_path = os.path.join(dirname, '../static/result/text_cloud.png')

        wc.to_file(result_path)

        #self.msg["data"] = 0
#        return self.msg

    def read_json(self):
        # Opening JSON file
        with open(self.input["path"], 'r') as openfile:  
            # Reading from json file
            self.input["words"] = json.load(openfile)
            #print("type:", type(self.input["words"]))

    def create_textcloud(self):
        self.read_json()
        self.generate_textcloud()
        #return self.msg