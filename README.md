# SIGMA-PULSE

## Structure du projet

```
📁 ingestion/        # Collecte des données brutes (IOC, X/TG, finance)
📁 processing/       # Extraction IOC, NER, nettoyage
📁 correlation/      # Moteur de mise en relation des signaux
📁 scoring/          # Calcul du niveau de menace par signal
📁 playbooks/        # Actions à déclencher automatiquement
📁 reporting/        # Génération de rapports (Markdown, PDF)
📁 utils/            # Fonctions génériques, config
📄 main.py           # Orchestrateur global du pipeline
```

## Objectifs
- Ingestion multi-source (IOC, narratif, financier)
- Corrélation des signaux faibles
- Scoring de menace hybride
- Déclenchement de playbooks automatisés
- Génération de rapports enrichis pour analystes

## Lancement

```bash
python main.py
```
