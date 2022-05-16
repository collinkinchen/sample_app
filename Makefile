export FLASK_APP=myproject
export FLASK_DEBUG=1
export FLASK_ENV=production

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt


run: venv/bin/activate
	./venv/bin/python3 -m flask run

clean:
	rm -rf myproject/__pycache__
	rm -rf venv

test:
	@echo $$FLASK_APP $$FLASK_DEBUG 