# Rock Paper Scissors

A simple command-line Rock Paper Scissors game written in Python. Play against the computer in the terminal, round after round, until you decide to quit.

## Features

- Interactive terminal gameplay
- Input validation for player choices
- Random computer opponent
- Play again or exit after each round

## Requirements

- Python 3.8 or newer
- No third-party packages required (uses only the Python standard library)

## Getting Started

### Clone the repository

```bash
git clone https://github.com/zigiraplac/Rock_Paper_Scissors.git
cd Rock_Paper_Scissors
```

### Run the game

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```


## How to Play

1. Run `main.py`.
2. When prompted, enter one of: `rock`, `paper`, or `scissors`.
3. The computer makes a random choice.
4. The result is displayed: win, lose, or tie.
5. Choose whether to play again (`y`) or quit (`n`).

## Rules

| Choice   | Beats      |
|----------|------------|
| Rock     | Scissors   |
| Paper    | Rock       |
| Scissors | Paper      |

If both players choose the same option, the round is a tie.

## Example Session

```
Choose your option (rock, paper, scissors): rock
Computer chose: scissors
Player chose: rock
You win!
Do you want to play again? (y/n): n
Thanks for playing!
```

## License

This project is open source. Feel free to use and modify it.
