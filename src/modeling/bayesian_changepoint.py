import pymc as pm
import numpy as np

def bayesian_change_point(returns):
    n = len(returns)
    idx = np.arange(n)

    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)

        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        sigma = pm.Exponential("sigma", 1)

        mu = pm.math.switch(idx < tau, mu_1, mu_2)

        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

        trace = pm.sample(
            draws=2000,
            tune=1000,
            target_accept=0.95,
            return_inferencedata=True
        )

    return model, trace
