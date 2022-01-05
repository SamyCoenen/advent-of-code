import collections
list_of_sweeps = []
file_with_sweeps = 'day-1-input'
with open(file_with_sweeps) as f:
    list_of_sweeps = f.read().splitlines()

print(f'Total sweeps is {len(list_of_sweeps)}')

count_increases = 0
previous_sweep = 0

previous_sweeps = collections.deque(maxlen=3)

for sweep in list_of_sweeps:
    if len(previous_sweeps) < 3:
        previous_sweeps.append(int(sweep))
        continue
    total_sweep_collection_a = sum(previous_sweeps)
    previous_sweeps.append(int(sweep))
    total_sweep_collection_b = sum(previous_sweeps)
    print(f'total a: {total_sweep_collection_a}, total b: {total_sweep_collection_b}')
    if total_sweep_collection_b > total_sweep_collection_a and len(previous_sweeps) != 1:
        count_increases +=1
        print(f'Increased by 1')
    

print(f'Total increases: {count_increases}')
