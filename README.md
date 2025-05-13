# Examen BentoML

## Clonage du repository
```bash  
git clone https://github.com/TustiWutsi/examen_bentoml.git
```

## Configuration de l'Environnement Virtuel
```bash
virtualenv bentoml-env
source bentoml-env/bin/activate
pip install -r requirements.txt
```

## Lancement du service
### En décompressant l'image Docker du Bento
```bash
docker load --input bento_image.tar
docker images
docker run --rm -p 3000:3000 lr_service:je4fwcrphgea56nh

# dans un autre terminal
source bentoml-env/bin/activate
python tests/quick_test_service.py
pytest tests/test_service.py
```

### En réentraînant le modèle et en l'enregistrant dans le Model Store de BentoML
```bash
python src/prepare_data.py
python src/train_model.py
bentoml serve src.service:lr_service --reload

# dans un autre terminal
source bentoml-env/bin/activate
python tests/quick_test_service.py
pytest tests/test_service.py
```
#### Et en créant un Bento conteneurisé
```bash
bentoml build
bentoml containerize lr_service:latest
docker images
docker run --rm -p 3000:3000 lr_service:<tag>

# dans un autre terminal
source bentoml-env/bin/activate
python tests/quick_test_service.py
pytest tests/test_service.py
```