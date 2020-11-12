# Copyright (c) 2020 3DPrinterOS
from typing import List, Optional
from UM.OutputDevice.OutputDevice import OutputDevice
from UM.OutputDevice import OutputDeviceError
from UM.Scene.SceneNode import SceneNode #For typing.
from UM.FileHandler.FileHandler import FileHandler #For typing.
from UM.i18n import i18nCatalog
from UM.Signal import Signal

catalog = i18nCatalog("cura")


##  Implements an OutputDevice that supports saving to arbitrary local files.
class OctoPrintOutputUploadDevice(OutputDevice):
    def __init__(self, device_id):
        super().__init__(device_id)

        self.setName(catalog.i18nc("@item:inmenu", "Local File"))
        self.setShortDescription(catalog.i18nc("@action:button", "Upload to Hercules Host"))
        self.setDescription(catalog.i18nc("@info:tooltip", "Upload G-Code to Hercules Host"))
        self.setIconName("upload_3d")
        self._busy = False


    ##  Request the specified nodes to be written to a file.
    #
    #   \param nodes A collection of scene nodes that should be written to the
    #   file.
    #   \param file_name \type{string} A suggestion for the file name to write
    #   to. Can be freely ignored if providing a file name makes no sense.
    #   \param limit_mimetypes Should we limit the available MIME types to the
    #   MIME types available to the currently active machine?
    #   \param kwargs Keyword arguments.

    def requestWrite(self, nodes: List[SceneNode], file_name: Optional[str] = None, limit_mimetypes: bool = False,
                     file_handler: Optional[FileHandler] = None, filter_by_machine: bool = False,
                     **kwargs: str) -> None:
        if self._busy:
            raise OutputDeviceError.DeviceBusyError()

        self.finished.connect(self._onUploadJobFinished)

        self._busy = True
        self.started.emit()

    def _onUploadJobFinished(self):
        self.finished.disconnect(self._onUploadJobFinished)
        self._busy = False

    def close(self) -> None:
        self.finished.disconnect(self._onUploadJobFinished)
        self._busy = False

    started = Signal()
    finished = Signal()
