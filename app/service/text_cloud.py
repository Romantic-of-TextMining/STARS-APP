import json
from PIL import Image
from io import BytesIO
import os
from os.path import exists

#for generate textcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#local
from app.lib import benchmark

class AddTextCloud:
    def __init__(self, cluster):
        self.input = {
            "cluster": cluster,
            "levels": cluster.keys()
        }
        dirname = os.path.dirname(__file__)
        self.input["result_path"] = os.path.join(dirname, '../static/result')

    def get_textcloud_path(self, level):
        figure_path = os.path.join(self.input["result_path"], f'{level}.png')
        return figure_path

    def get_textclouds_path(self):
        path = []
        for level in self.input["levels"]:
            path.append(self.get_textcloud_path(level))
        return path

    def get_textclouds_level(self):
        return self.input["levels"]

    def check_result(self):
        #return os.path.exists(self.input["result_path"])
        return False
    
    @benchmark.timerfunc
    def create_textcloud(self):
        for level,token in self.input["cluster"].items():
            if not self.check_result():
                #self.read_json()
                self.generate_textcloud(level, token)
        #return self.msg
        return

    def read_json(self):
        # Opening JSON file
        #with open(self.input["path"], 'r') as openfile:  
            # Reading from json file
            #self.input["words"] = json.load(openfile)
            #print("type:", type(self.input["words"]))
        self.input["words"] = json.load(self.input["token"])   
        print(f"words: {self.input.words}")

    def generate_textcloud(self, level, token):
        words = token
        seg_list = " ".join(words)

        #x, y = np.ogrid[:1500, :1500]

        #mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
        #mask = 255 * mask.astype(int)

        #back_image = ""
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
        
        wc.to_file(self.get_textcloud_path(level))

class GenerateTfIdfTag:

    @classmethod
    def transform_tag(self, field_dict):
        for level, token_dict in field_dict.items():
            tagList = []
            minFreq=20000
            for token, tfidf in token_dict.items():
                freq = round(tfidf, 4)*10000 + 1
                if freq < minFreq:
                    minFreq = freq
                tagList.append([token, freq])
            field_dict[level] = {
                "minFreq": minFreq,
                "tagList": tagList
            }
        
        return field_dict
