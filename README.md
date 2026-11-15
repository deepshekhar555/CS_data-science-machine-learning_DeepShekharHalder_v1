Project 1 — Predict bike-rental demand without fooling yourself

This project models daily bike demand for a fictional mobility service. The objective is to forecast demand honestly using only information that would be known before the day begins. The main point is not to chase the best score at any cost; it is to avoid time leakage and report a sensible baseline.

Project flow:
1. Reproduce the synthetic dataset with the fixed seed.
2. Explore the time series and the weekday and rain effects.
3. Split the data chronologically: train days 1-120, validation days 121-150, test days 151-180.
4. Report a naive baseline before any modelling.
5. Compare a lightweight honest model against the baseline and leave the final test slice untouched until the end.

Key results:
- Baseline A (training mean): 23.81 validation MAE
- Baseline B (previous day): 12.33 validation MAE
- Candidate LinearRegression: 7.60 validation MAE

The project uses only features available before the day starts. Same-day temperature and same-day rain were intentionally excluded from the candidate model, which prevents the most common leakage mistake in time-series work.

Files to inspect:
- data/bike_demand.csv
- templates/data-dictionary.csv
- templates/baseline.csv
- templates/experiment-log.csv
- evidence-log.csv
- figures/exploration.png

AI assistance disclosure: the analysis was generated in Python, checked by rerunning the script, and no external or real-world customer data was used.
