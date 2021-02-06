all:
	gcc -std=c99 -Wall -pedantic -o bfc bfc.c
	python3 main.py > out.bf
	./bfc out.bf
