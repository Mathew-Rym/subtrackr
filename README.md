SubTrackr CLI 
Your personal subscription expense tracker


Quick Start

bash
1. Clone & setup
git clone https://github.com/Mathew-Rym/subtrackr.git
cd subtrackr
pipenv install

2. Initialize database
pipenv run python -c "from utils.db import init_db; init_db()"

3. Start tracking!
pipenv run python main.py --help


DBdiagram Link: https://dbdiagram.io/d/6834096fb9f7446da320998f

