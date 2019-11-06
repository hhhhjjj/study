import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
for dist in get_installed_distributions():
    call("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade " + dist.project_name, shell=True)


# 这个库不要瞎更新，pywin32更新了反而不好使了，最后话要回退版本