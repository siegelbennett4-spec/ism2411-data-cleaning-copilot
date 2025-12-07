Reflection on using GitHub Copilot for this assignment

What Copilot generated

I used Copilot to generate the initial implementations of several functions in `src/data_cleaning.py`, most notably `load_data`, `clean_column_names`, and `handle_missing_values`. I prompted Copilot by writing short comments above each function describing the intended behavior (e.g., "Load a CSV file into a pandas DataFrame"), then accepted and reviewed the suggestions.

What I modified

I changed Copilot's suggestions to match the project policy and simplify logic. For `load_data` I added a fallback to a different encoding and wrapped file reading in a try/except. For `clean_column_names` I simplified the normalization to `lower()` and underscore replacement. For `handle_missing_values` I replaced Copilot's multiple-fill strategies with a clear, consistent policy: drop rows missing a valid `price` (price is required) and fill missing `quantity` with `1` (assume single item). I also added `strip_text_fields` and `add_total_column` functions to make the pipeline clearer.

What I learned

Data cleaning requires clear, repeatable decisions: for example, deciding whether to drop or impute missing values depends on the column's meaning. Copilot is helpful for boilerplate and for suggesting common patterns, but it often offers multiple reasonable alternatives; it's the human's job to choose the correct policy. A specific example: Copilot suggested several ways to handle non-numeric `price` values; I chose to coerce to numeric and drop rows with invalid prices because price is required for revenue calculations.

Overall, Copilot sped up writing routine functions but I verified and adjusted logic to ensure the pipeline's decisions are explicit and documented in comments.
