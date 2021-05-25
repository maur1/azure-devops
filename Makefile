hello:
	echo "Azure devops Makefile initiated"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv click-ex/test_hello.py

all: hello install