# clone-labels

A Python script to migrate or copy labels between GitHub repositories.

## Description

`clone-labels` is a Python script that uses the GitHub API to copy labels from one repository to multiple other repositories. This is useful for developers who want to maintain consistent labelling across multiple projects.

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/axiomatic-aardvark/clone-labels.git
   ```
2. Navigate into the cloned project directory:
   ```shell
   cd clone-labels
   ```
3. Install the required Python packages:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Open the script `clone_labels.py` in a text editor.
2. Replace `GH_PAT_TOKEN` with your actual GitHub personal access token.
3. Replace `<username>/<source repository name>` with your username and the name of the repository from which you want to copy the labels.
4. Replace `target_repo_names` with the names of the repositories where you want to copy the labels to.
5. Save and close the file.
6. Run the script:
   ```shell
   python clone_labels.py
   ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
