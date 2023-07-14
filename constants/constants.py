DEBUG = False

if DEBUG:
    CMR_TO_ICH_SDO = 0x50F
    ICH_TO_CMR_SDO = 0x48F
else:
    CMR_TO_ICH_SDO = 0x50E
    ICH_TO_CMR_SDO = 0x48E

CANOPEN_READ = 0x40
CANOPEN_READ_1_BYTE = 0x4F
CANOPEN_READ_2_BYTE = 0x4B
CANOPEN_READ_4_BYTE = 0x43

CANOPEN_WRITE_1_BYTE = 0x2F
CANOPEN_WRITE_2_BYTE = 0x2B
CANOPEN_WRITE_4_BYTE = 0x23

READ_MEMORY_INDEX = 0x4003
READ_MEMORY_SUBINDEX = 0x01

COLOR_SCHEME = "DARK"
COLORS = {
    "LIGHT": {
        "BACKGROUND_COLOR": "#eff1f5",
        "SECONDARY_COLOR": "#e6e9ef",
        "THIRD_COLOR": "#dce0e8",
        "BORDER_COLOR": "#ccd0da",
        "BORDER_COLOR_HOVERED": "#bcc0cc",
        "BORDER_COLOR_FOCUSED": "#acb0be",
        "TEXT_COLOR": "#4c4f69",
        "RED": "#d20f39",
        "RED_HOVER": "#d16163",
        "RED_FOCUSED": "#a94447",
        "MAROON": "#e64553",
        "GREEN": "#40a02b",
        "GREEN_HOVER": "#87b162",
        "GREEN_FOCUSED": "#6c904a",
    },
    "DARK": {
        "BACKGROUND_COLOR": "#303446",
        "SECONDARY_COLOR": "#292c3c",
        "THIRD_COLOR": "#232634",
        "BORDER_COLOR": "#414559",
        "BORDER_COLOR_HOVERED": "#51576d",
        "BORDER_COLOR_FOCUSED": "#626880",
        "TEXT_COLOR": "#c6d0f5",
        "RED": "#e78284",
        "RED_HOVER": "#d16163",
        "RED_FOCUSED": "#a94447",
        "MAROON": "#ea999c",
        "GREEN": "#a6d189",
        "GREEN_HOVER": "#87b162",
        "GREEN_FOCUSED": "#6c904a",
    }
}
