{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5135aaf3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Final Project 10.16 SEPT 27 2022  Ramon Torres "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "44d97dc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "052ce6a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "53484b9e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "c = lambda f: 5 / 9 * (f - 32)\n",
    "\n",
    "temps = [(f, c(f)) for f in range (0, 101, 10)]\n",
    "\n",
    "temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celcius'])\n",
    "\n",
    "axes = temps_df.plot(x='Fahrenheit', y='Celcius', style='.-')\n",
    "\n",
    "y_label = axes.set_ylabel('Celcius')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "8b53f544",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ratorres\n"
     ]
    }
   ],
   "source": [
    "cd C:\\Users\\ratorres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "8ac94fde",
   "metadata": {},
   "outputs": [],
   "source": [
    "nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "2542fa3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Value</th>\n",
       "      <th>Anomaly</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>189501</td>\n",
       "      <td>34.2</td>\n",
       "      <td>-3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>189601</td>\n",
       "      <td>34.7</td>\n",
       "      <td>-2.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>189701</td>\n",
       "      <td>35.5</td>\n",
       "      <td>-1.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>189801</td>\n",
       "      <td>39.6</td>\n",
       "      <td>2.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>189901</td>\n",
       "      <td>36.4</td>\n",
       "      <td>-1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Value  Anomaly\n",
       "0  189501   34.2     -3.2\n",
       "1  189601   34.7     -2.7\n",
       "2  189701   35.5     -1.9\n",
       "3  189801   39.6      2.2\n",
       "4  189901   36.4     -1.0"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "24389add",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Value</th>\n",
       "      <th>Anomaly</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>119</th>\n",
       "      <td>201401</td>\n",
       "      <td>35.5</td>\n",
       "      <td>-1.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>201501</td>\n",
       "      <td>36.1</td>\n",
       "      <td>-1.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>201601</td>\n",
       "      <td>40.8</td>\n",
       "      <td>3.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122</th>\n",
       "      <td>201701</td>\n",
       "      <td>42.8</td>\n",
       "      <td>5.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>201801</td>\n",
       "      <td>38.7</td>\n",
       "      <td>1.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Value  Anomaly\n",
       "119  201401   35.5     -1.9\n",
       "120  201501   36.1     -1.3\n",
       "121  201601   40.8      3.4\n",
       "122  201701   42.8      5.4\n",
       "123  201801   38.7      1.3"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "68197a23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Temperature</th>\n",
       "      <th>Anomaly</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>189501</td>\n",
       "      <td>34.2</td>\n",
       "      <td>-3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>189601</td>\n",
       "      <td>34.7</td>\n",
       "      <td>-2.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>189701</td>\n",
       "      <td>35.5</td>\n",
       "      <td>-1.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Temperature  Anomaly\n",
       "0  189501         34.2     -3.2\n",
       "1  189601         34.7     -2.7\n",
       "2  189701         35.5     -1.9"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.columns = ['Date', 'Temperature', 'Anomaly']\n",
    "\n",
    "nyc.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "35239317",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    124.000000\n",
       "mean      37.595161\n",
       "std        4.539848\n",
       "min       26.100000\n",
       "25%       34.575000\n",
       "50%       37.600000\n",
       "75%       40.600000\n",
       "max       47.600000\n",
       "Name: Temperature, dtype: float64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.Temperature.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "3154e8b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('int64')"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.Date.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "242e64ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "nyc.Date = nyc.Date.floordiv(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "d08d0b17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Temperature</th>\n",
       "      <th>Anomaly</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1895</td>\n",
       "      <td>34.2</td>\n",
       "      <td>-3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1896</td>\n",
       "      <td>34.7</td>\n",
       "      <td>-2.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1897</td>\n",
       "      <td>35.5</td>\n",
       "      <td>-1.9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Date  Temperature  Anomaly\n",
       "0  1895         34.2     -3.2\n",
       "1  1896         34.7     -2.7\n",
       "2  1897         35.5     -1.9"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "89182c23",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.precision', 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "70dd5d92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    124.00\n",
       "mean      37.60\n",
       "std        4.54\n",
       "min       26.10\n",
       "25%       34.58\n",
       "50%       37.60\n",
       "75%       40.60\n",
       "max       47.60\n",
       "Name: Temperature, dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nyc.Temperature.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "d2e57e6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy import stats\n",
    "\n",
    "linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "5b0520ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.014771361132966163"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linear_regression.slope"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "c74ae9f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8.694993233674289"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linear_regression.intercept"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "51e3502f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38.51837136113297"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linear_regression.slope * 2019 + linear_regression.intercept"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "3bdc1048",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36.612865774980335"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "linear_regression.slope * 1890 + linear_regression.intercept"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "b1cb230f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10.0, 70.0)"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.set_style('whitegrid')\n",
    "\n",
    "axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)\n",
    "\n",
    "axes.set_ylim(10, 70)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "ba90b1c3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2120"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Self check 3 for a higher temperture of 40 degrees\n",
    "year = 2019\n",
    "\n",
    "slope = linear_regression.slope\n",
    "\n",
    "intercept = linear_regression.intercept\n",
    "\n",
    "temperature = slope * year + intercept\n",
    "\n",
    "while temperature < 40.0:\n",
    "    year += 1\n",
    "    temperature = slope * year + intercept\n",
    "    \n",
    "year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "831fd486",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2188"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Self check variance for a higher temperture of 41 degrees\n",
    "year = 2019\n",
    "\n",
    "slope = linear_regression.slope\n",
    "\n",
    "intercept = linear_regression.intercept\n",
    "\n",
    "temperature = slope * year + intercept\n",
    "\n",
    "while temperature < 41.0:\n",
    "    year += 1\n",
    "    temperature = slope * year + intercept\n",
    "    \n",
    "year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "0fb4a1a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3474"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Self check variance for a higher temperture of 60 degrees\n",
    "year = 2019\n",
    "\n",
    "slope = linear_regression.slope\n",
    "\n",
    "intercept = linear_regression.intercept\n",
    "\n",
    "temperature = slope * year + intercept\n",
    "\n",
    "while temperature < 60.0:\n",
    "    year += 1\n",
    "    temperature = slope * year + intercept\n",
    "    \n",
    "year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9902771",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Final project Ramon Torres"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
