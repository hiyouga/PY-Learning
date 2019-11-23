import numpy as np
import json

with open('docs.json', 'r') as f:
    docs = json.loads(f.read())
    f.close()

link_dict = {}
ind2link = []
link_num = 0

for k in docs.keys():
    if k not in ind2link:
        link_dict[k] = link_num
        ind2link.append(k)
        link_num += 1

for v in docs.values():
    for ck in v.keys():
        if ck not in ind2link:
            link_dict[ck] = link_num
            ind2link.append(ck)
            link_num += 1

markov = np.zeros((link_num, link_num))

for k, v in docs.items():
    for ck, cv in v.items():
        markov[link_dict[k]][link_dict[ck]] += cv

for i in range(link_num):
    if np.sum(markov[i]) == 0:
        markov[i] += 1.0 / link_num
    else:
        markov[i] /= np.sum(markov[i])

alpha, eps = 0.85, 1e-15
K = 400

trans_mat = alpha * np.transpose(markov) + (1-alpha) / link_num
P_old = np.zeros((link_num))
P_old[0] = 1
P = np.matmul(trans_mat, P_old)

while np.linalg.norm(P - P_old) > eps:
    P_old = P
    P = np.matmul(trans_mat, P_old)

solution = []
for i in range(link_num):
    if '.shtml' in ind2link[i] and 'gaotan' not in ind2link[i]:
        solution.append((P[i], ind2link[i]))
solution.sort(reverse = True)

out_dict = {}
for v, l in solution[0:K]:
    out_dict[l] = v
with open('pagerank.json', 'w') as f:
    f.write(json.dumps(out_dict, sort_keys = False, indent=4))
    f.close()

print('Completed!')