create env

```bash
conda create -n wineq python=3.11.1 -y
```

activate env

```bash

conda activate env
```

created req file

install thr req

```bash

pip install -r requirement.txt
```

download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init

dvc init

dvc add data_given/wine quality.csv

git add .

git commit -m "first commit"
