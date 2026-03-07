##Plant Disease Detection by Alex Vuong and Samantha Sobhian

## Dataset Setup

This project uses a dataset that is automatically downloaded from Kaggle.

### 1. Clone the repository

```bash
git clone https://github.com/username/Planet-Disease-Detection.git
cd Planet-Disease-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Kaggle API credentials

Place your kaggle account and api in `kaggle.json` file in:

```
~/.kaggle/kaggle.json
```

and run:

```bash
chmod 600 ~/.kaggle/kaggle.json
```

### 4. Download the dataset

Run the dataset download script:

```bash
python download_dataset.py
```

This will automatically download and extract the dataset into the project directory.


Credit to emmarex for plantdisease dataset.