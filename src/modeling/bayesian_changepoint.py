import pymc as pm
import numpy as np
import arviz as az
from typing import Tuple
from ..config import ModelConfig



def build_model(returns: np.ndarray):
    n = len(returns)
    idx = np.arange(n)

    with pm.Model() as model:

        # Continuous changepoint location
        tau = pm.Uniform("tau", lower=0, upper=n)

        # Regime means
        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        sigma = pm.Exponential("sigma", 1)

        # Smooth transition using sigmoid
        w = pm.math.sigmoid((idx - tau) / 1.0)

        mu = (1 - w) * mu_1 + w * mu_2

        pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

    return model

def sample_model(model, config: ModelConfig):
    with model:
        trace = pm.sample(
            draws=config.draws,
            tune=config.tune,
            chains=4,
            cores=4,
            target_accept=0.9,
            random_seed=config.random_seed,
            return_inferencedata=True
        )
    return trace
def extract_tau_summary(trace):

    tau_samples = trace.posterior["tau"].values.flatten()

    tau_mean = int(np.mean(tau_samples))
    tau_ci_low = int(np.percentile(tau_samples, 2.5))
    tau_ci_high = int(np.percentile(tau_samples, 97.5))

    return {
        "tau_mean": tau_mean,
        "tau_ci_low": tau_ci_low,
        "tau_ci_high": tau_ci_high
    }
