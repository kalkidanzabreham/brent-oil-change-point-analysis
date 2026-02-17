from dataclasses import dataclass

@dataclass
class ModelConfig:
    draws: int = 4000
    tune: int = 2000
    target_accept: float = 0.99
    random_seed: int = 42
