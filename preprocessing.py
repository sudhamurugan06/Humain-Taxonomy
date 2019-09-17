import re
import nltk
import six
import bs4
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
def remove_tags(text):
    tags_to_filter = ['code', 'a']
    if isinstance(text, six.string_types):
        text = text.encode('utf8')
    soup = BeautifulSoup(text, features='lxml')
    for tag_to_filter in tags_to_filter:
        text_to_remove = soup.findAll(tag_to_filter)
        [tag.extract() for tag in text_to_remove]
    return soup.get_text()

def rem_body_space(text):
    text = re.sub("\'", "", text)
    text = re.sub("[^a-zA-Z]", " ", text)
    text = ' '.join(text.split())
    text = text.lower()
    return text

def freq_words(x, terms=30):
    all_words = [text for text in x]
    fdist = nltk.FreqDist(all_words)
    words_df = pd.DataFrame({'word': list(fdist.keys()), 'count': list(fdist.values())})
    d = words_df.nlargest(columns="count", n=terms)


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    no_stopwords_text = [w for w in text.split() if not w in stop_words]
    return ' '.join(no_stopwords_text)
