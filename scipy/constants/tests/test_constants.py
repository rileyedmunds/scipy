from __future__ import division, print_function, absolute_import

from numpy.testing import run_module_suite, assert_equal, assert_allclose
from scipy._lib._numpy_compat import suppress_warnings
import scipy.constants as sc


def test_convert_temperature():
    assert_equal(sc.convert_temperature(32, 'f', 'Celsius'), 0)
    assert_equal(sc.convert_temperature([0, 0], 'celsius', 'Kelvin'),
                 [273.15, 273.15])
    assert_equal(sc.convert_temperature([0, 0], 'kelvin', 'c'),
                 [-273.15, -273.15])
    assert_equal(sc.convert_temperature([32, 32], 'f', 'k'), [273.15, 273.15])
    assert_equal(sc.convert_temperature([273.15, 273.15], 'kelvin', 'F'),
                 [32, 32])
    assert_equal(sc.convert_temperature([0, 0], 'C', 'fahrenheit'), [32, 32])
    assert_allclose(sc.convert_temperature([0, 0], 'c', 'r'), [491.67, 491.67],
                    rtol=0., atol=1e-13)
    assert_allclose(sc.convert_temperature([491.67, 491.67], 'Rankine', 'C'),
                    [0., 0.], rtol=0., atol=1e-13)
    assert_allclose(sc.convert_temperature([491.67, 491.67], 'r', 'F'),
                    [32., 32.], rtol=0., atol=1e-13)
    assert_allclose(sc.convert_temperature([32, 32], 'fahrenheit', 'R'),
                    [491.67, 491.67], rtol=0., atol=1e-13)
    assert_allclose(sc.convert_temperature([273.15, 273.15], 'K', 'R'),
                    [491.67, 491.67], rtol=0., atol=1e-13)
    assert_allclose(sc.convert_temperature([491.67, 0.], 'rankine', 'kelvin'),
                    [273.15, 0.], rtol=0., atol=1e-13)


def test_fahrenheit_to_celsius():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`F2C` is deprecated!")
        assert_equal(sc.F2C(32), 0)
        assert_equal(sc.F2C([32, 32]), [0, 0])


def test_celsius_to_kelvin():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`C2K` is deprecated!")
        assert_equal(sc.C2K([0, 0]), [273.15, 273.15])


def test_kelvin_to_celsius():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`K2C` is deprecated!")
        assert_equal(sc.K2C([0, 0]), [-273.15, -273.15])


def test_fahrenheit_to_kelvin():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`F2K` is deprecated!")
        sup.filter(DeprecationWarning, "`F2C` is deprecated!")
        sup.filter(DeprecationWarning, "`C2K` is deprecated!")
        assert_equal(sc.F2K([32, 32]), [273.15, 273.15])


def test_kelvin_to_fahrenheit():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`K2F` is deprecated!")
        sup.filter(DeprecationWarning, "`K2C` is deprecated!")
        sup.filter(DeprecationWarning, "`C2F` is deprecated!")
        assert_equal(sc.K2F([273.15, 273.15]), [32, 32])


def test_celsius_to_fahrenheit():
    with suppress_warnings() as sup:
        sup.filter(DeprecationWarning, "`C2F` is deprecated!")
        assert_equal(sc.C2F([0, 0]), [32, 32])


def test_lambda_to_nu():
    assert_equal(sc.lambda2nu(sc.speed_of_light), 1)


def test_nu_to_lambda():
    assert_equal(sc.nu2lambda(1), sc.speed_of_light)


if __name__ == "__main__":
    run_module_suite()
