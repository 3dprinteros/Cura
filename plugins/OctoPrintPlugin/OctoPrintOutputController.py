# Copyright (c) 2020 Aldo Hoeben / fieldOfView
# OctoPrintPlugin is released under the terms of the AGPLv3 or higher.

from cura.PrinterOutput.GenericOutputController import GenericOutputController

class OctoPrintOutputController(GenericOutputController):
    def __init__(self, output_device: "PrinterOutputDevice") -> None:
        super().__init__(output_device)

    def moveHead(self, printer: "PrinterOutputModel", x, y, z, speed) -> None:
        axis_information = self._output_device.getAxisInformation()
        if axis_information["x"].inverted:
            x = -x
        if axis_information["y"].inverted:
            x = -y
        if axis_information["z"].inverted:
            x = -z

        self._output_device.sendCommand("G91")
        self._output_device.sendCommand("G0 X%s Y%s Z%s F%s" % (x, y, z, speed))
        self._output_device.sendCommand("G90")