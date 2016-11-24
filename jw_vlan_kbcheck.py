import pyeapi

# Reuse functions from class5, exercise2
from ansible.module_utils.basic import *

def main():
    '''
    Simple Ansible module to create an Arista VLAN
    '''
    module = AnsibleModule(
        argument_spec=dict(
            arista_sw=dict(required=True),
            vlan_id=dict(required=True),
            vlan_name=dict(required=False),
            doiremove=dict(required=False, type='bool', default=False),
            doichange=dict(required=False, type='bool', default=False)
        )
    )

    vlan_id = module.params['vlan_id']
    name = module.params.get('vlan_name')
    arista_sw = module.params.get('arista_sw')
    doiremove = module.params.get('doiremove')
    doichange = module.params.get('doichange')

    eapi_conn = pyeapi.connect_to(arista_sw)

    show_vlan = eapi_conn.enable('show vlan')
    show_vlan = show_vlan[0]
    show_vlan = show_vlan['result']
    show_vlan = show_vlan['vlans']
    if vlan_id not in show_vlan.keys():
        cmds = ['vlan ' + vlan_id, 'name ' + name]
        eapi_conn.config(cmds)
        module.exit_json(msg="Adding VLAN including vlan_name (if present)", changed=True)
    else:
        if doiremove:
            cmds = ['no vlan ' + vlan_id]
            eapi_conn.config(cmds)
            module.exit_json(msg="Removing VLAN", changed=True)
        elif doichange:
            my_vlan = show_vlan[vlan_id]
            my_vlan_name = my_vlan['name']
            if name is not None and name != my_vlan_name:                
                cmds = ['vlan ' + vlan_id, 'name ' + name]
                eapi_conn.config(cmds)
                module.exit_json(msg="Changing vlan_name", changed=True)
            else:   
                module.exit_json(msg="VLAN already exists, no action required", changed=False)
        else:
                module.exit_json(msg="VLAN already exists, no action required", changed=False)

if __name__ == "__main__":
    main()
