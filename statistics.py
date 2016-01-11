import numpy as np
def process(node_num):
	f = open("../data/omnetpp.out")
	data = list()
	for line in f:
		line = line.strip().split("\t")
		data.append(line)
	l = len(data)
	key = ''
	i = 0
	good_array = np.zeros((1000,1000))
	sum_array = np.zeros((1000,1000))
	data_group = list()
	while i < l:
		data_tmp = data[i]
		i += 1
		if data_tmp != '' and data_tmp[3] != key:
			if key == '':
				key = data_tmp[3]
				data_group.append(data_tmp)
				continue
			key = data_tmp[3]
			l_tmp = len(data_group)
			node = list()
			for k in range(l_tmp):
				node_list = data_group[k][2].split('[')
				from_node = int(node_list[1].split(']')[0])
				to_node = int(node_list[2].split(']')[0])
				if k == 0:
					node.append(from_node)
					node.append(to_node)
				else:
					node.append(to_node)
			l_tmp = len(node)
			for j in range(l_tmp):
				for k in range(j+1,l_tmp):
					good_array[node[j]][node[k]] += 1
					sum_array[node[j]][node[k]] += 1
			if data_tmp[3] == 'bad':
				node_list = data_tmp[2].split('[')
				from_node = int(node_list[1].split(']')[0])
				to_node = int(node_list[2].split(']')[0])
				for j in range(l_tmp):
					sum_array[node[j]][to_node] += 1
			while data_tmp[3] == 'bad' and i < l:
				i += 1;
				data_tmp = data[i]
			data_group = list()
			data_group.append(data_tmp)
		else:
			data_group.append(data_tmp)
	for i in range(node_num):
		print i
		for j in range(node_num):
			print "%d\t%d\t%d" % (j,int(good_array[i][j]),int(sum_array[i][j]))
if __name__ == "__main__":
	node_num = int(raw_input())
	process(node_num)
