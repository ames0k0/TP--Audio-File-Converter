# API TEST

#### APP
```bash
uv sync --no-dev
uv run python src/converter.py
```

#### CLI
```bash
uv sync --no-dev
uv run python src/cli.py -i samples/BAK.wav -o samples/BAK.mp3
```

#### TEST
```bash
uv sync --all-groups
uv run pytest tests
```

<p align="center"><img src="../../_readme/Diagram-WUI.drawio.png" /></p>
