def traverse_nested_config(config_dict, path_str, default=None):
    if not path_str or not isinstance(config_dict, dict):
        return default

    keys = path_str.split(".")

    try:
        value = config_dict

        for key in keys:
            value = value[key]

        return value

    except (KeyError, TypeError, AttributeError):
        return default


def main():
    config = {
        "server": {
            "host": "127.0.0.1",
            "port": 8080,
            "ssl": {
                "enabled": True,
                "cert_path": "/etc/ssl/certs"
            }
        },
        "database": "postgresql://localhost:5432"
    }

    print(traverse_nested_config(config, "server.ssl.cert_path"))
    print(traverse_nested_config(config, "server.database.username", "guest"))
    print(traverse_nested_config(config, "database.host", "localhost"))


main()
