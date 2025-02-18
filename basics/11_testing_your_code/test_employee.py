from src.employee import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee("Abdulquadri", "Ishola", 2000000)
    return employee


def test_give_default_raise(employee):
    initial_salary = employee.annual_salary
    employee.give_raise()
    assert initial_salary + 5000 == employee.annual_salary


def test_give_custom_raise(employee):
    initial_salary = employee.annual_salary
    employee.give_raise(20000)
    assert initial_salary + 20000 == employee.annual_salary
