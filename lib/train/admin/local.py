class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/kaggle/working/AiATrack'  # Base directory for saving network checkpoints
        self.tensorboard_dir = self.workspace_dir  # Directory for tensorboard files
        self.pretrained_networks = self.workspace_dir + '/pretrained_networks'
        self.lasot_dir = '/kaggle/input/LaSOT'
        self.got10k_dir = '/kaggle/input/GOT10k'
        self.trackingnet_dir = '/kaggle/input/TrackingNet'
        self.coco_dir = '/kaggle/input//COCO'
