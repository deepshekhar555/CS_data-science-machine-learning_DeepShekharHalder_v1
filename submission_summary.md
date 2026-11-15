# Project 1 — Predict Bike-Rental Demand Without Fooling Yourself

This project follows the CareerSwami brief closely and keeps the evaluation honest. The dataset is synthetic, reproducible, and built from a known rule. The main challenge is not to get a good-looking score at any cost, but to avoid data leakage and to compare every model against a real baseline.

## Workflow followed

1. Reproduce the synthetic dataset with a fixed seed.
2. Explore the time order and the obvious effects (weekday and rain).
3. Use a strict chronological split: train = days 1–120, validation = days 121–150, test = days 151–180.
4. Report a naive baseline before modelling.
5. Compare a lightweight honest model to that baseline.
6. Leave the test set untouched until the final evaluation.

## Honest results

- Baseline A (training mean): 23.81 validation MAE
- Baseline B (previous day): 12.33 validation MAE
- Candidate linear model: 7.60 validation MAE

## Methodological decisions

The model uses only information that would actually be known before the day starts. Same-day temperature and same-day rain were not used as features, because they are not available at prediction time and would create an impossible, leakage-prone model.

## Key files

- `analysis.py` — reproducible dataset and evaluation logic
- `data/bike_demand.csv` — generated synthetic dataset
- `templates/data-dictionary.csv` — definitions for each column
- `templates/baseline.csv` — naive baseline comparisons
- `templates/experiment-log.csv` — model comparison log
- `evidence-log.csv` — evidence trail for each claim
- `figures/exploration.png` — exploratory plots
- `bike_demand_analysis.ipynb` — notebook version of the project

## Final interpretation

The best honest comparison is against the previous-day baseline, and the candidate linear model beats it on validation. That is a valid result, but it is still only a validation result. The final test set remains untouched and should be used only once at the end, as required by the brief.
