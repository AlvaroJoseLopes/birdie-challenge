test:
	python3 transform.py -i data/input.json -o data/output.json \
		-t delete:color set:number:three rename:pet:animal

test2:
	python3 transform.py -i data/example.json -o data/output2.json \
		-t delete:key_999995 set:key_100:three rename:key_999993:animal