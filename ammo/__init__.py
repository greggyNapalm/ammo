# -*- coding: utf-8 -*-

import os

version_info = (0, 0, 6)
__version__ = ".".join(map(str, version_info))
__path = os.path.dirname(__file__)


class Mixer(object):
    '''Takes data chunks(requests) from sources, mix data in given proportion
    and yields chunks.
    Attributes:
        num_req: int, total requests needed. Not used if one of generators
        stops earlier.
    '''
    def __init__(self, num_req=10 ** 7):
        self.num_req = num_req
        self.gens = {}

    def add_generator(self, name, frequency, miner):
        '''Add one more data source to mix in.
        Args:
            name: str, name of data source(Helps to debug).
            frequency: float, percentil of source in result stream
            miner: generator obj, yelds requests.

        Returns:
            generator object, yield pids.
        '''
        assert isinstance(name, basestring)
        assert isinstance(frequency, float)

        self.gens[name] = {
            'frq': frequency,
            'miner': miner,
        }

    def __iter__(self):
        '''Iterate over generator till one of them ends(raises StopIteration).
        Returns:
            yields requetst from original generators in given proportion.
        '''

        if len(self.gens) < 1:
            raise ValueError('Have no generators to mix.')

        state = {}
        cntr = 0
        max_freq = max(g['frq'] for g in self.gens.values())
        for g_name, g_val in self.gens.iteritems():
            state[g_name] = {
                'proficit': 0,
                'ratio': g_val['frq'] / max_freq,
            }

        while True:
            for g_name, ctx in state.iteritems():
                if cntr >= self.num_req:
                    raise StopIteration('{} achieved'.format(self.num_req))
                ctx['proficit'] += ctx['ratio']
                if ctx['proficit'] >= 1:
                    for i in xrange(int(ctx['proficit'])):
                        ctx['proficit'] -= 1
                        cntr += 1
                        yield self.gens[g_name]['miner'].next()

        for each in self.__dict__.keys():
            yield self.__getattribute__(each)
