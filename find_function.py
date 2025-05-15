import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def main():
    # Input Variables
    file_name = 'schema.sql'
    file_path = '/Users/Vkirubakaran/Downloads/test_schema_search'
    output_file = '/Users/Vkirubakaran/Downloads/merged_schema.sql'

    matching_files = find_all(file_name, file_path)

    with open(output_file, 'w') as outf:
        for file in matching_files:
            with open(file, 'r') as f:
                outf.write(f.read())
                outf.write("\n\n")

if __name__ == "__main__":
    main()