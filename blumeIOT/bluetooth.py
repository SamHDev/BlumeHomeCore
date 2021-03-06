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
        return str(self._execute(["hciconfig", self.adapter, "name"])).split("Name: '")[1].rsplit("'")[0]

    def show(self):
        self._execute(["hciconfig", self.adapter, "piscan"])

    def hide(self):
        self._execute(["hciconfig", self.adapter, "noscan"])
