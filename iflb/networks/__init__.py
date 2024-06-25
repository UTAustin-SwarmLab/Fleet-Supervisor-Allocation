from .dirichlet_network import DirichletNetwork
from .real_network import RealNetwork
from .base_network import BaseNetwork
from .scarce_network import ScarceNetwork
from .fiveg_network import FiveGNetwork

network_map = {
    "base": BaseNetwork,
    "dirichlet": DirichletNetwork,
    "real": RealNetwork,
    "scarce": ScarceNetwork,
    "fiveg": FiveGNetwork,

}

network_cfg_map = {
    "dirichlet": "dirichlet_network.yaml",
    "real": "real_network.yaml",
    "scarce": "scarce_network.yaml",
    "fiveg": "fiveg_network.yaml"
}
