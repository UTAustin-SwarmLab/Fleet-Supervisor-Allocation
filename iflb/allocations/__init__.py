from .random_allocation import RandomAllocation
from .CUR_allocation import CURAllocation
from .TD_allocation import TDAllocation
from .NASA_allocation import NASAAllocation
from .ASA_allocation import ASAAllocation
from .NCUR_allocation import NCURAllocation


# Mappings from CLI option strings to allocation strategies
allocation_map = {
    "random": RandomAllocation,
    "CUR": CURAllocation,
    "TD": TDAllocation,
    "NASA": NASAAllocation,
    "ASA": ASAAllocation,
    "NCUR": NCURAllocation
}

allocation_cfg_map = {
    "CUR": "CUR_allocation.yaml",
    "TD": "TD_allocation.yaml",
    "random": "random_allocation.yaml",
    "NASA": "NASM_allocation.yaml",
    "ASA": "ASM_allocation.yaml",
    "NCUR": "NCUR_allocation.yaml"
}
