commands = {"helpCog": ["help"]}


def register_commands(cog):
    commands_list = []
    for method in dir(cog):
        if method in [
            'bot', 'bot_check', 'bot_check_once', 'cog_after_invoke', 'cog_before_invoke', 'cog_check',
            'cog_command_error', 'cog_unload', 'description', 'file', 'get_commands', 'get_listeners',
            'has_error_handler', 'ids', 'listener', 'pickle', 'qualified_name', 'to_register', 'walk_commands'
        ]:
            continue

        if method.startswith('_'):
            continue

        commands_list.append(method)

    commands[cog.__class__.__name__] = commands_list