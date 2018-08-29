from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer=RegexpTokenizer(r'\w+')

en_stop=get_stop_words('en')
p_stemmer=PorterStemmer()

doc1="blockchain reached a critical milestone in 2017 when it peaked on research firm Gartner’s closely-watched hype cycle, a ranking of fledgling technologies based on how the market perceives them and how far they are away from mainstream adoption. In bestowing this status on the technology, Gartner predicted that blockchain is still five to 10 years away from going mainstream,"
doc2="writing:Blockchain technologies are extremely hyped, evolving at different trajectories, but should not be ignored.To put that hype in perspective, a keyword search for the word “blockchain” on the major press release distribution services, PR Newswire and Business Wire, turns up a total of 1,970 press releases issued in the first three quarters of 2017."
doc_set=[doc1, doc2]
texts=[]

for i in doc_set:

    raw = i.lower()
    tokens=tokenizer.tokenize(raw)
    stopped_tokens=[i for i in tokens if not i in en_stop]
    stemmed_tokens=[p_stemmer.stem(i) for i in stopped_tokens]
    print(stemmed_tokens)
    texts.append(stemmed_tokens)

print (len(texts[0]))
dictionary=corpora.Dictionary(texts)
print (len(dictionary))
corpus=[dictionary.doc2bow(text) for text in texts]
print(corpus[0])

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=40)


print(ldamodel.print_topics(num_topics=2, num_words=7))
