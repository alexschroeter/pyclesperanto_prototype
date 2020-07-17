import pyclesperanto_prototype as cle
import numpy as np
import pytest
import pyopencl as cl


@pytest.mark.xfail(raises=cl.RuntimeError)
def test_nonzero_minimum_box():
    test = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 2, 0],
        [0, 2, 2, 3, 0],
        [0, 3, 3, 4, 0],
        [0, 0, 0, 0, 0]
    ]))

    reference = cle.push(np.asarray([
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 2, 2, 2, 0],
        [0, 0, 0, 0, 0]
    ]))

    result = cle.create(test)
    flag = cle.create((1, 1, 1))
    cle.nonzero_minimum_box(test, flag, result)

    print(result)

    a = cle.pull(result)
    b = cle.pull(reference)
    assert (np.allclose(a, b, atol=0.00001))
    print("ok nonzero_minimum_box")

