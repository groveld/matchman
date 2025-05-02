# MatchManager

[Firebird Driver Documentation](https://firebird-driver.readthedocs.io/en/stable/index.html)

## TODO

- [ ] Add logging
- [ ] Add error handling
- [ ] Add tests
- [ ] Add documentation

## Setup

1. Clone and navigate to the repository

   ```bash
   git clone https://github.com/groveld/matchman.git
   cd matchman
   ```

2. Create a virtual environment

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: `.venv\Scripts\activate`
   python -m pip install --upgrade pip setuptools wheel
   ```

3. Install dependencies

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the application

   ```bash
   python ./matchman/app.py
   ```

5. Open your browser and go to `http://127.0.0.1:3000/`

## Steps to build a wheel

1. **Install Required Tools:** Ensure you have `setuptools` and `wheel` installed:

   ```bash
   python -m pip install --upgrade build
   ```

2. **Build the Wheel:** Run the following command in the terminal from the root of your project:

   ```bash
   python -m build
   ```

3. **Verify the Wheel:** The wheel file will be created in the `dist/` directory. You can install it locally to test:

   ```bash
   python -m pip install dist/matchman-0.1.0-py3-none-any.whl
   ```

   _add `--force-reinstall` to force reinstall the package for testing purposes._

## run in production

### Gunicorn

```bash
gunicorn --bind "0.0.0.0:8000" --workers 4 --threads 8 --worker-class gthread --timeout 120 matchman.cli:app
```
