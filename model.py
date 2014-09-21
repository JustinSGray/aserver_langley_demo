from openmdao.main.api import Component
from openmdao.lib.datatypes.api import Float

from analysis_server import ASMixin

class MyComp(Component, ASMixin):

    input_var = Float(0, iotype='in')
    output_var = Float(iotype='out')

    def execute(self):
        self.output_var = self.input_var