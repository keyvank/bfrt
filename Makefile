all:
	python3 main.py > out.bf
	python3 bfc.py out.bf out.c
	gcc -O3 out.c -o out
	./out
