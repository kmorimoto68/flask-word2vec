from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__,
            static_folder='./frontend/dist/static',
            template_folder='./frontend/dist'
            )
app.config.from_object(__name__)
CORS(app)

from gensim.models import word2vec
model = word2vec.Word2Vec.load('../dic/word2vec.gensim.model')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route("/w", methods=['GET'])
def word2vec():
    keyword = request.args.get('keyword')
    res = []
    try:
        results = model.most_similar(keyword, [], 10)
        for result in results:
            word, value = result
            dict = {
                'word': word,
                'value': value,
            }
            res.append(dict)
    except:
        pass
    return jsonify(results=res)


from gensim.models import KeyedVectors
model_dir = '../dic/entity_vector.model.bin'
kmodel = KeyedVectors.load_word2vec_format(model_dir, binary=True)

@app.route("/ww", methods=['GET'])
def word2veckv():
    keyword = request.args.get('keyword')
    res = []
    try:
        results = kmodel.most_similar([keyword])
        for result in results:
            word, value = result
            dict = {
                'word': word,
                'value': value,
            }
            res.append(dict)
    except:
        pass
    return jsonify(results=res)

@app.route("/calc", methods=['GET'])
def calc():
    positive = request.args.get('positive')
    negative = request.args.get('negative')
    res = []
    try:
        results = kmodel.most_similar(positive=['[' + positive + ']'],negative=['[' + negative + ']'])
        for result in results:
            word, value = result
            dict = {
                'word': word,
                'value': value,
            }
            res.append(dict)
    except:
        pass

    return jsonify(results=res)

if __name__ == '__main__':
    app.run()
