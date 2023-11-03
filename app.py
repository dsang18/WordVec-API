from flask import Flask, request
from flask_restful import Resource, Api #, reqparse
from flask_cors import CORS
import gensim.downloader as gd
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)
#
CORS(app)

api = Api(app)


     
# words = ['shoes', 'socks', 'loafer']

def conv_string_to_list(string):
    list_of_words=[]
    if "," in string:
        list_of_words=string.split(",")
    else:
        list_of_words.append(string)
    return list_of_words
 
wv_from_bin_glove = gd.load("glove-wiki-gigaword-300")

class prediction(Resource):
    def get(self,ViT_words, user_words):
        try:
            # print(bid_tendency,bid_ratio,succ_outbid,win_ratio)
            ouput_preed_from_ViT=conv_string_to_list(string)
            shoes_vector = wv_from_bin_glove[user_input].reshape(1, -1)
            similarity=[]
            for w in words:
                try:
                    w_vector = wv_from_bin_glove[w].reshape(1, -1)
                except KeyError:
            # The vector for this word doesn't exist, so return a vector of zeros
                    w_vector = np.zeros((1, 300))
        
                similarity.append(cosine_similarity(shoes_vector, w_vector)[0][0])
            print("\n")
            count=0
            if len(similarity)==1:
        
                if similarity[0]>0.5:
                    return f"yes"
                else:
                    return f"No"
            else:
                for i in range(len(similarity)):
                    if similarity[i]>0.5:
                        count+=1
                    if count==int(len(similarity)/2):
                        return f"yes"
                        break
                return f"No"

        except Exception as e:
            print(e)
            # return e



api.add_resource(prediction,'/predict/<string:ViT_words>&<string:user_words>')



if __name__ == '__main__':
    app.run(debug=True)

'shoes,shirt,pants','cap'

#