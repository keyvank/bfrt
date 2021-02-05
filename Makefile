all:
	gcc -std=c99 -Wall -pedantic -o bfc bfc.c
	./bfc main.bf
