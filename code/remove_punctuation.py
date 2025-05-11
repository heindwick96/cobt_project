import string

# Define punctuation and translation table
punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'
transtab = str.maketrans(dict.fromkeys(punct, ''))

# Remove punctuation from text
dataset['without stopwords'] = '|'.join(dataset['without stopwords'].tolist()).translate(transtab).split('|')
