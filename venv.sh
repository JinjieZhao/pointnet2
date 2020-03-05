rm -rf $HOME/.venv/pointnet2
virtualenv $HOME/.venv/pointnet2
source $HOME/.venv/pointnet2/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
pip install "setuptools<39" -U
