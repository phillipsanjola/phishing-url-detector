My first python project, any feedback is appreciated.
This project looks at URLs from a dataset and extracts features from it that helps to determine whether the URL is phishing.
I used a dataset from Kaggle called PhiUSIIL Phishing URL Dataset with 235,795 rows.

Phishing indicators:
-URL length,
-Number of dots,
-Presence of '@' symbols,
-Whether it starts with https,
-Number of hyphens,
-Presence of a URL shortener,
-Presence of suspicious words, such as: login, verify, secure , update and confirm,
-Presence of suspicious TLDs (.xyz, .top, .club, .info).

Results:
-First 4 indicators: 92.37% accuracy
-All 8 features: 93.95%
-So first 4 features most important
-Most important feature is HTTPS presence, then URL length

How:
1. Created a function to identify features from each URL
2. Split the data into training (80%) and testing (20%) sets
3. Train a RandomForestClassifier on the training data
4. Evaluate the model's predictions against the test set

TO ADD: A user interface where you can type a URL and it will detect whether it is phishing.

Tech used: Python, pandas, scikit-learn
