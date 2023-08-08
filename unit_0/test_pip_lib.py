import rich
from rich import print
from rich import pretty
pretty.install()        # <= Q: 这个有啥用

print(vars(rich))

print('世界是彩色的——')
print('⭐')

print({
    0: ['啊？', '这是', '真的吗'],
    '我去': object(),
})
