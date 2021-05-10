import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import io, base64
from django.db.models.functions import TruncDay
from matplotlib.ticker import LinearLocator

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec


class Figure():
    def __init__(self, test):
        self.test = test

    def primesfrom3to(self, n):
        """ Returns a array of primes, 3 <= p < n """
        sieve = np.ones(n//2, dtype=np.bool)
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i//2]:
                sieve[i*i//2::i] = False
        return 2*np.nonzero(sieve)[0][1::]+1


    def psd(self):
        prime = self.primesfrom3to(self.test)
        x = np.linspace(0.1, prime[-1:] * np.pi, 41)
        y = np.exp(np.sin(x))

        plt.clf()
        plt.stem(x, y, use_line_collection=True)
        flike = io.BytesIO()
        plt.savefig(flike)
        return base64.b64encode(flike.getvalue()).decode()
