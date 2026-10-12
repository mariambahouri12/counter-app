# Image Alpine : très légère (~50 Mo contre ~1 Go pour python:3.12 complet)
FROM python:3.12-alpine

WORKDIR /app

# Utilisateur non-root (sécurité : limite les dégâts en cas de compromission)
RUN addgroup -S app && adduser -S app -G app

# Les dépendances d'abord : cette couche reste en cache tant que
# requirements.txt ne change pas (build beaucoup plus rapide)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Le code ensuite (change souvent, donc en dernier)
COPY app.py .

USER app
EXPOSE 5000

# CMD : commande exécutée au démarrage du conteneur
CMD ["python", "app.py"]
