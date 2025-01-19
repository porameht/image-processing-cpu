import PIL.Image
import torch

from carvekit.api.interface import Interface
from carvekit.ml.wrap.fba_matting import FBAMatting
from carvekit.ml.wrap.tracer_b7 import TracerUniversalB7
from carvekit.pipelines.postprocessing import MattingMethod
from carvekit.pipelines.preprocessing import PreprocessingStub
from carvekit.trimap.generator import TrimapGenerator

class RemoveBackground:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RemoveBackground, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            print("Initializing RemoveBackground model...")

            # Initialize models
            self.seg_net = TracerUniversalB7(
                device='cpu',
                batch_size=1
            )

            self.fba = FBAMatting(
                device='cpu',
                input_tensor_size=2048,
                batch_size=1
            )

            self.trimap = TrimapGenerator()
            self.pre_processing = PreprocessingStub()
            self.post_processing = MattingMethod(
                matting_module=self.fba,
                trimap_generator=self.trimap,
                device='cpu'
            )

            self.interface = Interface(
                pre_pipe=self.pre_processing,
                post_pipe=self.post_processing,
                seg_pipe=self.seg_net
            )
            
            self._is_initialized = True
            print("Model initialization complete!")

    def remove_background(self, image_path: str):
        image = PIL.Image.open(image_path)
        image_wo_bg = self.interface([image])[0]
        return image_wo_bg
                   