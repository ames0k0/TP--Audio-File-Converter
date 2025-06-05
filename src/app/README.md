# API TEST

#### APP
```bash
uv sync --no-dev
uv run python afc.py
```

#### CLI
```bash
uv sync --no-dev
uv run python cli.py -i samples/BAK.wav -o samples/BAK.mp3
```

#### TEST
```bash
uv sync
uv run pytest test_afc.py
```

<p align="center"><img src="../../_readme/Diagram-WUI.drawio.png" /></p>
