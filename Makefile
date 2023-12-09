
all: firmament

clean:
	rm -r firmament


firmament: main.c OpenSimplex2S.c
	clang -lm -o firmament main.c OpenSimplex2S.c

