import pandas as pd
import nltk
from nltk.corpus import stopwords

# Download NLTK data (if not already downloaded)
nltk.download('stopwords')
nltk.download('punkt')

# Define custom stopwords (mostly Malay + numbers)
additional_stopwords = set([
    'dan', 'dalam', 'untuk', 'yang', 'ada', 'kepada', 'seperti', 'adalah', 'dengan', 'atau', 'ini', 'di',
    'ya', 'sabah', 'juga', 'oleh', 'akan', 'pada', 'dari', 'daripada', 'lain', 'melalui', 'lebih', 'kami', 'sangat',
    'masih', 'tidak', 'kurang', 'tiada', 'mereka', 'ialah', 'itu', 'kerana', 'ianya', 'lagi', 'mana',
    'terdapat', 'bagi', 'termasuk', 'boleh', 'harus', 'ia', 'sekitar', 'banyak', 'saya',
    'anda', 'kita', 'setiap', 'serta', 'sebuah', 'pelancongan', 'pelancong', 'ke', 'sentiasa', 'pengunjung',
    'produk', 'kawasan', 'baru', 'menawarkan', 'meningkatkan', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
])

# Combine with English stopwords
combined_stopwords = set(stopwords.words('english')).union(additional_stopwords)

# Remove stopwords
dataset['without stopwords'] = dataset['Community Engagement'].apply(
    lambda x: ' '.join([word for word in x.split() if word.lower() not in combined_stopwords])
)
