# General

* **Include a disclaimer:** State explicitly that the creator of the package is not responsible for any usage of the package by users.
* **Specify intended purpose:** Clearly outline the intended purpose and appropriate use of the package.
* **Highlight user responsibility:** Emphasize that users are responsible for understanding the implications and potential risks associated with using the package.

**In the package code:**

* **Add a comment at the beginning of the package:** Include a comment indicating the creator's non-responsibility for usage.
* **Use header files:** Add a header file to each module or component of the package that includes the disclaimer.

**Additional measures:**

* **Version Control:** Maintain a clear version control history to track changes and demonstrate the evolution of the package.
* **Open Source License:** Choose an open-source license that includes a clause limiting the creator's liability, such as the MIT License or the Apache License 2.0.
* **Community Engagement:** Encourage users to contribute to the package and provide feedback. This helps foster a sense of shared responsibility.
* **Bug Reporting and Support:** Establish a mechanism for users to report bugs or seek support. This can help identify and mitigate potential risks.
* **Regular Updates:** Regularly update the package with bug fixes and security patches to address any potential vulnerabilities.

**Example Disclaimer:**

```
**Disclaimer:** The creator of this package assumes no responsibility or liability for any usage of the package by users. Users are solely responsible for understanding the implications and potential risks associated with using the package. The intended purpose of the package is [briefly state the purpose]. Misuse or unintended use of the package is at the user's own risk.
```

# License

```
[License](LICENSE.md)
```

# Install from git
```sh
pip install --user git+https://github.com/rafaelang/gemini-personal-cli.git;
export GCLI_GOOGLE_API_KEY=**************************
```


# Usage

```sh
gcli "Question..."
```


# Install from download/clone

```sh
pip install --user [DOWNLOAD PACKAGE]/dist/geminicli-0.1.0-py3-none-any.whl
export GCLI_GOOGLE_API_KEY=**************************
```


