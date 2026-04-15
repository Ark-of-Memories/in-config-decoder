import os

from src.i18n import decode_locres
from src.lua import decode_luas, decode_lua_bytecode
from src.config import decode_configs, decode_helper
from src.sound import generate_bank_data, load_bank_xml, resort_event_wems

def decode_lua_and_configs(I_N_CORE_DATA_PATH):
    decode_luas(I_N_CORE_DATA_PATH)
    decode_configs(I_N_CORE_DATA_PATH)
    decode_helper(I_N_CORE_DATA_PATH)

def decode_infinity_nikki_data_repo(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, (f"X6Game/Content/Script/GenV2/Cfg/CfgTypes.lua")))
    decode_configs(I_N_CORE_DATA_PATH, True)
    decode_locres(I_N_CORE_DATA_PATH)

def decode_just_configs(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, (f"X6Game/Content/Script/GenV2/Cfg/CfgTypes.lua")))
    decode_configs(I_N_CORE_DATA_PATH)

def decode_just_helper(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, (f"X6Game/Content/Script/GenV2/Cfg/CfgHelper.lua")))
    decode_helper(I_N_CORE_DATA_PATH)

def resort_audio(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH):
    generate_bank_data(I_N_CORE_DATA_PATH)
    load_bank_xml()
    resort_event_wems(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH)

if __name__ == '__main__':
    I_N_CORE_DATA_PATH = r'D:/RE/IN/CBT_Output/Exports'  # change here to your path, where .pak files are extracted
    I_N_STRM_DATA_PATH = r'D:/RE/IN/CBT_Output/Exports'  # change here to your path, where .utoc & .ucas files are extracted
    decode_just_configs(I_N_CORE_DATA_PATH)
    decode_just_helper(I_N_CORE_DATA_PATH)
    # decode_locres(I_N_CORE_DATA_PATH)
    # decode_infinity_nikki_data_repo(I_N_CORE_DATA_PATH)
    # resort_audio(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH)