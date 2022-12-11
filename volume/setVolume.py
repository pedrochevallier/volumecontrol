from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume



def setVolume(value, process):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == process + ".exe":
            print("Volume was: %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(value, None)
            print("Volume set to %s" % volume.GetMasterVolume())
