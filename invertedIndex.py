import json


def main():
	error='======================================='
	test=open('test.json','r')
	forward_index=json.load(test);
	test.close()
	# inverted=open('invertedIndex.json','w')
	output_dict=dict()
for item in forward_index:
		if output_dict[item] is None:
			output_dict[item]=[forward_index[item][0],0,'h1']
		else:
			pass	# do nothing
		print(error)
		for each_word in forward_index[item][1].items()
			print(type(each_word))
		# print(error,'\n',item,'\n',error,'\n')



if __name__ == '__main__':
	main()
