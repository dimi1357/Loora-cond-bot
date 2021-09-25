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
sig_size = len(values) // num_sig
# start = [(min_val + (i+1) * size_sig) for i in range(num_sig-1)]
# values_sorted = sorted(values)
# thresholds = []
# for i in range(num_sig-1):
#     thresholds.append(values_sorted[sig_size*(i+1)])
# start = [0.0, 7.0]
# thresholds.append(10e8)
thresholds = [0.0, 7.0, 10e8]
print(thresholds)

with open(f'{train_path.replace(".csv","")}_ready.csv', 'w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["context", "target", "signal"])
    for context, target, value in zip(contexts, targets, values):
        # import pdb; pdb.set_trace()
        for i, top in enumerate(thresholds):
            if value < top:
                csvWriter.writerow([context, target, signals_text[i]])
                break


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
        for i, top in enumerate(thresholds):
            if value < top:
                csvWriter.writerow([context, target, signals_text[i]])
                break
