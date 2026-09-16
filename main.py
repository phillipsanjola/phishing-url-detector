import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('Phishing_dataset.csv')

shorteners = ['bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly', 'is.gd']
suspicious_words = ['login', 'verify', 'secure', 'account', 'update', 'confirm']
suspicious_tld = ['.xyz', '.top', '.club', '.info']

#Signs of phishing url
def extract_features(url):
    length = len(url)
    num_dots = url.count('.')
    has_at = '@'in url
    is_https = url.startswith('https')
    num_hyphens = url.count('-')
    is_shortened = any(shortener in url for shortener in shorteners)
    tld_suspicious = any(tld in url for tld in suspicious_tld)
    words_suspicious = any(word in url for word in suspicious_words)
    return length, num_dots, has_at, is_https, num_hyphens, is_shortened, tld_suspicious, words_suspicious


result = df['URL'].apply(extract_features)
features_df = pd.DataFrame(result.tolist(), columns= ['length', 'num_dots', 'has_at', 'is_https', 'num_hyphens',
                                                      'is_shortened', 'tld_suspicious', 'words_suspicious'])

features_df['label'] = df['label']

x = features_df[['length', 'num_dots', 'has_at', 'is_https', 'num_hyphens',
                                                      'is_shortened', 'tld_suspicious', 'words_suspicious']]
y = features_df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2)

model = RandomForestClassifier()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

print(accuracy_score(y_test, predictions))

importance = model.feature_importances_
for name, score in zip(x.columns, importance):
    print(name, score)



















