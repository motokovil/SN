import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):

    def setUp(self) -> None:
        self.empleado = Empleado(200)

    def test_instance(self):
        self.assertIsInstance(self.empleado, Empleado)

    def test_is_correct(self):
        self.assertEqual(self.empleado.prestamo(200),True)

