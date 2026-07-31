### Assignment

Just To Finish The Task

### Completed Work

- Added a `before_save` method to the custom DocType controller so `description` falls back to `Default Description` when empty.
- Configured `doc_events` in `hooks.py` to trigger a custom function on a standard DocType.
- Added the custom Python function that shows `frappe.msgprint("Hook executed!")`.

### Submission

Repository URL: https://github.com/dharanidharansr/Frappe-Assignment.git

Commit URL: https://github.com/dharanidharansr/Frappe-Assignment/commit/00da1c1e1b8d0d0a70b66780a62eeafdd2e00ba2

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app assignment
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/assignment
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
