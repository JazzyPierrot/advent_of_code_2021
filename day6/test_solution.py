import unittest
import solution as s


class TestSwarm(unittest.TestCase):

    def test_update(self):
        swarm = s.Swarm([3, 4, 3, 1, 2])
        swarm.update()
        self.assertEqual(swarm.states[2], 2)
        self.assertEqual(swarm.states[0], 1)
        swarm.update()
        self.assertEqual(swarm.states[1], 2)
        self.assertEqual(swarm.states[6], 1)
        self.assertEqual(swarm.states[8], 1)


if __name__ == "__main__":
    unittest.main()
