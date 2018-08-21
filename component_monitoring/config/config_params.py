class OutputConfig(object):
    def __init__(self):
        self.name = ''
        self.obtained_value_type = ''
        self.expected_value = ''

class FunctionalMappingConfig:
    def __init__(self):
        self.inputs = list()
        self.outputs = list()

class MonitorModeConfig:
    def __init__(self):
        self.name = ''
        self.mappings = list()

class ComponentMonitorConfig:
    def __init__(self):
        self.name = ''
        self.modes = list()
        self.component_dependencies = list()

class HardwareMonitorNames:
    LASER_DEVICE_MONITOR = 'laser_device_monitor'
    LASER_FUNCTIONAL_MONITOR = 'laser_functional_monitor'
    LASER_HEARTBEAT_MONITOR = 'laser_heartbeat_monitor'
