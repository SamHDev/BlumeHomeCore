import blumeIOT as blume

blume.BlumeManager(config="config.json")

bt = blume.BluetoothManager()

bt.setName("BlumeDevice")

print(bt.getName())

input("")

bt.show()

input()

bt.hide()
