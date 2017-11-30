import pickle
data_Name = "cotra"
vocab_file = "vocab_" + data_Name + ".pkl"

word, vocab = pickle.load(open('save/'+vocab_file, 'rb'), encoding='latin1')
print(len(word))
input_file = 'save/generator_sample.txt'
output_file = 'speech/' + data_Name + '_' + input_file.split('_')[-1]
with open(output_file, 'w')as fout:
    with open(input_file)as fin:
        for line in fin:
            #line.decode('utf-8')
            line = line.split()
            #line.pop()
            #line.pop()
            line = [int(x) for x in line]
            line = [word[x] for x in line]
            # if 'OTHERPAD' not in line:
            line = ' '.join(line) + '\n'
            print(line)
            # fout.write(line)#.encode('utf-8'))
