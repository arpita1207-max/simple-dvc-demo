create env

```bash
conda create -n wineq python=3.11.1 -y
```

activate env

```bash

conda activate env
```

created req file

install the req

```bash

pip install -r requirement.txt
```

```bash
download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
```

```bash
git init

```

```bash
dvc init
```

```bash
dvc add data_given/wine quality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

onliner updates

```bash
git add . && git commit -m "second commit"
```

```bash
git remote add origin https://github.com/arpita1207-max/simple-dvc-demo.git
git branch -M main
git push origin main
```

```bash
touch src/split_data.py
python  src/split_data.py
git add .
git commit -m "split data updated"
git push origin main
```

```bash
touch src/train_and_evaluate.py
python  src/train_and_evaluate.py
git add .
git commit -m "train and evluate updated"
git push origin main
```
