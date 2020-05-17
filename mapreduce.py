import multiprocessing
import random
import threading

from rios import applier


class MapReduce():
    def __init__(self, input_images, output_image, map_func, reduce_func):
        self.__input_images = input_images
        self.__output_image = output_image
        self.__map_func = map_func
        self.__reduce_func = reduce_func

    def get_controls(self):
        controls = applier.ApplierControls()
        controls.setJobManagerType('multiprocessing')
        controls.setNumThreads(multiprocessing.cpu_count())
        return controls

    def map_func(self, info, inputs, outputs):
        outputs.output_image = self.__map_func(inputs.input_image)

    def reduce_func(self, info, inputs, outputs):
        outputs.output_image = self.__reduce_func(inputs.input_images)

    def map_worker(self, input_image, output_image):
        print("Running map function...")
        infiles = applier.FilenameAssociations()
        infiles.input_image = input_image

        outfiles = applier.FilenameAssociations()
        outfiles.output_image = output_image

        applier.apply(self.map_func, infiles, outfiles,
                      controls=self.get_controls())

    def reduce_worker(self, input_images, output_image):
        print("Running reduce function...")
        infiles = applier.FilenameAssociations()
        infiles.input_images = input_images

        outfiles = applier.FilenameAssociations()
        outfiles.output_image = output_image

        applier.apply(self.reduce_func, infiles, outfiles,
                      controls=self.get_controls())
        return output_image

    def __run_map_func(self, input_images):

        threads = []
        output_images = []

        for image in input_images:
            output_image = "/vsimem/{hash}".format(
                hash=random.getrandbits(128)
            )
            output_images.append(output_image)
            t = threading.Thread(target=self.map_worker,
                                 args=(image, output_image))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        return output_images

    def run(self):
        output_images_map = self.__run_map_func(self.__input_images)
        output_image_reduce = self.reduce_worker(output_images_map,
                                                self.__output_image)
        return output_image_reduce
