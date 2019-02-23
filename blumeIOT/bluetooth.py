import subprocess


class BluetoothManager:
    def __init__(self, adapter="hci0", sudo=True):
        self.adapter = adapter
        self.sudo = sudo

    def _sudo(self):
        if (self.sudo==True): return "sudo "
        return ""

    def _execute(self, cmd):
        if (type(cmd) == list):
            cmd = " ".join(cmd)
        cmd = self._sudo() + cmd
        print(">> " + cmd)
        out = subprocess.check_output(cmd,shell=True)
        print("<< " + str(out))
        return out

    def setName(self, name):
        self._execute(["hciconfig",self.adapter,"name",name])

    def getName(self):
        pass

    def show(self):
        pass

    def hide(self):
        pass
