from ckan import plugins as p


def no_registering(context, data_dict):
    return {
        'success': False,
        'msg': p.toolkit._(
            'You cannot register for this site.'
        )
    }


class NoSelfRegistration(p.SingletonPlugin):
    p.implements(p.IAuthFunctions, inherit=True)
    p.implements(p.IConfigurer)

    def get_auth_functions(self):
        return {
            'user_create': no_registering
        }

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
