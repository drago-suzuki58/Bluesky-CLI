import configparser

def load_config(file="config/config.ini"):
    config = configparser.ConfigParser()
    config.read(file)

    config_values = {}
    for section in config.sections():
        for key, val in config.items(section):
            config_values[key] = val

    return config_values

def save_config(config_values, file="config/config.ini"):
    config = configparser.ConfigParser()

    for key, val in config_values.items():
        section, _, key = key.partition('.')
        if not config.has_section(section):
            config.add_section(section)
        config.set(section, key, val)

    with open(file, 'w') as configfile:
        config.write(configfile)


def edit_config():
    config_values = load_config()

    save_config(config_values)

    print("Config updated.")