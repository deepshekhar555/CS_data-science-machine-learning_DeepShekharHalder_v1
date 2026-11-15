# CareerSwami Project 1 — Submission Ready Guide

This project is ready to submit as a public link. The link should be viewable by anyone with the link, without login restrictions.

## Best submission option

Use a public link to one of the HTML files in this project folder:

- `index.html` — simple report
- `portfolio_case_study.html` — polished portfolio version
- `presentation.html` — slide-style deck

## Recommended opening page

Open `portfolio_case_study.html` first if you want a polished portfolio-style submission. It has the cleanest presentation for a reviewer.

## Short submission note to paste into the dashboard

"This project follows the CareerSwami brief by generating the synthetic bike demand dataset, keeping the split time-ordered, reporting honest baselines, and using only information available before the day starts. The project includes exploratory analysis, baseline comparisons, and a candidate linear model evaluated on validation data only."

## Optional shorter version

"Honest time-series forecasting project: generated synthetic bike demand data, kept the train/validation/test splits chronological, reported baseline A and baseline B, and compared a simple linear model using only pre-day information."

## Submission checklist

- [ ] Make sure the link is public
- [ ] Confirm the project page opens without login
- [ ] Check that the main file loads correctly
- [ ] Paste the public link into the dashboard
- [ ] Add the short note above
- [ ] Keep the final test set untouched in the analysis as required by the brief

## Files to include in the public folder

- `index.html`
- `portfolio_case_study.html`
- `presentation.html`
- `bike_demand_analysis.ipynb`
- `submission_summary.md`
- `README.md`
- `figures/exploration.png`
- `data/bike_demand.csv`
- `templates/` folder
- `evidence-log.csv`

## Final results summary

- Baseline A (training mean): 23.81 validation MAE
- Baseline B (previous day): 12.33 validation MAE
- Candidate LinearRegression: 7.60 validation MAE

This is the honest validation outcome, and it respects the project requirements by avoiding same-day leakage and leaving the final test period untouched until the end.
