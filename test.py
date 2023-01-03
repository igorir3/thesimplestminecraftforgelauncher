import minecraft_launcher_lib as mf
import uuid
import subprocess

print("Start")
current_max = 0


def set_status(status: str):
    print(status)

print("Start")
def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")

print("Start")
def set_max(new_max: int):
    global current_max
    current_max = new_max
print("Start")

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

mf.forge.install_forge_version("1.16.5-36.2.39", "C:\\Users\\kiril\\Desktop\\MLP\\minecraft", callback = callback)
print("i'm alive!")
UUID = uuid.uuid4().hex
print(UUID)
options = {
    "username": "Igorir3",
    "uuid": UUID,
    "token": ""
}


print("i'm")
version_list = mf.utils.get_installed_versions("C:\\Users\\kiril\\Desktop\\MLP\\minecraft")
version = version_list[0].get('id')
minecraft_command = mf.command.get_minecraft_command(version, "C:\\Users\\kiril\\Desktop\\MLP\\minecraft", options)
print("alive!")
subprocess.run(minecraft_command)