import sys, csv, math

train_path = sys.argv[1]
test_path = sys.argv[2]

signals_text = sys.argv[3:]
contexts = []
targets = []
values = []
with open(train_path, 'r') as f:
    csvFile = csv.reader(f)
    first = True
    for line in csvFile:
        if first:
            first = False
            continue
        context, target, score, grad = line[:4]
        contexts.append(context)
        targets.append(target)
        values.append(float(grad))

min_val = min(values)
max_val = max(values)

# import pdb; pdb.set_trace()

num_sig = len(signals_text)
size_sig = int((max_val - min_val) / num_sig)
# start = [(min_val + (i+1) * size_sig) for i in range(num_sig-1)]
start = [0.0, 7.0]

with open(f'{train_path.replace(".csv","")}_ready.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["context", "target", "signal"])
    for context, target, value in zip(contexts, targets, values):
        # import pdb; pdb.set_trace()
        top = start[0]
        found = False
        for i, top in enumerate(start):
            if value < top:
                csvWriter.writerow([context, target, signals_text[i]])
                found = True
                break
        if not found:
            csvWriter.writerow([context, target, signals_text[-1]])


contexts = []
targets = []
values = []
with open(test_path, 'r') as f:
    csvFile = csv.reader(f)
    first = True
    for line in csvFile:
        if first:
            first = False
            continue
        context, target, score, grad = line[:4]
        contexts.append(context)
        targets.append(target)
        values.append(float(grad))

with open(f'{test_path.replace(".csv","")}_ready.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["context", "target", "signal"])
    for context, target, value in zip(contexts, targets, values):
        # import pdb; pdb.set_trace()
        top = start[0]
        found = False
        for i, top in enumerate(start):
            if value < top:
                csvWriter.writerow([context, target, signals_text[i]])
                found = True
                break
        if not found:
            csvWriter.writerow([context, target, signals_text[-1]])