"""Networks module."""

from .ookla import OoklaNetwork
from .base import BaseNetwork
from .always import AlwaysNetwork
from .mixed_scarce import MixedScarceNetwork
from .fiveg import FiveGNetwork
from .changing_scarce import ChangingScarceNetwork
from .dirichlet import DirichletNetwork

network_map = {
    "base": BaseNetwork,
    "always": AlwaysNetwork,
    "ookla": OoklaNetwork,
    "mixed-scarce": MixedScarceNetwork,
    "fiveg": FiveGNetwork,
    "changing-scarce": ChangingScarceNetwork,
    "dirichlet": DirichletNetwork
}

network_cfg_map = {
    "ookla": "ookla_network.yaml",
    "mixed-scarce": "mixed_scarce_network.yaml",
    "fiveg": "fiveg_network.yaml",
    "changing-scarce": "changing_scarce_network.yaml",
    "dirichlet": "dirichlet_network.yaml"
}
