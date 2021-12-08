class Swarm:

    def __init__(self, states):
        self.states = {n: 0 for n in range(9)}
        for n in states:
            self.states[n] += 1

    def update(self):
        for k in sorted(self.states):
            if k > 0:
                self.states[k - 1] += self.states[k]
            else:
                new6 = self.states[k]
                new8 = new6
            self.states[k] = 0
        self.states[6] += new6
        self.states[8] += new8

    def total(self):
        return(sum(self.states.values()))


def read_input(path):
    with open(path) as f:
        line = f.readline()
    return Swarm([int(d) for d in line.split(',')])


if __name__ == "__main__":
    path = 'input.txt'
    n = 80
    swarm = read_input(path)
    for _ in range(n):
        swarm.update()
    print("Day:", n, "Swarm:", swarm.total())
    n = 256
    swarm = read_input(path)
    for _ in range(n):
        swarm.update()
    print("Day:", n, "Swarm:", swarm.total())
