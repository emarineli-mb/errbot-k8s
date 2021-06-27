from errbot import BotPlugin, botcmd, arg_botcmd, webhook
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException

import yaml


class ErrbotK8S(BotPlugin):
    """
    K8S utilities
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(ErrbotK8S, self).activate()

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def list(self, message, args):

        config.load_incluster_config()

        v1 = client.CoreV1Api()
        print("Listing pods with their IPs:")
        ret = v1.list_pod_for_all_namespaces(watch=False)

        str = ""
        for i in ret.items:
            str += i.metadata.name

            return str
