"""Load the native extension only when its operation is called."""


def generalized_rspmm(edge_index, edge_type, edge_weight, relation, input,
                      sum="add", mul="mul"):
    # Importing a Triton submodule also initializes this package. Keep that
    # path independent of the optional C++/CUDA extension and its toolchain.
    from .rspmm import generalized_rspmm as native_rspmm

    return native_rspmm(edge_index, edge_type, edge_weight, relation, input,
                        sum=sum, mul=mul)
