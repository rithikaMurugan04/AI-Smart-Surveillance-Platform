from src.camera.camera_manager import CameraManager
class VideoPipeline:

    def __init__(self):

        self.camera = CameraManager()


    def start(self):

        self.camera.start_camera()


        while True:

            frame = self.camera.get_frame()


            if frame is not None:

                print("Frame received")


            key = input("Press q to stop: ")

            if key == "q":
                break


        self.camera.release()