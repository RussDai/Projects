# **Cricket Match Dataset Analysis: Test Nations (1877–2025):**

The dataset contains the complete history of international cricket matches played by all `Test-playing nations` from `1877 to 2025`, including `Afghanistan`, `Australia`, `Bangladesh`, `England`, `India`, `Ireland`, `New Zealand`, `Pakistan`, `South Africa`, `Sri Lanka`, `West Indies`, and `Zimbabwe`.

The dataset under analysis also includes `official ICC World XI matches` played against `Australia`, `Pakistan`, and `West Indies`, providing a more complete view of rare yet recognized international fixtures.

Match `results`, `margins`, `venues`, and `team performances` are covered across all formats. 

---------
--------
---
----

# **Data Engineering:**

1. **`Initial Data Exploration`:**

- **Load the dataset**
- **Check column data types** 
- **Inspect for null values** 
- **Find unique values per column** 
- **Check for duplicates** 
- **Preview a few records** 

2. **`Data Cleaning`:**
- **Handle missing values** 
- **Fix inconsistent entries**
- **Convert ‘Match Date’ to datetime** 
- **Normalize string fields** 
- **Drop irrelevant columns** 

3. **`Feature Engineering`:**

- **Create ‘Match Year’ and ‘Month’**
- **Create ‘Is Neutral Ground’** 
- **Extract Margin Type**  
- **Create binary outcome features** 
- **Create ‘Home Team’ and ‘Away Team’** 
- **Add ‘Decade’ or ‘Era’ column** 

4. **`Data Validation`:**

- **Ensure winner is in team1 or team2 or is draw/tie** 
- **Validate margin format** 
- **Ensure match format is consistent** 

5. **`Data Enrichment`:**

- **Map countries to regions** 
- **Add ranking/tier data** 
- **Incorporate match outcome context** 

---
---
---
---
#  **Data Analysis:**

### **A. General Dataset Overview:**

1. **Match Count by Format:**
   - **How to**: Group by `format`.
   - **Conclusion**: Understand which format is most played.
   - **To Decision Makers**: Resource allocation per format.
   - **Visual**: Pie chart or bar chart.

2. **Match Count Over Time:**
   - **How to**: Use `year` or `year_month`.
   - **Conclusion**: Detect rising or falling trends.
   - **To Decision Makers**: Investment in formats over time.
   - **Visual**: Line chart.

3. **Growth of T20Is & ODIs:**
   - **How to**: Filter by `format`, use `start_date`.
   - **Conclusion**: Short formats’ rise in modern era.
   - **To Decision Makers**: Marketing focus on fast-paced formats.
   - **Visual**: Area chart over time.

### **B. Geography-Based Exploration:**

4. **Top Host Countries:**
   - **How to**: Group by `ground_country`.
   - **Conclusion**: Identify major cricket-hosting nations.
   - **To Decision Makers**: Target venues for events.
   - **Visual**: Horizontal bar chart.

5. **Neutral Ground Matches:**
   - **How to**: Filter `is_neutral_ground == True`.
   - **Conclusion**: Usage of neutral venues.
   - **To Decision Makers**: Decision on neutral ground policies.
   - **Visual**: Stacked bar by `format`.

6. **Grounds with Highest Win Margins:**
   - **How to**: Group by `ground`, get max `won_by_runs`.
   - **Conclusion**: Bias of pitches (batting-friendly or not).
   - **To Decision Makers**: Pitch regulation.
   - **Visual**: Box plot per ground.

### **C. Team Performance & Rivalry:**

7. **Most Successful Teams:**
   - **How to**: Count `winner`.
   - **Conclusion**: Historical dominance.
   - **To Decision Makers**: Strengthen underdogs, fund grassroots.
   - **Visual**: Bar chart.

8. **Head-to-Head Results:**
   - **How to**: Group by `team_1`, `team_2`, `winner`.
   - **Conclusion**: Key rivalries and dominance.
   - **To Decision Makers**: Marketing around rivalries.
   - **Visual**: Heatmap or matrix.

9. **Performance in Neutral Venues:**
   - **How to**: Filter `is_neutral_ground`, analyze `winner`.
   - **Conclusion**: Performance away from home conditions.
   - **To Decision Makers**: Strategy for ICC tournaments.
   - **Visual**: Grouped bar chart.

10. **Team Dominance by Format:**
    - **How to**: Cross `winner` with `format`.
    - **Conclusion**: Teams’ strengths across formats.
    - **To Decision Makers**: Format-specific team preparation.
    - **Visual**: Faceted bar plots.

### **D. Victory Margin Analysis:**

11. **Distribution of Runs-Based Wins:**
    - **How to**: Analyze `won_by_runs`.
    - **Conclusion**: Magnitude of dominance.
    - **To Decision Makers**: Pitch balance check.
    - **Visual**: Histogram or violin plot.

12. **Distribution of Wickets-Based Wins:**
    - **How to**: Use `won_by_wickets`.
    - **Conclusion**: Ease of chasing.
    - **To Decision Makers**: Batting order strategies.
    - **Visual**: Box plot.

13. **Innings Victory Frequency:**
    - **How to**: Count `won_by_inns`.
    - **Conclusion**: One-sidedness of matches.
    - **To Decision Makers**: League balance.
    - **Visual**: Bar chart over years.

14. **Top 10 Biggest Wins in History:**
    - **How to**: Sort `won_by_runs` or `won_by_inns`.
    - **Conclusion**: Historical milestones.
    - **To Decision Makers**: Historical storytelling, PR.
    - **Visual**: Highlighted table or infographics.

### **E. Match Duration Trends:**

15. **Average Match Duration by Format:**
    - **How to**: Group by `format`.
    - **Conclusion**: Attention span required per format.
    - **To Decision Makers**: TV scheduling, viewership planning.
    - **Visual**: Line or bar chart.

16. **Long Matches Over the Years:**
    - **How to**: Analyze top 10 longest matches.
    - **Conclusion**: Historical battles.
    - **To Decision Makers**: Spectacle opportunities.
    - **Visual**: Timeline plot.

### **F. Score Analysis:**

17. **Total Runs Distribution:**
    - **How to**: Combine scores (`test_score`, etc.).
    - **Conclusion**: Scoring patterns per format.
    - **To Decision Makers**: Rule adjustments.
    - **Visual**: KDE plots by format.

18. **High-Scoring Grounds:**
    - **How to**: Group by `ground`, avg score.
    - **Conclusion**: Batting vs bowling pitch.
    - **To Decision Makers**: Match scheduling.
    - **Visual**: Bar chart.

### **G. Time-Based Patterns:**

19. **Matches Per Month:**
    - **How to**: Use `month`.
    - **Conclusion**: Seasonal popularity.
    - **To Decision Makers**: Plan tours in cricket-heavy months.
    - **Visual**: Calendar heatmap.

20. **Decade-Wise Team Wins:**
    - **How to**: Bucket `year`.
    - **Conclusion**: Historical legacy.
    - **To Decision Makers**: Celebrate team eras.
    - **Visual**: Line or stacked area chart.

21. **Dominant Team Per Year:**
    - **How to**: Find yearly `winner` mode.
    - **Conclusion**: Changing leadership.
    - **To Decision Makers**: Strategic support cycle.
    - **Visual**: Slopegraph.

### **H. Competitive Balance:**

22. **Close Matches Frequency:**
    - **How to**: Small `won_by_runs` and `won_by_wickets`.
    - **Conclusion**: How competitive matches are.
    - **To Decision Makers**: Tournament excitement.
    - **Visual**: Count chart by margin bin.

23. **Innings Wins Over Time:**
    - **How to**: Analyze `won_by_inns` count yearly.
    - **Conclusion**: Growing gap or balance?
    - **To Decision Makers**: Talent development.
    - **Visual**: Line graph.

24. **Win Margins by Team:**
    - **How to**: Avg margin by winner.
    - **Conclusion**: Dominant or scrape wins.
    - **To Decision Makers**: Match strategies.
    - **Visual**: Strip plots.

### **I. Format-Specific Insights:**

25. **Win Trends in Test vs T20:**
    - **How to**: Group by `format` and `winner`.
    - **Conclusion**: Format dominance.
    - **To Decision Makers**: Format-specific team investment.
    - **Visual**: Clustered bars.

26. **Chasing vs Defending Success:**
    - **How to**: Create proxy if available via `margin` pattern.
    - **Conclusion**: Format-based chase difficulty.
    - **To Decision Makers**: Team composition strategies.
    - **Visual**: Split bar charts.

### **J. Other Interesting Analyses:**

27. **Matches Involving Associate Nations:**
    - **How to**: If team includes newer/less frequent names.
    - **Conclusion**: Growth of global cricket.
    - **To Decision Makers**: Support emerging teams.
    - **Visual**: Highlighted bar chart.

28. **Team Success Away vs Home:**
    - **How to**: Use `is_neutral_ground`.
    - **Conclusion**: Home advantage bias.
    - **To Decision Makers**: Ground allocations.
    - **Visual**: Side-by-side bar chart.

29. **Top 10 Grounds by Match Count:**
    - **How to**: Group by `ground`.
    - **Conclusion**: Venue reliability.
    - **To Decision Makers**: Infrastructure focus.
    - **Visual**: Dot plot.

30. **Most Frequent Matchups:**
    - **How to**: Count pair frequency `team_1` + `team_2`.
    - **Conclusion**: Popular rivalries.
    - **To Decision Makers**: Schedule high-interest matches.
    - **Visual**: Chord diagram.

31. **Upset Detection (Underdog Wins):**
    - **How to**: Use domain knowledge/rankings.
    - **Conclusion**: Cinderella stories.
    - **To Decision Makers**: Value unpredictability.
    - **Visual**: Highlight plots.

32. **Venue Win Bias:**
    - **How to**: % wins by home team at each `ground`.
    - **Conclusion**: Is ground biased?
    - **To Decision Makers**: Neutrality analysis.
    - **Visual**: Gradient map.

33. **First vs Second Team Win Rate:**
    - **How to**: Compare `winner` with `team_1`/`team_2`.
    - **Conclusion**: Advantage of toss or order.
    - **To Decision Makers**: Toss policies.
    - **Visual**: Split donut chart.

34. **Win Type Distribution by Format:**
    - **How to**: Compare `won_by_runs`, `won_by_wickets`, `won_by_inns`.
    - **Conclusion**: Format-specific outcomes.
    - **To Decision Makers**: Game structure review.
    - **Visual**: Treemap.

35. **Country-wise Format Hosting Pattern:**
    - **How to**: `ground_country` + `format`.
    - **Conclusion**: Which countries host which formats more.
    - **To Decision Makers**: Global format planning.
    - **Visual**: Grouped stacked bars.
