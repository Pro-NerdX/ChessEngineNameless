## Requirements

> Note: This program has only been tested for **Python 3**

You need the [python-chess](https://github.com/niklasf/python-chess) library. You can install it via `pip` with:

```bash
pip install chess
```

or if you are on Arch-based systems:

```bash
python -m venv venv

source venv/bin/activate

pip install chess
```

> Note: If you're using the **fish shell**, you have to replace `activate` with `activate.fish`.

If you want to use the same `syzygy` endgame tablebases that I have used, run the following 2 commands in a terminal in the root of the project in order to download them from the urls in `urls_for_endgame_tablebases.txt`:
```bash
mkdir -p syzygy
wget -c -P syzygy -i urls_for_endgame_tablebases.txt
```
> Note: The commands might differ slightly depending on your operating system.

The engine uses `polyglot` opening books from the following [git repository](https://github.com/michaeldv/donna_opening_books). In order to clone them into your project, open a terminal in the root of your project and run:
```bash
git clone https://github.com/michaeldv/donna_opening_books.git
```

## Usage

To run the chess engine, just run:
```bash
python main.py
```
During the execution, you can feed it positions in **FEN** with the following format:
```bash
position fen <FEN str>
```
Replace `<FEN str>` with you FEN position. Use `quit` to exit the program gracefully.
