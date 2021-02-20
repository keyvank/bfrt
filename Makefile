all:
	python3 main.py > out.bf
	python3 bfc.py out.bf out.c
	python3 opt.py < out.c > outopt.c
	gcc -O1 outopt.c -o out
	./out > out.ppm
