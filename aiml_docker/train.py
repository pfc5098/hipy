import numpy as np
import logging
logging.basicConfig(# filename='train.log',
                    level=logging.INFO, format='%(asctime)s:%(message)s')

f = lambda x: x ** 2 - x + 0.25 

x_obs = np.linspace(0, 1, num=10)
y = f(x_obs) + np.random.normal(0, 0.02, size=len(x_obs))

X = np.array([[x ** 2, x, 1] for x in x_obs])
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y

logging.info(f'X = {X}')
logging.info(f'y = {y}')
logging.info(f'beta_hat = {beta_hat}')