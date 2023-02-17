import nbimporter
import my_mr_clean as eq
from my_mr_clean import*
from io import StringIO

muted_output = io.StringIO()
sys.stdout = muted_output

data = get_content("Ozone_layer")

merge_content = merge_contents(data)

collection = tokenize(merge_content)

collection = lower_collection(collection)

stop_words = ["the", "of", "and", "in", "to", "is", "most", "between", "a", "an", "by", "that", "where", "we", "if" "are", "was", "be", "from", "as", "about", "have", "at", "for", "this", "it", "are", "with", "these", "if", "has", "on", "which", "because", "into", "can", "over", "being", "were", "or", "an", "its", "other", "all", "out", "used", "also", "been", "near", "not", "alhough", "since", "less", "than", "while", "above", "so", "due", "could", "after", "per", "with", "until"] 
filtered_collection = remove_stop_words(collection, stop_words)

frequencies = count_frequency(filtered_collection)

data = print_most_frequent(frequencies, 20)

plot_bar_diagram_frequent_tokens(data)