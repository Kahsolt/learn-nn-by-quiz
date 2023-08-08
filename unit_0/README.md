# Unit - 0

    setup toolchain

----

### 代码编辑器

首先我们需要一个好用的代码编辑器，我推荐微软的 [VSCode](https://code.visualstudio.com/)，它是一个开源、配置高度可定制、轻量化跨平台的代码编辑器：

> Task 1: 安装 vscode

而从猴子进化成人类则主要得益于插件的广泛使用：

> Task 2: 安装下列 vscode 插件 

- Python
- IntelliCode
- Markdown Preview Enhanced
- JetBrains IDE Keymap

> Q1: 看看它们的文档，都是干啥用的


### 开发语言

然后我们需要安装开发语言 [Python](https://www.python.org/) 的运行环境，但我们并不安装官方的发行版 —— 因为它太裸了，不好用 —— 我们选择更好用的集成包 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ，它是一个基于包管理器 conda 构建的最小化 Python 环境。

> Task 3: 安装 miniconda

> Q2: 什么叫 "包管理器" ，浅要了解 conda 和 pip 的关系，为何用 pip 安装第三方包比 conda 快
> Q3: 什么是 "第三方包"，PyPI: [https://pypi.org/](https://pypi.org/) 是个什么网站

为了让控制台小黑窗变得更好看好用，我们需要整点啥来着？

> Task 4: 用 pip 安装下列第三方 python 包；运行并通过测试脚本 test_pip_lib.py

- [pyreadline](https://github.com/pyreadline/pyreadline)
- [rich](https://github.com/Textualize/rich)

> Q4: 看看它们的项目主页，又是干啥用的

在安装一些体积很大的库比如 pytorch 的时候，从外国原始站点下载可能会很慢，好在开源项目在全球有着比较广阔的镜像分发站点，通常由高校和企业支撑。

> Task 5: 换源，配置 pip 默认使用国内源

你有很多选择，但我推荐金枪鱼：

- [https://zhuanlan.zhihu.com/p/191065264](https://zhuanlan.zhihu.com/p/191065264)
- [https://mirror.tuna.tsinghua.edu.cn/](https://mirror.tuna.tsinghua.edu.cn/)


### python 虚拟环境

我们 [为什么需要虚拟环境？](https://www.jianshu.com/p/b49d13d3c8f2)  
哦孩子，那肯定是因为现实在某些意义、某个方面、某种程度上重创过我们 😥……

> Task 6: 用 conda 创建名为 quiz 的虚拟环境，固定版本 python==3.10.0

练习一下进入和退出一个虚拟环境，以后会经常用到，别忘了！  

主环境和创建的虚拟环境所使用的 python 解释器在磁盘上是两个不同的文件，为了避免搞混，我们有必要检查一下。使用命令 `where python.exe` 可以列出当前运行环境所能找到的 python 解释器，第一个就是我们将实际运行的。  

> Task 7: 用 where 命令查看一下进入和退出虚拟环境后实际所用 python 解释器的路径，它们应该是不同的


### 神经网络计算框架 pytorch

现在，终于可以安装 [PyTorch](https://pytorch.org/get-started/locally/) 了 🎉  
⚠ **记得一定要在虚拟环境 quiz 中安装哦**  

> Task 8: 用 pip 安装最新版 pytorch ；如果你有cuda显卡，选择 CUDA 版本，否则选择 CPU 版本

> Q5: 对比 [Tensor 类的 API 列表](https://pytorch.org/docs/stable/torch.html#tensors) 和 numpy 的 [ndarray 类的 API 列表](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)，感觉一下它们能用来干什么；这两个框架有什么目的意义上的区别

运行脚本 test_torch.py


### 矩阵是一种低阶张量

那么 [Tensor](https://pytorch.org/docs/stable/torch.html#tensors) 类当然可以用来做一些简单的矩阵计算

> Task 9: 编写代码，运行并通过测试 test_matrix.py


----
by Armit
2023/08/08
