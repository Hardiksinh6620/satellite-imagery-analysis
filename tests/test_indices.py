import numpy as np
from src.indices import normalized_difference

def test_normalized_difference_formula():
    red=np.array([[0.1,0.2]],dtype="float32"); nir=np.array([[0.4,0.6]],dtype="float32")
    out=normalized_difference(nir,red)
    assert np.isclose(out[0,0],0.6)

def test_zero_denominator_is_masked():
    out=normalized_difference(np.array([1.0]),np.array([-1.0]))
    assert bool(out.mask[0])
