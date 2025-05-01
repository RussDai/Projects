# **Cricket Match Dataset Analysis: Test Nations (1877–2025):**

The dataset contains the complete history of international cricket matches played by all `Test-playing nations` from `1877 to 2025`, including `Afghanistan`, `Australia`, `Bangladesh`, `England`, `India`, `Ireland`, `New Zealand`, `Pakistan`, `South Africa`, `Sri Lanka`, `West Indies`, and `Zimbabwe`.

The dataset under analysis also includes `official ICC World XI matches` played against `Australia`, `Pakistan`, and `West Indies`, providing a more complete view of rare yet recognized international fixtures.

Match `results`, `margins`, `venues`, and `team performances` are covered across all formats. 

---------
--------
---
----

### **Data Engineering:**

1. **Initial Data Exploration:**

- **Load the dataset** – Understand structure, column names, and row count.
- **Check column data types** – Ensure types align with expected formats (e.g., dates, strings).
- **Inspect for null values** – Identify missing data to plan imputation or removal.
- **Find unique values per column** – Understand variety and categorical spread.
- **Check for duplicates** – Remove redundant records that could skew analysis.
- **Preview a few records** – Visually inspect data consistency.

2. **Data Cleaning:**
- **Handle missing values** – Fill, infer, or remove based on business logic and data distribution.
- **Fix inconsistent entries** – Standardize team names, venues, etc. (e.g., spacing, casing).
- **Convert ‘Match Date’ to datetime** – Enables time-based analysis and filtering.
- **Normalize string fields** – Trim whitespaces, unify cases (e.g., title case for teams).
- **Drop irrelevant columns** – If any columns are unnecessary for analysis (e.g., `Scorecard` as a link).

3. **Feature Engineering:**

- **Create ‘Match Year’ and ‘Month’** – For time-series or seasonal analysis.
- **Create ‘Is Neutral Ground’** – Compare ground with both team names to infer neutrality.
- **Extract Margin Type** – Separate win type (e.g., runs, wickets, innings) from margin string. 
- **Create binary outcome features** – Flags like `Is Draw`, `Is Tie`, `Is Win by Runs`, etc.
- **Create ‘Home Team’ and ‘Away Team’** – If derivable, based on venue and common patterns.
- **Add ‘Decade’ or ‘Era’ column** – Useful for historical trend analysis.

4. **Data Validation:**

- **Ensure winner is in team1 or team2 or is draw/tie** – Logical consistency check.
- **Validate margin format** – Confirm all margin values follow expected pattern (e.g., “100 runs”).
- **Ensure match format is consistent** – Should be “Test” throughout, else flag anomalies.

5. **Data Enrichment:**

- **Map countries to regions** – Group teams by regions like Asia, Europe, etc.
- **Add ranking/tier data** – If historical rankings available externally.
- **Incorporate match outcome context** – Series name, championship flags if data available.

---
---
---
---
##  **Data Analysis:**