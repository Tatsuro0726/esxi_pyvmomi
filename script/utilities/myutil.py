# VMware module
# URL: https://github.com/vmware/pyvmomi
# pyvmomi community: https://github.com/vmware/pyvmomi-community-samples
from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim

# Basic python module
import atexit


class VirtualMachine:

    def __init__(self, summary_obj, storage_obj

def get_all_vms(host_ip, username, password, port=443):
    """対象のESXiホスト上のVMを取得

    Parameters:
    -------------------------------
    host_ip: string
        対象ESXiホストのIPアドレス
    port: int
        対象ESXiホストの接続ポート
    username: string
        対象ESXiホストのログインユーザー名
    password: string
        対象ESXiホストのログインパスワード

    Returns:
    -------------------------------


    """

    # Service Instance作成
    si = SmartConnectNoSSL(
        host=host_ip,
        port=int(port),
        user=username,
        pwd=password
    )
    # プログラム終了後の実行登録
    atexit.register(Disconnect, si)

    # Service content取得
    content = si.RetrieveContent()
    # vmFolderの検索
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            vmFolder = child.vmFolder
            vmList = vmFolder.childEntity

    for vm in vmList:



get_all_vms(host_ip='192.168.3.41', username='root', password='root123!')
