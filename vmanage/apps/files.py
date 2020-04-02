"""Cisco vManage Files API Methods.
"""

import json
import requests
import os
import dictdiffer
import yaml
from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods
from vmanage.api.device_templates import DeviceTemplates
from vmanage.api.feature_templates import FeatureTemplates
from vmanage.api.policy_lists import PolicyLists
from vmanage.api.policy_definitions import PolicyDefinitions
from vmanage.api.local_policy import LocalPolicy
from vmanage.api.central_policy import CentralPolicy


class Files(object):
    """Access to Various vManage Utilitiesinstance.

    vManage has several utilities that are needed for correct execution
    of applications against the API.  For example, this includes waiting
    for an action to complete before moving onto the next task.

    """

    def __init__(self, session, host, port=443):
        """Initialize Utilities object with session parameters.

        Args:
            session (obj): Requests Session object
            host (str): hostname or IP address of vManage
            port (int): default HTTPS 443

        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f'https://{self.host}:{self.port}/dataservice/'

    def export_templates_to_file(self, export_file, name_list=[], type=None):

        device_templates = DeviceTemplates(self.session, self.host, self.port)
        feature_templates = FeatureTemplates(self.session, self.host, self.port)

        template_export = {}
        if type != 'feature':
            # Export the device templates and associated feature templates
            device_template_list = device_templates.get_device_template_list(name_list=name_list)
            template_export.update({'vmanage_device_templates': device_template_list})
            feature_name_list = []
            if name_list:
                for device_template in device_template_list:
                    if 'generalTemplates' in device_template:
                        for general_template in device_template['generalTemplates']:
                            if 'templateName' in general_template:
                                feature_name_list.append(general_template['templateName'])
                            if 'subTemplates' in general_template:
                                for sub_template in general_template['subTemplates']:
                                    if 'templateName' in sub_template:
                                        feature_name_list.append(sub_template['templateName'])
                name_list = list(set(feature_name_list))
        # Since device templates depend on feature templates, we always add them.
        feature_templates = FeatureTemplates(self.session, self.host, self.port)
        feature_template_list = feature_templates.get_feature_template_list(name_list=name_list)
        template_export.update({'vmanage_feature_templates': feature_template_list})

        if export_file.endswith('.json'):
            with open(export_file, 'w') as outfile:
                json.dump(template_export, outfile, indent=4, sort_keys=False)
        elif export_file.endswith('.yaml') or export_file.endswith('.yml'):
            with open(export_file, 'w') as outfile:
                yaml.dump(template_export, outfile, indent=4, sort_keys=False)
        else:
            raise Exception("File format not supported")

    def import_templates_from_file(self, file, update=False, check_mode=False, name_list=[], type=None):

        vmanage_device_templates = DeviceTemplates(self.session, self.host, self.port)
        vmanage_feature_templates = FeatureTemplates(self.session, self.host, self.port)

        changed = False
        feature_template_updates = []
        device_template_updates = []
        template_data = {}
        feature_template_data = {}

        # Read in the datafile
        if not os.path.exists(file):
            raise Exception(f"Cannot find file {file}")
        with open(file) as f:
            if file.endswith('.yaml') or file.endswith('.yml'):
                template_data = yaml.safe_load(f)
            else:
                template_data = json.load(f)

        if 'vmanage_feature_templates' in template_data:
            imported_feature_template_list = template_data['vmanage_feature_templates']
        else:
            imported_feature_template_list = []

        imported_device_template_list = []

        if type != 'feature':
            # Import the device templates and associated feature templates
            if 'vmanage_device_templates' in template_data:
                imported_device_template_list = template_data['vmanage_device_templates']
            if name_list:
                feature_name_list = []
                pruned_device_template_list = []
                for device_template in imported_device_template_list:
                    if device_template['templateName'] in name_list:
                        pruned_device_template_list.append(device_template)
                        if 'generalTemplates' in device_template:
                            for general_template in device_template['generalTemplates']:
                                if 'templateName' in general_template:
                                    feature_name_list.append(general_template['templateName'])
                                if 'subTemplates' in general_template:
                                    for sub_template in general_template['subTemplates']:
                                        if 'templateName' in sub_template:
                                            feature_name_list.append(sub_template['templateName'])
                imported_device_template_list = pruned_device_template_list
                name_list = list(set(feature_name_list))
        # Since device templates depend on feature templates, we always add them.
        if name_list:
            pruned_feature_template_list = []
            imported_feature_template_dict = self.list_to_dict(imported_feature_template_list, key_name='templateName', remove_key=False)
            for feature_template_name in name_list:
                if feature_template_name in imported_feature_template_dict:
                    pruned_feature_template_list.append(imported_feature_template_dict[feature_template_name])
                # Otherwise, we hope the feature list is already there (e.g. Factory Default)
            imported_feature_template_list = pruned_feature_template_list

        # Process the feature templates
        feature_template_updates = vmanage_feature_templates.import_feature_template_list(
            imported_feature_template_list,
            check_mode=False,
            update=False
        )

        # Process the device templates
        device_template_updates = vmanage_device_templates.import_device_template_list(
            imported_device_template_list,
            check_mode=False,
            update=False
        )

        return {
            'feature_template_updates': feature_template_updates,
            'device_template_updates': device_template_updates,
        }

    #
    # Policy
    #
    def export_policy_to_file(self, export_file):

        policy_lists = PolicyLists(self.session, self.host, self.port)
        policy_definitions = PolicyDefinitions(self.session, self.host, self.port)
        local_policy = LocalPolicy(self.session, self.host, self.port)
        central_policy = CentralPolicy(self.session, self.host, self.port)

        policy_lists_list = policy_lists.get_policy_list_list()
        policy_definitions_list = policy_definitions.get_policy_definition_list()
        central_policies_list = central_policy.get_central_policy_list()
        local_policies_list = local_policy.get_local_policy_list()

        policy_export = {
            'vmanage_policy_lists': policy_lists_list,
            'vmanage_policy_definitions': policy_definitions_list,
            'vmanage_central_policies': central_policies_list,
            'vmanage_local_policies': local_policies_list
        }

        if export_file.endswith('.json'):
            with open(export_file, 'w') as outfile:
                json.dump(policy_export, outfile, indent=4, sort_keys=False)
        elif export_file.endswith('.yaml') or export_file.endswith('.yml'):
            with open(export_file, 'w') as outfile:
                yaml.dump(policy_export, outfile, default_flow_style=False)
        else:
            raise Exception("File format not supported")

    def import_policy_from_file(self, file, update=False, check_mode=False, push=False):

        vmanage_policy_lists = PolicyLists(self.session, self.host, self.port)
        vmanage_policy_definitions = PolicyDefinitions(self.session, self.host, self.port)
        vmanage_central_policy = CentralPolicy(self.session, self.host, self.port)
        vmanage_local_policy = LocalPolicy(self.session, self.host, self.port)

        changed = False
        policy_list_updates = []
        policy_definition_updates = []
        central_policy_updates = []
        local_policy_updates = []

        # Read in the datafile
        if not os.path.exists(file):
            raise Exception('Cannot find file {0}'.format(file))
        with open(file) as f:
            if file.endswith('.yaml') or file.endswith('.yml'):
                policy_data = yaml.safe_load(f)
            else:
                policy_data = json.load(f)

        # Separate the feature template data from the device template data
        if 'vmanage_policy_lists' in policy_data:
            policy_list_data = policy_data['vmanage_policy_lists']
        else:
            policy_list_data = []
        if 'vmanage_policy_definitions' in policy_data:
            policy_definition_data = policy_data['vmanage_policy_definitions']
        else:
            policy_definition_data = []
        if 'vmanage_central_policies' in policy_data:
            central_policy_data = policy_data['vmanage_central_policies']
        else:
            central_policy_data = []
        if 'vmanage_local_policies' in policy_data:
            local_policy_data = policy_data['vmanage_local_policies']
        else:
            local_policy_data = []

        policy_list_updates = vmanage_policy_lists.import_policy_list_list(policy_list_data, check_mode=check_mode, update=update,
                                                                           push=push)

        vmanage_policy_lists.clear_policy_list_cache()

        policy_definition_updates = vmanage_policy_definitions.import_policy_definition_list(policy_definition_data, check_mode=check_mode,
                                                                                             update=update, push=push)
        central_policy_updates = vmanage_central_policy.import_central_policy_list(central_policy_data, check_mode=check_mode,
                                                                                   update=update, push=push)
        local_policy_updates = vmanage_local_policy.import_local_policy_list(local_policy_data, check_mode=check_mode, update=update,
                                                                             push=push)

        for local_policy in local_policy_data:
            diff = vmanage_local_policy.import_local_policy(local_policy, check_mode=check_mode, update=update, push=push)
            if len(diff):
                local_policy_updates.append({'name': local_policy['policyName'], 'diff': diff})

        return {
            'policy_list_updates': policy_list_updates,
            'policy_definition_updates': policy_definition_updates,
            'central_policy_updates': central_policy_updates,
            'local_policy_updates': local_policy_updates
        }