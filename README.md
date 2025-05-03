# Blackjack Simulation Repository

This repository contains Python files for simulating various blackjack strategies and gameplay experiences.

## play.py

### Overview

The `play.py` script is a blackjack simulator that allows users to either play blackjack manually or watch an automated play process.

### Features

- **Manual Play**: Users can play blackjack themselves, with the option to receive hints on recommended moves.
- **Automated Play**: Users can set the basic unit of bet for the bot to simulate automated gameplay.
- **Game Rules**: The simulator follows simplified blackjack rules:
  - No splitting, double down, or surrender.
  - Legal actions are limited to hit or stand.

### Recommendations

Basic blackjack moves are recommended based on online materials.

### Usage

To start the simulator, run:
```bash
python play.py
```

## doubledown.py

### Overview

The `doubledown.py` script performs a Monte Carlo simulation of the double down betting strategy, which is a variation of the famous Martingale betting strategy in blackjack.

### Features

- **Starting Bet**: Users can customize the starting bet as a portion of their initial balance.
- **Parameter Input**: Users can input different parameters when prompted, assuming they follow the specified ranges.
- **Hands Played**: The program loops through a variable number of hands (7 to 50), representing how many blackjack hands each gambler will play before leaving the table.
- **Earnings Recording**: Each gambler's earnings are recorded and averaged.
- **Top 20 Sharpe Ratios**: The simulation repeats with a batch of gamblers to find the top 20 Sharpe ratios, listing:
  - Number of hands played
  - Win rate (the chance of leaving the table with a profit)
  - Sharpe ratio

### Important Notes

- **Win Rate**: A win rate greater than 50% does not necessarily indicate a positive expected value (EV) or average return, as these are different mathematical concepts.
- **Graph Output**: Users can choose to output a graph comparing win rate versus Sharpe ratio at the end.
- **All-in Assumption**: Gamblers are assumed to go all-in if they lack sufficient funds for a unit bet.

### Usage

To start the simulator, run:
```bash
python doubledown.py
```

## oscargrind.py

### Overview

The `oscargrind.py` script performs a Monte Carlo simulation of a variation of the Oscar Grind betting strategy.

### Features

- **Parameter Input**: Users can input different parameters when prompted, assuming correct ranges as instructed.
- **Average Return**: The program outputs the average return of all gamblers and the win rate.
- **Win Rate**: Defined as the chance of leaving the table with a profit, similar to the other scripts.
- **Graph Output**: Users can choose to output a graph representing the profit and loss (PnL) of all gamblers across the number of hands played. The y-axis shows the PnL, while the x-axis shows the number of hands played and each single line representing one single gambler.

### Important Notes

- **Win Rate**: As with the other scripts, a win rate greater than 50% does not guarantee a positive expected value (EV) or average return.

### Usage

To start the simulator, run:
```bash
python oscargrind.py
```
