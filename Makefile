hello:
	echo "Azure devops Makefile initiated"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120,W0105 hello.py

test:
	python3 -m pytest -vv test_hello.py

all: install lint test