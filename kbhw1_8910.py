from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco.txt")
crypto_map = cisco_cfg.find_objects(r"^crypto")
for citem in crypto_map:
    if "crypto map CRYPTO" in citem.text:
        if "group2" in citem.children[2].text:
            print citem.children
for citem in crypto_map:
    if "crypto map CRYPTO" in citem.text:
        if "AES" not in citem.children[1].text:
            print citem.children
