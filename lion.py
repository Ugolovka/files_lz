import collections
import io

c = collections.defaultdict(int)

with io.open('lion.txt', encoding='utf-8') as f:
   for line in f:
       if len(line.strip()):
           for word in line.split(' '):
               c[word] += 1

with io.open('out.txt', 'w') as f:
    for word, count in c:
        f.write('{} {}\n'.format(word, count))