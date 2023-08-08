import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

if device == 'cuda':
    print('哦牛逼，你有显卡')
else:
    print('没关系，没 cuda 也可以用命换')

print()


x = torch.rand([16, 3, 512, 512]).to(device)

print('[tensor]')
print('x.device:', x.device)
print('x.dtype:', x.dtype)
print('x.shape:', x.shape)

print()


def loss_fn(x):
    return (x ** 2).mean()

x.requires_grad = True
loss = loss_fn(x)

print('[loss]')
print('loss.shape', loss.shape)
print('loss', loss)
assert loss.grad_fn, 'loss 应该有梯度的哼哼啊啊啊啊啊啊'
