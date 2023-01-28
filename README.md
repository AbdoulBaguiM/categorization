# Classifying Text with Elasticsearch: A No-ML Approach

This project provides a script for indexing text documents in Elasticsearch using the \_bulk method, without the use of machine learning. The documents are organized by category and are contained in a folder named "bbc" in the current directory. The "bbc" folder referenced in this code is based on the dataset used in the paper "Practical Solutions to the Problem of Diagonal Dominance in Kernel Document Clustering" by D. Greene and P. Cunningham. This dataset, which was published in the Proceedings of ICML 2006, consists of text documents organized by category.

## Requirements

- Python 3
- Elasticsearch

## Usage

Clone the repository

    git clone https://github.com/AbdoulBaguiM/categorization.git

Make sure to have the "bbc" folder containing your text documents, organized by category in the current directory

Run the script

    python classify.py

The response from Elasticsearch will be printed to the console for debugging purposes.

## Note

Make sure Elasticsearch is running on your localhost and the default port is 9200 before running the script.

## License

This project is licensed under the MIT License.

## Contributing

If you want to contribute to this project, please open an issue or a pull request.
