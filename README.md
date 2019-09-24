<h1 align="center">
    conways-game-of-life
</h1>

> An implementation of the Conway's Game of Life in python
<div align="center">
    <img src="assets/image.gif"/>
</div>
This repository is an implementation of the Conway's Game of Life in Python using pygame and numpy. I refactored the code so that it looks better but it still does not aims at being optimized so it runs at a poorly low framerate. 

## Table of Contents
- [What is the Conway's Game of Life?](##what-is-the-conway's-game-of-life)
- [Rules](##rules)
- [Requirements](##requirements)
- [Install](##install)
- [Contributing](##contributing)

## What is the Conway's Game of Life
The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970
The game is a zero-player game, meaning that its evolution is determined by its initial state. The only interaction with the game is by creating the initial configuration and observing how it evolves. If you are curious about it take a look at the [wikipedia article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Rules
* Any live cell with fewer than two live neighbors dies, as if by under population.
* Any live cell with two or three live neighbors lives on to the next generation.
* Any live cell with more than three live neighbors dies, as if by overpopulation.
* Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Requirements
* [Python](https://www.python.org/)

## Install
```
git clone https://github.com/TrAyZeN/conways-game-of-life.git
cd conways-game-of-life
pip install -r requirements.txt
```

## License
MIT TrAyZeN
