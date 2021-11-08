git clone https://gitlab.cern.ch/cara/cara.git
cd cara
git lfs install
git lfs pull
pip install -e .
python -m cara.apps.calculator --theme=cara/apps/calculator/themes/cern
echo "CARA is now running at http://localhost:8080"