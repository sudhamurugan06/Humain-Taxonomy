import sys
import csv as csv
from bs4 import BeautifulSoup
import os

def main():
    stop_w = get_words('words.csv')
    # if no filenames were given as input it would try to run on the default 'train.csv' and 'test.csv'
    if len(sys.argv)==1:
        preprocess_csv('train.csv',stop_w)
        preprocess_csv('test.csv',stop_w)
    # pre process any given filename in the command line input
    for arg in sys.argv[1:]:
        preprocess_csv(arg,stop_w)


def filter_common_words(text, stop_w):
    if isinstance(text, unicode):
        text = text.encode('utf8')
    # the following symbols will be replaced with white space
    symbols = [',','.',':',';','+','=','"','/']
    for symbol in symbols:
        text = text.replace(symbol,' ')
    output = ""
    for word in text.split():
        if not word.lower() in stop_w:
            output += word + ' '
    return output


def filter_html_tags(text):
    # the following tags and their content will be removed, for example <a> tag will remove any html links
    tags_to_filter = ['code','a']
    if isinstance(text, unicode):
        text = text.encode('utf8')
    soup = BeautifulSoup(text)
    for tag_to_filter in tags_to_filter:
        text_to_remove = soup.findAll(tag_to_filter)
        [tag.extract() for tag in text_to_remove]
    return soup.get_text()


def preprocess_csv(filename, word_set_to_filter=None):
    if word_set_to_filter is None:
        word_set_to_filter = set()
    print 'pre processing '+filename+'...'
    train_file_object = csv.reader(open('..'+os.path.sep+'csv'+os.path.sep+filename, 'rb'))
    header = train_file_object.next()
    preprocessed_file = csv.writer(open('..'+os.path.sep+'csv'+os.path.sep+'preprocess_'+filename, "wb"),quoting=csv.QUOTE_NONNUMERIC)
    preprocessed_file.writerow(header)
    # if the csv file is the test data
    if len(header)==3
        for row in train_file_object:
            preprocessed_file.writerow([int(row[0]), filter_common_words(row[1],word_set_to_filter), filter_common_words(filter_html_tags(row[2]),word_set_to_filter)])
    # if the csv file is the train data
    if len(header)==4:
        for row in train_file_object:
            preprocessed_file.writerow([int(row[0]), filter_common_words(row[1],word_set_to_filter), filter_common_words(filter_html_tags(row[2]),word_set_to_filter),row[3]])
    print 'finished'


def get_words(filename):
    english_words_file = csv.reader(open('..'+os.path.sep+'csv'+os.path.sep+filename, 'rb'))
    stop_w = set()
    for row in english_words_file:
        for word in row:
            stop_w.add(word.lower())
    return stop_w


if __name__ == '__main__':
    main()
