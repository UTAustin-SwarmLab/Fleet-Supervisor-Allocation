from .dirichlet_network import DirichletNetwork
from .real_network import RealNetwork
from .base_network import BaseNetwork

network_map = {
    "base": BaseNetwork,
    "dirichlet": DirichletNetwork,
    "real": RealNetwork,
}

network_cfg_map = {"dirichlet": "dirichlet_network.yaml", "real": "real_network.yaml"}
