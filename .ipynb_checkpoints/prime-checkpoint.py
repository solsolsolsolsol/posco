{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_prime(num):\n",
    "    for i in range(1,int(num)+1):\n",
    "        if (int(num)%i==0) and (i!=1) and (i!=int(num)):\n",
    "            return False\n",
    "        else:\n",
    "            return True\n",
    "        \n",
    "isprime=check_prime(7)\n",
    "print(isprime)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
