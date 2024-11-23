# N-puzzle

This repository contains my work for the Lab 3 of the computational intelligence courses on the [N-puzzle](https://en.wikipedia.org/wiki/15_puzzle).

## Notebook

The [n-puzzle.ipnyb](./n-puzzle.ipynb) file contains my reflexion about the problem. How I end up step by step with this solution.

## Code

The [n-puzzle-a-star.py](./n-puzzle-a-star.py) file contains the code of my A* algorithm.

The [n-puzzle-gbf.py](./n-puzzle-gbf.py) file contains the code of my Gready Best First algorithm.

### Run
#### Poetry

If you have [Poetry](https://python-poetry.org/) installed on your pc, you can run the file with the following commands :

```shell
cd CI2024_LAB3 # Go to the directory
```

```shell
poetry install # Install dependencies
```

```shell
poetry shell # Start a shell in the virtual environment
```

```shell
python n-puzzle-a-star.py

# Run the program (one of the two)

python n-puzzle-gbf.py
```

#### Others

Otherwise, you can just run the script from scratch.

```shell
cd CI2024_LAB3 # Go to the directory
```

```shell
pip install ... # Install dependencies one by one
```

```shell
python n-puzzle-a-star.py

# Run the program (one of the two)

python n-puzzle-gbf.py
```