# shipstation-client

<div align="center">

[![Build status](https://github.com/agritheory/shipstation-client/workflows/build/badge.svg?branch=master&event=push)](https://github.com/agritheory/shipstation-client/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/shipstation-client.svg)](https://pypi.org/project/shipstation-client/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/agritheory/shipstation-client/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/agritheory/shipstation-client/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/agritheory/shipstation-client/releases)
[![License](https://img.shields.io/github/license/agritheory/shipstation-client)](https://github.com/agritheory/shipstation-client/blob/master/LICENSE)

`shipstation-client` is a Python cli/package created with https://github.com/TezRomacH/python-package-template
</div>

---

## 🚀 Features

For your development we've prepared:

- Supports for `Python 3.10` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/agritheory/shipstation-client/blob/master/pyproject.toml).
- Power of [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade) formatters.
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with formatters above.
- Type checks with the configured [`mypy`](https://mypy.readthedocs.io).
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).
- Security checks with [`bandit`](https://github.com/PyCQA/bandit).
- Well-made [`.editorconfig`](https://github.com/agritheory/shipstation-client/blob/master/.editorconfig) and [`.gitignore`](https://github.com/agritheory/shipstation-client/blob/master/.gitignore). You don't have to worry about those things.

For building and deployment:

- `GitHub` integration.
- [`Makefile`](https://github.com/agritheory/shipstation-client/blob/master/Makefile#L89) for building routines. Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc. More details at [Makefile summary](#makefile-usage)).
- [Dockerfile](https://github.com/agritheory/shipstation-client/blob/master/docker/Dockerfile) for your package.
- `Github Actions` with predefined [build workflow](https://github.com/agritheory/shipstation-client/blob/master/.github/workflows/build.yml) as the default CI/CD.

---

### Setup [Poetry](https://python-poetry.org/docs/)

1. Initialize `git` inside your repo:

```bash
git init
```

2. If you don't have `Poetry` installed, run:

```bash
make download-poetry
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
```

## Installation

```bash
pip install shipstation-client
```

or install with `Poetry`

```bash
poetry add shipstation-client
```

## Usage

Then you can run

```bash
shipstation-client --help
```

```bash
shipstation-client --name Roman
```

or if installed with `Poetry`:

```bash
poetry run shipstation-client --help
```

```bash
poetry run shipstation-client --name Roman
```

### Makefile usage

[`Makefile`](https://github.com/agritheory/shipstation-client/blob/master/Makefile) contains many functions for fast assembling and convenient work.

<details>
<summary>1. Download Poetry</summary>
<p>

```bash
make download-poetry
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

```bash
make install
```

If you do not want to install pre-commit hooks, run the command with the NO_PRE_COMMIT flag:

```bash
make install NO_PRE_COMMIT=1
```

</p>
</details>

<details>
<summary>3. Check the security of your code</summary>
<p>

```bash
make check-safety
```

This command launches a `Poetry` and `Pip` integrity check as well as identifies security issues with `Bandit`. By default, the build will not crash if any of the items fail. But you can set `STRICT=1` for the entire build, or you can configure strictness for each item separately.

```bash
make check-safety STRICT=1
```

> List of flags for `check-safety` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `BANDIT_STRICT`.

</p>
</details>

<details>
<summary>4. Check the codestyle</summary>
<p>

The command is similar to `check-safety` but to check the code style, obviously. It uses `Black`, `Isort`, and `Mypy` inside.

```bash
make check-style
```

It may also contain the `STRICT` flag.

```bash
make check-style STRICT=1
```

> List of flags for `check-style` (can be set to `1` or `0`): `STRICT`, `BLACK_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>5. Run all the codestyle formaters</summary>
<p>

Codestyle uses `pre-commit` hooks, so ensure you've run `make install` before.

```bash
make codestyle
```

</p>
</details>

<details>
<summary>6. Run tests</summary>
<p>

```bash
make test
```

</p>
</details>

<details>
<summary>7. Run all the linters</summary>
<p>

```bash
make lint
```

the same as:

```bash
make test && make check-safety && make check-style
```

> List of flags for `lint` (can be set to `1` or `0`): `STRICT`, `POETRY_STRICT`, `PIP_STRICT`, `BANDIT_STRICT`, `BLACK_STRICT`, `ISORT_STRICT`, `MYPY_STRICT`.

</p>
</details>

<details>
<summary>8. Build docker</summary>
<p>

```bash
make docker
```

which is equivalent to:

```bash
make docker VERSION=latest
```

More information [here](https://github.com/agritheory/shipstation-client/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup docker</summary>
<p>

```bash
make clean_docker
```

or to remove all build

```bash
make clean
```

More information [here](https://github.com/agritheory/shipstation-client/tree/master/docker).

</p>
</details>


## 🛡 License

[![License](https://img.shields.io/github/license/agritheory/shipstation-client)](https://github.com/agritheory/shipstation-client/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/agritheory/shipstation-client/blob/master/LICENSE) for more details.

## 📃 Citation

```
@misc{shipstation-client,
  author = {AgriTheory},
  title = {`shipstation-client` is a Python cli/package created with https://github.com/TezRomacH/python-package-template},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/agritheory/shipstation-client}}
}
```

## Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).
