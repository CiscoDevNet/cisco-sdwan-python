"""Cisco vManage Monitor Networks API Methods.
"""

from six.moves.urllib.parse import urlencode
from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods


class MonitorNetwork(object):
    """vManage Monitor Networks API

    Responsible for GET methods against vManage Real Time Monitoring
    for network devices.

    """
    def __init__(self, session, host, port=443):
        """Initialize Monitor Networks object with session parameters.

        Args:
            session (obj): Requests Session object
            host (str): hostname or IP address of vManage
            port (int): default HTTPS 443

        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f'https://{self.host}:{self.port}/dataservice/'

    def _get_device_type(self, system_ip):
        device_model = self.get_device_system_info(system_ip)[0]['device-model']
        url = f"{self.base_url}device/models"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        device_type = [device['deviceClass'] for device in result if device_model == device['name']][0]
        return device_type

    def _ipsec_query_params(self, query_params, **kwargs):
        if 'remote_tloc_address' in kwargs:
            query_params.append(('remote-tloc-address', kwargs['remote_tloc_address']))
        if 'remote_tloc_color' in kwargs:
            query_params.append(('remote-tloc-color', kwargs['remote_tloc_color']))
        if 'local_tloc_color' in kwargs:
            query_params.append(('local-tloc-color', kwargs['local_tloc_color']))
        return query_params

    def get_aaa_users(self, system_ip):
        """Provides AAA users for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device ARP table data.
        """

        url = f"{self.base_url}device/aaa/users?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_arp_table(self, system_ip):
        """Provides ARP entries for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device ARP table data.
        """

        url = f"{self.base_url}device/arp?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_history(self, system_ip, **kwargs):
        """Provides BFD history for device.

        Args:
            system_ip (str): Device System IP
            remote_system_ip (str): (Optional) Remote System IP
            remote_color (str): (Optional) Remote Color

        Returns:
            result (dict): Device BFD history data.
        """

        url = f"{self.base_url}device/bfd/history"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'remote_system_ip' in kwargs:
            query_params.append(('system-ip', kwargs['remote_system_ip']))
        if 'remote_color' in kwargs:
            query_params.append(('color', kwargs['remote_color']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_links(self, system_ip, **kwargs):
        """Provides BFD links for device.

        Args:
            system_ip (str): Device System IP
            state (str): (Optional) State

        Returns:
            result (dict): Device BFD links data.
        """

        url = f"{self.base_url}device/bfd/links"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'state' in kwargs:
            query_params.append(('state', kwargs['state']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_sessions(self, system_ip, **kwargs):
        """Provides BFD sessions for device.

        Args:
            system_ip (str): Device System IP
            remote_system_ip (str): (Optional) Remote System IP
            remote_color (str): (Optional) Remote Color
            local_color (str): (Optional) Local Color

        Returns:
            result (dict): Device BFD sessions data.
        """

        url = f"{self.base_url}device/bfd/sessions"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'remote_system_ip' in kwargs:
            query_params.append(('system-ip', kwargs['remote_system_ip']))
        if 'remote_color' in kwargs:
            query_params.append(('color', kwargs['remote_color']))
        if 'local_color' in kwargs:
            query_params.append(('local-color', kwargs['local_color']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_device_state(self, system_ip):
        """Provides BFD state for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device BFD state data.
        """

        url = f"{self.base_url}/device/bfd/state/device?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_device_state_tloc(self, system_ip):
        """Provides BFD state summary with TLOC for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device BFD state summary with TLOC data.
        """

        url = f"{self.base_url}/device/bfd/state/device/tloc?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_summary(self, system_ip):
        """Provides BFD summary data for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device BFD summary data.
        """

        url = f"{self.base_url}device/bfd/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bfd_tloc(self, system_ip):
        """Provides BFD TLOC for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device BFD TLOC data.
        """

        url = f"{self.base_url}device/bfd/tloc?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bgp_neighbors(self, system_ip, **kwargs):
        """Provides BGP neighbors for device.

        Args:
            system_ip (str): Device System IP
            vpn-id (str): VPN ID
            peer-addr (str): Peer address
            as (str): ASN

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/bgp/neighbors"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'peer_addr' in kwargs:
            query_params.append(('peer-addr', kwargs['peer_addr']))
        if 'asn' in kwargs:
            query_params.append(('as', kwargs['asn']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_bgp_routes(self, system_ip, **kwargs):
        """Provides BGP routes for device.

        Args:
            system_ip (str): Device System IP
            vpn-id (str): VPN ID
            prefix (str): IP prefix
            nexthop (str): Nexthop

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/bgp/routes"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'prefix' in kwargs:
            query_params.append(('prefix', kwargs['prefix']))
        if 'nexthop' in kwargs:
            query_params.append(('nexthop', kwargs['nexthop']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_bgp_summary(self, system_ip):
        """Provides BGP summary for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/bgp/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_connections(self, system_ip):
        """Provides celluar connection information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/connection?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_hardware(self, system_ip):
        """Provides celluar hardware information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/hardware?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_modems(self, policy_id):
        """Provides celluar modem information for device.

        Args:
            policy_id (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/modem?policyId={policy_id}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_networks(self, system_ip):
        """Provides celluar network information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/network?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_profiles(self, system_ip):
        """Provides celluar profile information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/profiles?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_radios(self, system_ip):
        """Provides celluar radio information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/radio?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_sessions(self, system_ip, **kwargs):
        """Provides celluar session information for device.

        Args:
            system_ip (str): Device System IP
            interface_name (str): Interface name values: ge0/0 - ge0/7, system, , eth0
            primary_dns_ipv4 (str): Primary DNS IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/sessions"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'interface_name' in kwargs:
            query_params.append(('if-name', kwargs['interface_name']))
        if 'primary_dns_ipv4' in kwargs:
            query_params.append(('ipv4-dns-pri', kwargs['primary_dns_ipv4']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_cellular_status(self, system_ip):
        """Provides celluar status information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/cellular/status?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_affinity_config(self, system_ip):
        """Provides current control affinity config for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/affinity/config?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_affinity_status(self, system_ip):
        """Provides current control affinity status for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/affinity/status?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_connections(self, system_ip, **kwargs):
        """Provides current control connections for device.

        Args:
            system_ip (str): Device System IP
            peer_type (str): Peer type (vedge, vsmart, vmanage, vbond)
            peer_system_ip (str): Peer System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/control/connections"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'peer_type' in kwargs:
            query_params.append(('peer-type', kwargs['peer_type']))
        if 'peer_system_ip' in kwargs:
            query_params.append(('system-ip', kwargs['peer_system_ip']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_connections_history(self, system_ip, **kwargs):
        """Provides control connections history for device.

        Args:
            system_ip (str): Device System IP
            peer_type (str): Peer type (vedge, vsmart, vmanage, vbond)
            peer_system_ip (str): Peer System IP
            local_color (str): Local Color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/control/connectionshistory"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'peer_type' in kwargs:
            query_params.append(('peer-type', kwargs['peer_type']))
        if 'peer_system_ip' in kwargs:
            query_params.append(('system-ip', kwargs['peer_system_ip']))
        if 'local_color' in kwargs:
            query_params.append(('local-color', kwargs['local_color']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_count(self):
        """Provides current control count for device.

        Args:
            None (None):

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/control/count"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_links(self, system_ip, **kwargs):
        """Provides control links for device.

        Args:
            system_ip (str): Device System IP
            state (str): State

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/control/links"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'state' in kwargs:
            query_params.append(('state', kwargs['state']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_local_properties(self, system_ip):
        """Provides control local properties history for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/localproperties?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_summary(self, system_ip):
        """Provides current control summary for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/control/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_valid_devices(self, system_ip):
        """Provides control valid devices for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/validdevices?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_valid_vsmarts(self, system_ip):
        """Provides control valid vsmarts for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/validvsmarts?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_wan_interface(self, system_ip):
        """Provides current control wan interface for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/waninterface?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_control_wan_interface_color(self, system_ip):
        """Provides current control wan interface for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/control/waninterface/color?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_device_status(self, system_ip):
        """Provides status for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/system/status?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_device_system_info(self, system_ip):
        """Provides system info for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/system/info?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dhcp_clients(self, system_ip):
        """Provides dhcp clients for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dhcp/client?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dhcp_interfaces(self, system_ip):
        """Provides dhcp interfaces for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/dhcp/interfaces?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dhcp_servers(self, system_ip):
        """Provides dhcp servers for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dhcp/server?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dot1x_clients(self, system_ip):
        """Provides DOT1X clients for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dot1x/clients?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dot1x_interfaces(self, system_ip):
        """Provides DOT1X interfaces for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dot1x/interfaces?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dot1x_radius(self, system_ip):
        """Provides DOT1X RADIUS information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dot1x/radius?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_applications(self, system_ip, **kwargs):
        """Provides DPI application information for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN/VRF ID
            application (str): Application
            family (str): Family

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/applications"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'application' in kwargs:
            query_params.append(('application', kwargs['application']))
        if 'family' in kwargs:
            query_params.append(('family', kwargs['family']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_common_applications(self):
        """Provides common DPI application information.

        Args:
            None (None): None

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/common/applications"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_device_fields(self):
        """Provides DPI fields for device.

        Args:
            None (None): None

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/device/fields"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_device_fields_details(self):
        """Provides DPI detailed fields for device.

        Args:
            None (None): None

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/devicedetails/fields"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_flows(self, system_ip, **kwargs):
        """Provides DPI application information for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN/VRF ID
            source_ip (str): Source IP
            application (str): Application
            family (str): Family

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/flows"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'source_ip' in kwargs:
            query_params.append(('src-ip', kwargs['source_ip']))
        if 'application' in kwargs:
            query_params.append(('application', kwargs['application']))
        if 'family' in kwargs:
            query_params.append(('family', kwargs['family']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_summary(self, system_ip):
        """Provides DPI summary information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_dpi_supported_applications(self, system_ip, **kwargs):
        """Provides DPI supported application information for device.

        Args:
            system_ip (str): Device System IP
            application (str): Application
            family (str): Family

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/dpi/supported-applications"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'application' in kwargs:
            query_params.append(('application', kwargs['application']))
        if 'family' in kwargs:
            query_params.append(('family', kwargs['family']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_eigrp_interfaces(self, system_ip):
        """Provides EIGRP interface for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'cisco-router':
            url = f"{self.base_url}device/eigrp/interface?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_eigrp_routes(self, system_ip):
        """Provides EIGRP route for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'cisco-router':
            url = f"{self.base_url}device/eigrp/route?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_eigrp_topology(self, system_ip):
        """Provides EIGRP topology for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'cisco-router':
            url = f"{self.base_url}device/eigrp/topology?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_hardware_alarms(self, system_ip):
        """Provides hardware alarms for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/hardware/alarms?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_hardware_environment(self, system_ip):
        """Provides hardware environment information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/hardware/environment?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_hardware_inventory(self, system_ip):
        """Provides hardware inventory information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/hardware/inventory?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_hardware_status_summary(self, system_ip):
        """Provides hardware status summary information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/hardware/status/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_hardware_system(self, system_ip):
        """Provides hardware system information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/hardware/system?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_igmp_groups(self, system_ip):
        """Provides IGMP groups information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/igmp/groups?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_igmp_interfaces(self, system_ip):
        """Provides IGMP interfaces information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/igmp/interface?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_igmp_statistics(self, system_ip):
        """Provides IGMP statistics information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/igmp/statistics?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_igmp_summary(self, system_ip):
        """Provides IGMP summary information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/igmp/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_interface_vpn(self, system_ip):
        """Provides interface vpn/vrf information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/interface/vpn?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ip_fib(self, system_ip, **kwargs):
        """Provides IP FIB for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN ID
            address_family (str): Address Family
            destination_prefix (str): Destination Prefix
            tloc (str): TLOC
            color (str): TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ip/fib"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('routing-instance-name', kwargs['vpn_id']))
        if 'address_family' in kwargs:
            query_params.append(('rib-address-family', kwargs['address_family']))
        if 'destination_prefix' in kwargs:
            query_params.append(('route-destination-prefix', kwargs['destination_prefix']))
        if 'tloc' in kwargs:
            query_params.append(('tloc', kwargs['tloc']))
        if 'color' in kwargs:
            query_params.append(('color', kwargs['color']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_ip_route_table(self, system_ip, **kwargs):
        """Provides IP route table for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN ID
            address_family (str): Address Family
            destination_prefix (str): Destination Prefix
            source_protocol (str): Source Protocol
            next_hop_address (str): Next-Hop Address (cEdge Only)
            next_hop_oif (str): Next-Hop Outgoing Interface (cEdge Only)

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        query_params = []
        query_params.append(('deviceId', system_ip))
        if device_type == 'cisco-router':
            url = f"{self.base_url}device/ip/ipRoutes"
            if 'vpn_id' in kwargs:
                query_params.append(('routing-instance-name', kwargs['vpn_id']))
            if 'address_family' in kwargs:
                query_params.append(('rib-address-family', kwargs['address_family']))
            if 'destination_prefix' in kwargs:
                query_params.append(('route-destination-prefix', kwargs['destination_prefix']))
            if 'source_protocol' in kwargs:
                query_params.append(('route-source-protocol', kwargs['source_protocol']))
            if 'next_hop_address' in kwargs:
                query_params.append(('next-hop-next-hop-address', kwargs['next_hop_address']))
            if 'next_hop_oif' in kwargs:
                query_params.append(('next-hop-outgoing-interface', kwargs['next_hop_oif']))
        elif device_type == 'viptela-router':
            url = f"{self.base_url}device/ip/routetable"
            if 'vpn_id' in kwargs:
                query_params.append(('vpn-id', kwargs['vpn_id']))
            if 'address_family' in kwargs:
                query_params.append(('address-family', kwargs['address_family']))
            if 'destination_prefix' in kwargs:
                query_params.append(('prefix', kwargs['destination_prefix']))
            if 'source_protocol' in kwargs:
                query_params.append(('protocol', kwargs['source_protocol']))
        else:
            raise Exception(f"Could not retrieve device type {device_type} for {system_ip}")
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_ip_nat_translations(self, system_ip):
        """Provides IP NAT translations for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ip/nat/translation?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ip_nat64_translations(self, system_ip):
        """Provides IP NAT64 translations for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ip/nat64/translation?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_inbound_connections(self, system_ip, **kwargs):
        """Provides IPSec inbound connections for device.

        Args:
            system_ip (str): Device System IP
            remote_tloc_address (str): Remote TLOC address
            remote_tloc_color (str): Remote TLOC color
            local_tloc_color (str): Local TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/inbound"
        query_params = []
        query_params.append(('deviceId', system_ip))
        url += '?' + urlencode(self._ipsec_query_params(query_params, **kwargs))
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_localsa(self, system_ip):
        """Provides IPSec localsa for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/localsa?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_outbound_connections(self, system_ip, **kwargs):
        """Provides IPSec outbound connections for device.

        Args:
            system_ip (str): Device System IP
            remote_tloc_address (str): Remote TLOC address
            remote_tloc_color (str): Remote TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/outbound"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'remote_tloc_address' in kwargs:
            query_params.append(('remote-tloc-address', kwargs['remote_tloc_address']))
        if 'remote_tloc_color' in kwargs:
            query_params.append(('remote-tloc-color', kwargs['remote_tloc_color']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_pwk_inbound_connections(self, system_ip, **kwargs):
        """Provides IPSec pairwise key inbound connections for device.

        Args:
            system_ip (str): Device System IP
            remote_tloc_address (str): Remote TLOC address
            remote_tloc_color (str): Remote TLOC color
            local_tloc_color (str): Local TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/pwk/inbound"
        query_params = []
        query_params.append(('deviceId', system_ip))
        url += '?' + urlencode(self._ipsec_query_params(query_params, **kwargs))
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_pwk_localsa(self, system_ip, **kwargs):
        """Provides IPSec pairwise key localsa for device.

        Args:
            system_ip (str): Device System IP
            remote_tloc_address (str): Remote TLOC address
            remote_tloc_color (str): Remote TLOC color
            local_tloc_color (str): Local TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/pwk/localsa"
        query_params = []
        query_params.append(('deviceId', system_ip))
        url += '?' + urlencode(self._ipsec_query_params(query_params, **kwargs))
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ipsec_pwk_outbound_connections(self, system_ip, **kwargs):
        """Provides IPSec pairwise key outbound connections for device.

        Args:
            system_ip (str): Device System IP
            remote_tloc_address (str): Remote TLOC address
            remote_tloc_color (str): Remote TLOC color
            local_tloc_color (str): Local TLOC color

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ipsec/pwk/outbound"
        query_params = []
        query_params.append(('deviceId', system_ip))
        url += '?' + urlencode(self._ipsec_query_params(query_params, **kwargs))
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_multicast_replicator(self, system_ip):
        """Provides multicast replicator for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/mulitcast/replicator?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_multicast_rpf(self, system_ip):
        """Provides multicast rpf for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/mulitcast/rpf?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_multicast_topology(self, system_ip):
        """Provides multicast topology for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/mulitcast/topology?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_multicast_tunnel(self, system_ip):
        """Provides multicast tunnel for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/mulitcast/tunnel?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_omp_peers(self, system_ip):
        """Provides OMP peers for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/omp/peers?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_omp_routes_received(self, system_ip, **kwargs):
        """Provides OMP received routes for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN ID
            prefix (str): Prefix

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/omp/routes/received"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'prefix' in kwargs:
            query_params.append(('prefix', kwargs['prefix']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_omp_routes_advertised(self, system_ip, **kwargs):
        """Provides OMP advertised routes for device.

        Args:
            system_ip (str): Device System IP
            vpn_id (str): VPN ID
            prefix (str): Prefix

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/omp/routes/advertised"
        query_params = []
        query_params.append(('deviceId', system_ip))
        if 'vpn_id' in kwargs:
            query_params.append(('vpn-id', kwargs['vpn_id']))
        if 'prefix' in kwargs:
            query_params.append(('prefix', kwargs['prefix']))
        url += '?' + urlencode(query_params)
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_omp_summary(self, system_ip):
        """Provides OMP summary for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/omp/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_orchestrator_summary(self, system_ip):
        """Provides orchestrator (vbond) summary for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/orchestrator/summary?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_orchestrator_connections(self, system_ip):
        """Provides orchestrator (vbond) connections for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/orchestrator/connections?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_orchestrator_connections_history(self, system_ip):
        """Provides orchestrator (vbond) connections history for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/orchestrator/connections?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_orchestrator_local_properties(self, system_ip):
        """Provides orchestrator (vbond) local properties history for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}" \
              f"device/orchestrator/localproperties?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_interfaces(self, system_ip):
        """Provides OSPF interfaces for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ospf/interface?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_neighbors(self, system_ip):
        """Provides OSPF neighbors for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/ospf/neighbor?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_routes(self, system_ip):
        """Provides OSPF routes for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/ospf/routes?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET', timeout=60)
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_database(self, system_ip):
        """Provides OSPF database for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/ospf/database?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_database_summary(self, system_ip):
        """Provides OSPF database summary for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}" \
              f"device/ospf/databasesummary?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_process(self, system_ip):
        """Provides OSPF process for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}device/ospf/process?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_ospf_database_external(self, system_ip):
        """Provides OSPF database external for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        device_type = self._get_device_type(system_ip)
        if device_type == 'viptela-router':
            url = f"{self.base_url}" \
              f"device/ospf/databaseexternal?deviceId={system_ip}"
        else:
            raise Exception(f"Device type {device_type} for {system_ip} is not valid for this API endpoint.")
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_pim_interfaces(self, system_ip):
        """Provides PIM interfaces for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/pim/interface?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_pim_neighbors(self, system_ip):
        """Provides PIM neighbors for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/pim/neighbor?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_pim_rp_mapping(self, system_ip):
        """Provides PIM RP mapping for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/pim/rp-mapping?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_pim_statistics(self, system_ip):
        """Provides PIM statistics for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/pim/statistics?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_security_information(self, system_ip):
        """Provides security information for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/security/information?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_software(self, system_ip):
        """Provides software for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/software?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_umbrella_sig_tunnels(self, system_ip):
        """Provides Cisco Umbrella SIG tunnels for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/sig/umbrella/tunnels?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_users(self, system_ip):
        """Provides users for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device ARP table data.
        """

        url = f"{self.base_url}device/users?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_users_list(self, system_ip):
        """Provides users list for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): Device ARP table data.
        """

        url = f"{self.base_url}device/users/list?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_vrrp(self, system_ip):
        """Provides VRRP entries for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/vrrp?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_wlan_clients(self, system_ip):
        """Provides WLAN clients for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/wlan/clients?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_wlan_interfaces(self, system_ip):
        """Provides WLAN interfaces for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/wlan/interfaces?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_wlan_radios(self, system_ip):
        """Provides WLAN radios for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/wlan/radios?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_wlan_radius(self, system_ip):
        """Provides WLAN RADIUS authenticiation for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/wlan/radius?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result

    def get_zscaler_sig_tunnels(self, system_ip):
        """Provides Cisco zScaler SIG tunnels for device.

        Args:
            system_ip (str): Device System IP

        Returns:
            result (dict): All data associated with a response.
        """

        url = f"{self.base_url}device/sig/zscaler/tunnels?deviceId={system_ip}"
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_data(response)
        return result
