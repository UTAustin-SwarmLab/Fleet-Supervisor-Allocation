from .random_allocation import RandomAllocation
from .CUR_allocation import CURAllocation
from .TD_allocation import TDAllocation
from .NASM_allocation import NASMAllocation
from .ASM_allocation import ASMAllocation


# Mappings from CLI option strings to allocation strategies
allocation_map = {
    "random": RandomAllocation,
    "CUR": CURAllocation,
    "TD": TDAllocation,
    "NASM": NASMAllocation,
    "ASM": ASMAllocation,
}

allocation_cfg_map = {
    "CUR": "CUR_allocation.yaml",
    "TD": "TD_allocation.yaml",
    "random": "random_allocation.yaml",
    "NASM": "NASM_allocation.yaml",
    "ASM": "ASM_allocation.yaml",
}
