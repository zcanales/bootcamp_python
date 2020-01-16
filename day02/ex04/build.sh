tar -cvf ai42-1.0.0.tar.gz ./logger ./setup.py
python setup.py sdist
pip install ./dist/ai42-1.0.0.tar.gz
