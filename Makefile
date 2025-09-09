.PHONY: all generate-cv clean open-cv
.DEFAULT_GOAL := all

ci: generate-cv clean
all: generate-cv clean open-cv

generate-cv:
	@echo "make/generate-cv: Generating CV PDF..."
	pdflatex -jobname=cv/Mert_Sismanoglu_CV cv.tex

clean:
	@echo "make/clean: Cleaning auxiliary files..."
	rm -f cv/*.aux cv/*.log cv/*.out

open-cv:
	@echo "make/open-cv: Opening CV PDF..."
	xdg-open cv/Mert_Sismanoglu_CV.pdf
