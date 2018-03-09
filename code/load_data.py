

import preprocessor as p

def get_data(lang):
    if lang== 'english':
        train_text_path = '../data/emoji_semeval_2k18_data/us_trial.text'
        train_label_path = '../data/emoji_semeval_2k18_data/us_trial_labels.labels'
        test_text_path = '../data/emoji_test_data/us_test.text'

        read_file = open(train_text_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [p.tokenize(text) for text in texts]
        train_data = texts

        read_file = open(test_text_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [p.tokenize(text) for text in texts]
        test_data = texts

        read_file = open(train_label_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [int(text) for text in texts]
        train_label = texts

    elif lang == 'spanish':
        train_text_path = '../data/emoji_semeval_2k18_data/es_trial.text'
        train_label_path = '../data/emoji_semeval_2k18_data/es_trial_labels.labels'
        test_text_path = '../data/emoji_test_data/es_test.text'

        read_file = open(train_text_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [p.tokenize(text) for text in texts]
        train_data = texts

        read_file = open(test_text_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [p.tokenize(text) for text in texts]
        test_data = texts

        read_file = open(train_label_path,'r+')
        texts = read_file.read().splitlines()
        read_file.close()
        texts = [int(text) for text in texts]
        train_label = texts

    else:
        print('enter the correct language')
    return train_data, train_label, test_data
