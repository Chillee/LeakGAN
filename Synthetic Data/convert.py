import pickle
data_Name = "cotra"
vocab_file = "vocab_" + data_Name + ".pkl"

word, vocab = pickle.load(open('save/'+vocab_file, 'rb'), encoding='latin1')
print(len(word))
input_file = 'save/eval_file.txt'
output_file = 'speech/' + data_Name + '_' + input_file.split('_')[-1]
with open(input_file)as fin:
    for line in fin:
        #line.decode('utf-8')
        line = line.split()
        #line.pop()
        #line.pop()
        print(line)
        print(len(word))
        line = [int(x) for x in line if int(x) < len(word)]
        line = [word[x] for x in line]
        # if 'OTHERPAD' not in line:
        line = ' '.join(line) + '\n'
        print(line)
        # fout.write(line)#.encode('utf-8'))
