import hid
for d in hid.enumerate(0x0C45, 0x5004):
    print(hex(d["usage_page"]), hex(d["usage"]), d["interface_number"], d["path"])