<h2>About the connector</h2>

<p>Google Compute Engine's tooling and workflow supports to create advanced networks on the regional levels and load balancing capabilities in cloud computing. This connector facilitates automated operation related to GCE operations.</p>

<p>This document provides information about the Google Cloud Compute Connector, which facilitates automated interactions, with a Google Cloud Compute server using FortiSOAR&trade; playbooks. Add the Google Cloud Compute Connector as a step in FortiSOAR&trade; playbooks and perform automated operations,</p>

<h3>Version information</h3>

<p>Connector Version: 1.1.0</p>

<p>Authored By: Fortinet CSE</p>

<p>Contributors: Derrick Gooch</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>

<p><code>yum install cyops-connector-google-cloud-compute</code></p>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the URL of Google Cloud Compute server to which you will connect and perform automated operations and credentials to access that server.</li>
<li>To access the FortiSOAR&trade; UI, ensure that port 443 is open through the firewall for the FortiSOAR&trade; instance.</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Google Cloud Compute</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Upload Service Account JSON File<br></td><td>The service account private key file.<br>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:</p>

<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>List Instances within Zone<br></td><td>Retrieves the list of instances contained within the specified zone.<br></td><td>list_instances_within_zone <br/>Investigation<br></td></tr>
<tr><td>Get Instance Details<br></td><td>Returns the specified Instance resource details.<br></td><td>describe_instance <br/>Investigation<br></td></tr>
<tr><td>Start Instance<br></td><td>Starts an instance that you have specified using the resource ID.<br></td><td>start_instance <br/>Miscellaneous<br></td></tr>
<tr><td>Stop Instance<br></td><td>Stops an instance that you have specified using the resource ID.<br></td><td>stop_instance <br/>Miscellaneous<br></td></tr>
<tr><td>Delete Instance<br></td><td>Deletes an instance resource that you have specified using the resource ID.<br></td><td>delete_instance <br/>Miscellaneous<br></td></tr>
<tr><td>Reset Instance<br></td><td>This is a hard reset the VM does not do a graceful shutdown. Performs a reset on the instance that you have specified using the resource ID.<br></td><td>reset_instance <br/>Miscellaneous<br></td></tr>
<tr><td>Aggregated List Instances<br></td><td>Retrieves an aggregated list of all of the instances in your project across all regions and zones.<br></td><td>get_aggregated_list_instances <br/>Investigation<br></td></tr>
<tr><td>Set Instance Label<br></td><td>Set user defined labels on a Specified instance<br></td><td>set_device_label <br/>Investigation<br></td></tr>
</tbody></table>

<h3>operation: List Instances within Zone</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Filter<br></td><td>A filter expression that filters resources listed in the response.<br>
</td></tr><tr><td>OrderBy<br></td><td>Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.<br>
</td></tr><tr><td>Page Token<br></td><td>Specifies a page token to use.<br>
</td></tr><tr><td>Max Results<br></td><td>The maximum number of results per page that should be returned. Acceptable values are 0 to 500, inclusive. (Default: 500)<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "items": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nextPageToken": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warning": {}
</code><code><br>}</code></p>

<h3>operation: Get Instance Details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Resource ID<br></td><td>Name of the instance resource to return.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creationTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "tags": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "machineType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "statusMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "canIpForward": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "networkInterfaces": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "disks": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "metadata": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "serviceAccounts": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "scheduling": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "cpuPlatform": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "labels": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "params": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "labelFingerprint": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "minCpuPlatform": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "guestAccelerators": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "startRestricted": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "deletionProtection": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "resourcePolicies": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sourceMachineImage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "reservationAffinity": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "hostname": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "displayDevice": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "shieldedInstanceConfig": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "shieldedInstanceIntegrityPolicy": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sourceMachineImageEncryptionKey": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "confidentialInstanceConfig": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "fingerprint": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "privateIpv6GoogleAccess": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "advancedMachineFeatures": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "lastStartTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "lastStopTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "lastSuspendedTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "satisfiesPzs": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "networkPerformanceConfig": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "keyRevocationActionType": ""
</code><code><br>}</code></p>

<h3>operation: Start Instance</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Resource ID<br></td><td>Name of the instance resource to return.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creationTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "clientOperationId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "statusMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "progress": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "insertTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "startTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "endTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "error": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warnings": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorStatusCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "region": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationGroupId": ""
</code><code><br>}</code></p>

<h3>operation: Stop Instance</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Resource ID<br></td><td>Name of the instance resource to return.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creationTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "clientOperationId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "statusMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "progress": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "insertTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "startTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "endTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "error": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warnings": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorStatusCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "region": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationGroupId": ""
</code><code><br>}</code></p>

<h3>operation: Delete Instance</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Resource ID<br></td><td>Name of the instance resource to return.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creationTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "clientOperationId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "statusMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "progress": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "insertTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "startTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "endTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "error": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warnings": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorStatusCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "region": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationGroupId": ""
</code><code><br>}</code></p>

<h3>operation: Reset Instance</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Zone<br></td><td>The name of the zone for this request.<br>
</td></tr><tr><td>Resource ID<br></td><td>Name of the instance resource to return.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "creationTimestamp": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "zone": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "clientOperationId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationType": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "targetId": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "status": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "statusMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "user": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "progress": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "insertTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "startTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "endTime": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "error": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warnings": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorStatusCode": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "httpErrorMessage": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "region": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "description": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "operationGroupId": ""
</code><code><br>}</code></p>

<h3>operation: Aggregated List Instances</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Include all scopes<br></td><td>Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.<br>
</td></tr><tr><td>Filter<br></td><td>A filter expression that filters resources listed in the response.<br>
</td></tr><tr><td>OrderBy<br></td><td>Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.<br>
</td></tr><tr><td>Page Token<br></td><td>Specifies a page token to use.<br>
</td></tr><tr><td>Max Results<br></td><td>The maximum number of results per page that should be returned.<br>
</td></tr><tr><td>Return partial success<br></td><td>Opt-in for partial success behavior which provides partial results in  case of failure. The default value is false.<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "items": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nextPageToken": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warning": {},
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "unreachables": []
</code><code><br>}</code></p>

<h3>operation: Set Instance Label</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Instance Name<br></td><td>Specify the name of the instance for this request<br>
</td></tr><tr><td>Zone<br></td><td>Specify the name of the zone for this request<br>
</td></tr><tr><td>Key Name<br></td><td>Specify the key of the Label<br>
</td></tr><tr><td>Key Value<br></td><td>Specify the value of the Label<br>
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p><code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "kind": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "items": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "nextPageToken": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "selfLink": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "warning": {}
</code><code><br>}</code></p>

<h2>Included playbooks</h2>

<p>The <code>Sample - google-cloud-compute - 1.1.0</code> playbook collection comes bundled with the Google Cloud Compute connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR<sup>TM</sup> after importing the Google Cloud Compute connector.</p>

<ul>
<li>List Instances within Zone</li>
<li>Get Instance Details</li>
<li>Start Instance</li>
<li>Stop Instance</li>
<li>Delete Instance</li>
<li>Reset Instance</li>
<li>Aggregated List Instances</li>
<li>Set Instance Label</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.</p>
