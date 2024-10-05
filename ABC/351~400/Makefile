FILES = a.py b.py c.py d.py e.py f.py g.py

dir: create_directory create_files

create_directory:
	@if [ -z "$(name)" ]; then echo ""; exit 1; fi
	mkdir -p $(name)

create_files: create_directory
	@for file in $(FILES); do \
		touch $(name)/$$file; \
	done


run:
	@if [ -z "$(file)" ]; then echo ""; exit 1; fi
	python $(file).py < /Users/otsukanaoya/Desktop/programming/atcoder/input.txt
