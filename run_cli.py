import sys
from maa.toolkit import Toolkit
from assets.custom.action.basics.ChooseMax import ChooseMax


def main():
    # 注册自定义动作-每日采买
    Toolkit.pi_register_custom_action("ChooseMax", ChooseMax())  # 买买买

    directly = "-d" in sys.argv
    Toolkit.pi_run_cli("./", "./", directly)

if __name__ == "__main__":
    main()