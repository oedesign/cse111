# test_water_flow.py
from water_flow import *
from pytest import approx

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(10.0, 6.0) == approx(13.0)
    assert water_column_height(25.0, 0.2) == approx(25.1)
    assert water_column_height(48.3, 12.8) == approx(54.7)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.0, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.0, 0.018, 1.75) == approx(-113.008, abs=0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-0.309, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-0.337, abs=0.001)

def test_kpa_to_psi():
    assert kpa_to_psi(0.0) == approx(0.0, abs=0.001)
    assert kpa_to_psi(1.0) == approx(0.1450377, abs=0.001)
    assert kpa_to_psi(100.0) == approx(14.50377, abs=0.001)
    assert kpa_to_psi(158.7) == approx(23.012, abs=0.01)

# New test for creativity
def test_psi_to_kpa():
    assert psi_to_kpa(0.0) == approx(0.0, abs=0.001)
    assert psi_to_kpa(0.1450377) == approx(1.0, abs=0.001)
    assert psi_to_kpa(14.50377) == approx(100.0, abs=0.01)

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "--tb=line", "-rN", __file__])
