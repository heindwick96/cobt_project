import pandas as pd

# Define synonym dictionary
synonym_dict = {
    'sumber': 'pendapatan', 'income': 'pendapatan', 'perolehan': 'pendapatan',
    'inisiatif': 'inisiatif', 'program': 'inisiatif', 'projek': 'inisiatif',
    'usaha': 'usaha', 'cuba': 'usaha', 'ikhtiar': 'usaha',
    'cabaran': 'cabaran', 'halangan': 'cabaran', 'kesukaran': 'cabaran',
    'komuniti': 'komuniti', 'masyarakat': 'komuniti',
    'kerjasama': 'kerjasama', 'perkongsian': 'kerjasama',
    'keuntungan': 'keuntungan', 'manfaat': 'keuntungan',
    'maklum balas': 'maklum balas', 'ulasan': 'maklum balas',
    'promosi': 'promosi', 'pemasaran': 'pemasaran',
    'strategi': 'strategi', 'rancangan': 'rancangan', 'sasaran': 'sasaran'
}

# Replace words using the synonym dictionary
def replace_with_synonyms(text):
    words = text.split()
    return ' '.join([synonym_dict.get(word, word) for word in words])

dataset['improved'] = dataset['without stopwords'].apply(replace_with_synonyms)
