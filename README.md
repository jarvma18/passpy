# Passpy

Passpy is a lightweight password manager designed to securely store and manage your passwords. With Passpy, you can easily generate strong, unique passwords for all your online accounts and keep them organized in one place.

## Features

- Securely store and encrypt passwords
- Generate strong, random passwords
- Search and retrieve passwords quickly
- Auto-fill passwords in web browsers
- Backup and restore password database

## About storage

- Encrypted JSON file
- Structure:
  ```
    "uuid": {
      "username": "x",
      "password": "y"
    },
    "uuid": {},
    ...
  ```

## How to run in development

```
# install PyCryptodome
pip3 install -U PyCryptodome

# tests
python3 -m unittesst
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-username/passpy/blob/main/LICENSE) file for more information.
