# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
import unittest
from collections import Counter

from ammo import Mixer


class MixerCase(unittest.TestCase):
    @staticmethod
    def debug_gen(sym, num=None):
        '''Simple string generator.
        '''
        cntr = 0
        while True:
            if num and cntr == num:
                raise StopIteration('Done.')
            yield '{}'.format(sym)
            cntr += 1

    def test_num_kwarg(self):
        m = Mixer(num_req=10)
        m.add_generator('test1', 50.0, self.debug_gen('a', num=10))
        m.add_generator('test2', 50.0, self.debug_gen('b', num=3))

        res = Counter()
        for r in m:
            res[r] += 1

        self.assertTrue(res['b'] == 3 and res['a'] == 4)

    def test_max_limit(self):
        m = Mixer(num_req=10)
        m.add_generator('test_a', 50.0, self.debug_gen('a', num=100))
        m.add_generator('test_b', 25.0, self.debug_gen('b'))
        m.add_generator('test_c', 25.0, self.debug_gen('c'))

        self.assertTrue(len([r for r in m]) == 10)

    def test_proportion(self):
        perc = lambda p, w: 100 * float(p) / float(w)
        m = Mixer(num_req=1000)
        input_data = {
            'a': ('test_a', 50.0, self.debug_gen('a')),
            'b': ('test_b', 22.5, self.debug_gen('b')),
            'c': ('test_c', 27.5, self.debug_gen('c')),
        }
        for struct in input_data.values():
            m.add_generator(*struct)

        res = Counter()
        for r in m:
            res[r] += 1

        total = sum(res.values())
        for char, num in res.iteritems():
            self.assertEqual(perc(num, total), input_data[char][1])
