import time

@profile
def funcao():
    total = 0
    for i in range(1000):
        total+=i
        time.sleep(0.001)
    return total

if __name__ == '__main__':
    funcao()
