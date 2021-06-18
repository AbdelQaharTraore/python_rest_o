"# python_rest_o"

RUN:
python -m venv myenv
pip install -r requirements.txt
uvicorn main:app --reload
