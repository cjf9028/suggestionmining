import csv
import re
from nltk.tokenize import word_tokenize
import nltk
def word_classify_V1(sent_list):
    keywords = ["suggest", "recommend", "hopefully", "go for", "request", "it would be nice", "adding",
                "should come with", "should be able", "could come with", "i need", "we need", "needs", "would like to",
                "would love to", "allow", "add"]

    # Goldberg et al.
    pattern_strings = [r'.*would\slike.*if.*', r'.*i\swish.*', r'.*i\shope.*', r'.*i\swant.*', r'.*hopefully.*',
                       r".*if\sonly.*", r".*would\sbe\sbetter\sif.*", r".*should.*", r".*would\sthat.*",
                       r".*can't\sbelieve.*didn't.*", r".*don't\sbelieve.*didn't.*", r".*do\swant.*",
                       r".*i\scan\shas.*"]
    compiled_patterns = []
    for patt in pattern_strings:
        compiled_patterns.append(re.compile(patt))
    Index=[]
    label_list = []
    for sent in sent_list:
        tokenized_sent = word_tokenize(sent[1])
        tagged_sent = nltk.pos_tag(tokenized_sent)
        tags = [i[1] for i in tagged_sent]
        keyword_match = any(elem in keywords for elem in tokenized_sent)
        pos_match = any(elem in ['MD', 'VB'] for elem in tags)
        label=" "
        index=0
        if keyword_match == True:
            label = 1
            for x in range(len(tokenized_sent)):
                if tokenized_sent[x] in keywords:
                    label=tokenized_sent[x]
                    index = x
        elif pos_match == True:
            for x in range(0,len(tags)):
                if tags[x] in ['MD', 'VB']:
                    label=tokenized_sent[x]
                    index = x
        else:
            for x in range(0,len(tags)):
                if tags[x] in ['VBD', 'VBN','VBG','VBP','VBZ']:
                    label=tokenized_sent[x]
                    index = x
            if label == " ":
                for x in range(0,len(tags)):
                    if tags[x] in ['NN','NNP','NNG','NNS','WRB']:
                        label=tokenized_sent[x]
                        index=x
            if label == " ":
                label = "<PAD>"
                print(tags,tokenized_sent)
                index = -1
            if len(tags) !=len(tokenized_sent) or index>=len(tokenized_sent):
                print(tokenized_sent)
        Index.append(index)
        label_list.append(label)
    return label_list,Index
def word_classify_V3(sent_list):
    keywords = ["suggest", "recommend", "hopefully", "go for", "request", "it would be nice", "adding",
                "should come with", "should be able", "could come with", "i need", "we need", "needs", "would like to",
                "would love to", "allow", "add"]

    # Goldberg et al.
    pattern_strings = [r'.*would\slike.*if.*', r'.*i\swish.*', r'.*i\shope.*', r'.*i\swant.*', r'.*hopefully.*',
                       r".*if\sonly.*", r".*would\sbe\sbetter\sif.*", r".*should.*", r".*would\sthat.*",
                       r".*can't\sbelieve.*didn't.*", r".*don't\sbelieve.*didn't.*", r".*do\swant.*",
                       r".*i\scan\shas.*"]
    compiled_patterns = []
    for patt in pattern_strings:
        compiled_patterns.append(re.compile(patt))
    Index=[]
    label_list = []
    for sent in sent_list:
        tokenized_sent = word_tokenize(sent[1])
        tagged_sent = nltk.pos_tag(tokenized_sent)
        tags = [i[1] for i in tagged_sent]
        keyword_match = any(elem in keywords for elem in tokenized_sent)
        label=" "
        index=0
        if keyword_match == True:
            label = 1
            for x in range(len(tokenized_sent)):
                if tokenized_sent[x] in keywords:
                    label=tokenized_sent[x]
                    index = x
        else:
            for x in range(0,len(tags)):
                if tags[x] in ['VBD', 'VBN','VBG','VBP','VBZ']:
                    label=tokenized_sent[x]
                    index = x
            if label == " ":
                for x in range(0,len(tags)):
                    if tags[x] in ['NN','NNP','NNG','NNS','WRB']:
                        label=tokenized_sent[x]
                        index=x
            if label == " ":
                label = "<PAD>"
                print(tags,tokenized_sent)
                index = -1
            if len(tags) !=len(tokenized_sent) or index>=len(tokenized_sent):
                print(tokenized_sent)
        Index.append(index)
        label_list.append(label)
    return label_list,Index
def read_csv(data_path):
    file_reader = csv.reader(open(data_path,"rt",errors="ignore",encoding="utf-8"), delimiter=',')
    sent_list = []

    for row in file_reader:
        id = row[0]
        if "_" in id:
            id = id.split("_")[0]
        sent = row[1]
        sent = re.sub(r'[^0-9a-zA-Z ]+', '', re.sub(r'\s+', ' ', sent))
        suggestion=row[2]
        sent_list.append((id,sent,suggestion))
    return sent_list
'''
def read_csv_all(data_path):
    #__label__0 __label__0 __label__1 __label__1
    file_reader = csv.reader(open(data_path,"rt",errors="ignore",encoding="utf-8"), delimiter=',')
    sent_list = []

    for row in file_reader:
        id=0
        sentence = row[0]
        suggestion = row[1]
        sentence=sentence.replace("__label__0 __label__0","")
        sentence = sentence.replace("__label__1 __label__1", "")
        sentence = re.sub(r'[^0-9a-zA-Z ]+', '', re.sub(r'\s+', ' ', sentence ))

        sent_list.append((id,sentence ,suggestion))
    return sent_list
'''
def write_csv(sent_list, out_path):
    '''
    filewriter = csv.writer(open(out_path, "wb",errors="ignore",encoding="utf-8"), delimiter=',')
    filewriter.writerow("label, sentence")
    for (id, sent, label) in (sent_list):
        filewriter.writerow([label,sent])
    '''
    with open (out_path,"a",encoding="utf-8")as wf:
        writer=csv.writer(wf)
        writer.writerows("sentence, label")
        for (id, sent, label) in sent_list:
            raw=[sent,label]
            writer.writerows(raw)
def word_classify_V2(sent_list):
    # Goldberg et al.
    Index=[]
    label_list = []
    for sent in sent_list:
        tokenized_sent = word_tokenize(sent[1])
        tagged_sent = nltk.pos_tag(tokenized_sent)
        tags = [i[1] for i in tagged_sent]
        pos_match = any(elem in ['MD', 'VB'] for elem in tags)
        label=" "
        index=0
        if pos_match == True:
            for x in range(0,len(tags)):
                if tags[x] in ['MD', 'VB']:
                    label=tokenized_sent[x]
                    index = x
        else:
            for x in range(0, len(tags)):
                if tags[x] in ['VBD', 'VBN', 'VBG', 'VBP', 'VBZ']:
                    label = tokenized_sent[x]
                    index = x
            if label == " ":
                for x in range(0, len(tags)):
                    if tags[x] in ['NN', 'NNP', 'NNG', 'NNS', 'WRB']:
                        label = tokenized_sent[x]
                        index = x
            if label == " ":
                label = "<PAD>"
                index = -1
        Index.append(index)
        label_list.append(label)
    return label_list,Index
def write_file(sen,word_l,index,path):
    with open(path,"w") as wf:
        for x,word,ind in zip(sen,word_l,index):
            sentence = x[1]
            sentence = word_tokenize(sentence)
            if ind!=-1:
                sentence[ind] = "aspect_term"
                sentence = " ".join(sentence)
                label = x[2]
                if label == 1 or label =='1':
                    label = 'positive'
                else:
                    label = 'negative'
                try:
                    wf.write(sentence)
                    wf.write('\n')
                    wf.write(word)
                    wf.write('\n')
                    wf.write(label)
                    wf.write('\n')
                except:
                    print("error")
                    print(sentence)

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#k=read_csv("data/tmp.csv")
#t1,in1=(word_classify(k))
#write_file(k,t1,in1,"data/tmp.txt")
"""
k=read_csv("data/V1.4_Training.csv")
t1,t1_index=word_classify_V1(k)
write_file(k,t1,t1_index,"data/train.txt")

k=read_csv("data/SubtaskA_Trial_Test_Labeled.csv")
t1,t1_index=word_classify_V1(k)
write_file(k,t1,t1_index,"data/dev.txt")
"""
k=read_csv("data/SubtaskA_EvaluationData.csv")
t1,t1_index=word_classify_V1(k)
write_file(k,t1,t1_index,"data/test.txt")


#k=read_csv("data/SubtaskA_Test.csv")
#k=read_csv_all("data/alldata.csv")


#t1,t1_index=word_classify_count(k)
#write_file(k,t1,t1_index,"data/train.txt")
'''
k=read_csv("data/Training.csv")
la=len(k)

data_path=("data/train.csv")
t1,t1_index =word_classify(k[:int(la*0.7)])
write_file(k[:int(la*0.7)],t1,t1_index,"data/train.txt")

#data_path=("data/dev.csv")
t2, t2_index=word_classify(k[int(la*0.7):int(la*0.9)])
write_file(k[int(la*0.7):int(la*0.9)],t2,t2_index,"data/dev.txt")

#data_path=("data/test.csv")
t3,t3_index =word_classify(k[int(la*0.9):])
write_file(k[int(la*0.9):],t3,t3_index,"data/test.txt")
'''

'''
write_data_info(t1,t2,t3)
'''

'''
k=read_csv("data/Training.csv")
la=len(k)
data_path=("data/train.csv")
write_csv(k[:int(la*0.7)],data_path)
data_path=("data/dev.csv")
write_csv(k[int(la*0.7):int(la*0.9)],data_path)
data_path=("data/test.csv")
write_csv(k[int(la*0.9):],data_path)

data_p="data/Training.csv"
data = pd.read_csv(data_p)
X = data['sentence'].values.tolist()
Y = data['label'].values
print(Y)
'''