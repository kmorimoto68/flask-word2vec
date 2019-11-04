from gensim.models import KeyedVectors
model_dir = '../dic/entity_vector.model.bin'
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)
results = model.most_similar(positive=[u'[妻]'],negative=[u'[愛人]'])
for result in results:
    print(result)

positive='動物'
negative='野生'
results = model.most_similar(positive=['[' + positive + ']'],negative=['[' + negative + ']'])
for result in results:
    print(result)
