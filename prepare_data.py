import csv
import sys
import ast
import transformers
from readability import Readability


path = sys.argv[1]

convs = []
with open(path, 'r') as f:
    csvFile = csv.reader(f)
    first = True
    for line in csvFile:
        if first:
            first = False
            continue
        conv = ast.literal_eval(line[1])
        conv = [c.strip() for c in conv]
        convs.append(conv)

out_path = sys.argv[2]
tokenizer = transformers.AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
sep = tokenizer.eos_token
with open(out_path, 'w') as f:
    csvwriter = csv.writer(f) 
    csvwriter.writerow(['context', 'target', 'score', 'grade_level'])
    for conv in convs:
        #inp = conv[0]
        #target = sep.join(convs[1:])
        for i in range(1,len(conv)):
            context = f' {sep} '.join(conv[:i])
            target = conv[i]
            r = Readability(target) 
            # import pdb; pdb.set_trace()
            score = r.flesch_kincaid()
            # f.write(f'"{context}", "{target}", "{score.grade_level}"\n')
            csvwriter.writerow([context, target, score.score, score.grade_level])


