""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import json
import sys
import google.cloud.compute_v1 as compute
import google.api_core.retry as retry
from google.api_core.exceptions import NotFound
from google.oauth2 import service_account
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('google-cloud-compute')


class GoogleCloudCompute(object):

    def __init__(self, config):
        self.client_details = dict()
        json_file_contents = config.get('auth')
        scopes = ['https://www.googleapis.com/auth/cloud-platform']
        auth_contents = str(json_file_contents).replace("\'", "\"").replace("\\\\", "\\")
        self.auth_details = json.loads(auth_contents)
        self.p_id = self.auth_details.get('project_id')
        self.credentials = service_account.Credentials.from_service_account_info(
            self.auth_details, scopes=scopes)

    def create_clients(self):
        try:
            image_client = compute.ImagesClient(credentials=self.credentials)
            ins_client = compute.InstancesClient(credentials=self.credentials)
            zo_client = compute.ZoneOperationsClient(credentials=self.credentials)
            mt_client = compute.MachineTypesClient(credentials=self.credentials)
            nw_client = compute.NetworksClient(credentials=self.credentials)
            add_client = compute.AddressesClient(credentials=self.credentials)
            go_client = compute.GlobalOperationsClient(credentials=self.credentials)
            ro_client = compute.RegionOperationsClient(credentials=self.credentials)
            ga_client = compute.GlobalAddressesClient(credentials=self.credentials)
            disks_client = compute.DisksClient(credentials=self.credentials)
            dt_client = compute.DiskTypesClient(credentials=self.credentials)
            ig_client = compute.InstanceGroupsClient(credentials=self.credentials)
            reg_client = compute.RegionsClient(credentials=self.credentials)
            zone_client = compute.ZonesClient(credentials=self.credentials)
            f_client = compute.FirewallsClient(credentials=self.credentials)
            snap_client = compute.SnapshotsClient(credentials=self.credentials)
            proj_client = compute.ProjectsClient(credentials=self.credentials)
            self.client_details['images_client'] = image_client
            self.client_details['instances_client'] = ins_client
            self.client_details['zone_operations_client'] = zo_client
            self.client_details['machine_types_client'] = mt_client
            self.client_details['networks_client'] = nw_client
            self.client_details['addresses_client'] = add_client
            self.client_details['global_operations_client'] = go_client
            self.client_details['region_operations_client'] = ro_client
            self.client_details['global_addresses_client'] = ga_client
            self.client_details['disks_client'] = disks_client
            self.client_details['disk_types_client'] = dt_client
            self.client_details['instance_groups_client'] = ig_client
            self.client_details['regions_client'] = reg_client
            self.client_details['zones_client'] = zone_client
            self.client_details['firewalls_client'] = f_client
            self.client_details['snapshots_client'] = snap_client
            self.client_details['projects_client'] = proj_client
        except Exception as e:
            logger.exception(
                'Failed to get clients. Please check the service account json contents for authentication.')
            raise ConnectorError('Error: {0}'.format(e))

    def make_client_call(self, client_types, health_check=False):
        clients = dict()
        if not self.client_details:
            logger.info("Creating different clients.")
            self.create_clients()
        if health_check and not self.client_details:
            logger.error("Failed to create clients. Make sure the provided credentials are correct.")
            raise ConnectorError("Connector is not available. Health check failed.")
        for typ in client_types:
            clients[typ] = self.client_details[typ]
        return clients

    @retry.Retry()
    def list_instances_within_zone(self, params):
        zone = params.get('zone')
        sub_filter = params.get('filter')
        order_by = params.get('order_by')
        page_token = params.get('page_token')
        max_results = params.get('max_results')
        client_types = ['instances_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        request = compute.ListInstancesRequest(
            project=self.p_id, zone=zone, filter=sub_filter,
            order_by=order_by, page_token=page_token,
            max_results=max_results)
        instances = ins_client.list(request=request)
        data_res = []
        for instance in instances:
            data_res_item = {
                'id': instance.id,
                'name': instance.name,
                'createTime': instance.creation_timestamp,
                'machineType': instance.machine_type,
                'zone': instance.zone
            }
            data_res.append(data_res_item)
        return data_res

    @retry.Retry()
    def describe_instance(self, params):
        zone = params.get('zone')
        instance = params.get('resource_id')
        client_types = ['instances_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        instance_info = ins_client.get(project=self.p_id, zone=zone, instance=instance)
        logger.info('Instance details: {0}'.format(str(instance_info)))
        return str(instance_info)

    @retry.Retry()
    def start_instance(self, params):
        zone = params.get('zone')
        instance = params.get('resource_id')
        client_types = ['instances_client', 'zone_operations_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        op_client = clients[client_types[1]]
        op = ins_client.start_unary(project=self.p_id, zone=zone, instance=instance)
        while op.status != compute.Operation.Status.DONE:
            op = op_client.wait(operation=op.name, zone=zone, project=self.p_id)
        logger.info('VM started successfully.')
        return str(op)

    @retry.Retry()
    def stop_instance(self, params):
        zone = params.get('zone')
        instance = params.get('resource_id')
        client_types = ['instances_client', 'zone_operations_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        op_client = clients[client_types[1]]
        op = ins_client.stop_unary(project=self.p_id,
                                   zone=zone,
                                   instance=instance)
        while op.status != compute.Operation.Status.DONE:
            op = op_client.wait(operation=op.name,
                                zone=zone,
                                project=self.p_id)
        logger.info('VM is stopped successfully.')
        return str(op)

    def delete_instance(self, params):
        zone = params.get('zone')
        instance = params.get('resource_id')
        client_types = ['instances_client', 'zone_operations_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        op_client = clients[client_types[1]]
        # NOTE: Handling NotFound error for python module version compatibility.
        try:
            op = ins_client.delete_unary(project=self.p_id,
                                         zone=zone,
                                         instance=instance)
            while op.status != compute.Operation.Status.DONE:
                op = op_client.wait(operation=op.name,
                                    zone=zone,
                                    project=self.p_id)
            if op.error:
                print('Error during deletion:', op.error, file=sys.stderr)
            if op.warnings:
                print('Warning during deletion:', op.warnings, file=sys.stderr)
        except NotFound as e:
            logger.info('VM is not Found.')
        logger.info('VM deleted successfully.')
        return str(op)

    def reset_instance(self, params):
        zone = params.get('zone')
        instance = params.get('resource_id')
        client_types = ['instances_client', 'zone_operations_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        op_client = clients[client_types[1]]
        logger.info('Reset the VM instance.')
        op = ins_client.reset_unary(project=self.p_id,
                                    zone=zone,
                                    instance=instance)
        while op.status != compute.Operation.Status.DONE:
            op = op_client.wait(operation=op.name,
                                zone=zone,
                                project=self.p_id)
        logger.info('VM is reset successfully.')
        return str(op)

    @retry.Retry()
    def get_aggregated_list_instances(self, params):
        all_scopes = params.get('include_all_scopes')
        sub_filter = params.get('filter')
        order_by = params.get('order_by')
        page_token = params.get('page_token')
        max_results = params.get('max_results')
        partial_success = params.get('return_partial_success')
        client_types = ['instances_client']
        clients = self.make_client_call(client_types)
        ins_client = clients[client_types[0]]
        request = compute.AggregatedListInstancesRequest(
            filter=sub_filter, include_all_scopes=all_scopes,
            max_results=max_results, order_by=order_by,
            page_token=page_token, project=self.p_id,
            return_partial_success=partial_success)
        instances = ins_client.aggregated_list(request=request)
        data_res = []
        for instance in instances:
            if 'warning' not in str(instance[1]):
                data_res.append(str(instance[1]))
        return data_res


def _run_operation(config, params):
    compute_obj = GoogleCloudCompute(config)
    command = getattr(GoogleCloudCompute, params['operation'])
    response = command(compute_obj, params)
    return response


def _check_health(config):
    compute_obj = GoogleCloudCompute(config)
    logger.info('Checking Health check.')
    return compute_obj.make_client_call(['instances_client'], True)

