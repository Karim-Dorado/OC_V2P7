# OC_V2P7

## Solving problems using algorithms with Python

### Description of application

This project consist to developp an application witch can choose the best combinaison of shares from a share list.

1. Every share is a dictionnary caracterized with the following keys:
    - name (str) -> name of the share
    - price (int or float) -> price of the share
    - profit (int or float) -> percentage of the profit generate by the share

2. You can run 3 apps:
    - brutforce.py: will generate the best combination from `data/brutforce.csv`
    - optimized.py: will use a greedy algorithm to generate a combination from `data/brutforce.csv`
    - main.py: will use a greedy algorithm to generate a combination from `data/dataset1.csv` and `data/dataset2.csv`

3. You can also use:
    - time_brut.py: will generate a graph which give us the execution time of the brutforce algorithm in function of the number of shares
    - time_opti.py: will generate a graph which give us the execution time of the optimized algorithm in function of the number of shares


### Setup
1. Create a folder and put all the files inside it.
2. Create a virtual environment - `python -m venv env`
3. Activate VirtualENV 
  - On Windows, run: `env\Scripts\activate.bat`
  - On Unix or MacOS, run: `source env/bin/activate`
5. Run requirements.txt - `pip install -r requirements.txt`
6. How to run the following Applications 
  - brutforce.py: `python brutforce.py`
  - optimized.py: `python optimized.py`
  - main.py: `python main.py`
