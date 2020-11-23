
# enhancedcontainers 
![PYPI Version](https://img.shields.io/pypi/v/enhancedcontainers.svg) ![PYPI Downloads](https://img.shields.io/pypi/dw/enhancedcontainers?color=64b594) [![Views](https://api.ghprofile.me/view?username=sh-wayz-enhancedcontainers&color=51B780&label=views&style=flat)](https://ghprofile.me)
### Data structures improved built-in containers.

## Usage

### Stack
```py
import enhancedcontainers as ec

stack = ec.Stack()

stack.push('World!')
stack.push('Hello')

print(stack.pop())
print(stack.pop())

# Output:
Hello
World!
```
### Queue
```py
import enhancedcontainers as ec

queue = ec.Queue()

queue.enqueue('Hello')
queue.enqueue('World!')

print(queue.dequeue())
print(queue.dequeue())

# Output:
Hello
World!
```
### EnhancedList
```py
import enhancedcontainers as ec

elist = ec.EnhancedList()

print(elist.append('Hello'))
print(elist.append('World!'))

# Output:
Hello
World!
```
### EnhancedDict
```py
import enhancedcontainers as ec

edict = ec.EnhancedDict()

edict.hello = "Hello"
edict.world = "World!"
print(edict.hello)
print(edict.world)

# Output:
Hello
World!
```
## Install / Setup
### Manually:
- Clone the repository
```
git clone https://github.com/sh-wayz/enhancedcontainers.git
```
- cd into the directory
```
cd enhancedcontainers
```
- Run setup.py
```
python3 setup.py build install
```

### With pip:
```
python3 -m pip install enhancedcontainers
```


## Contribution
- Fork the repository
- Make your changes
- Submit a pull request

-------------------------------


